"""
Scheduler – determines what the daily GitHub Action run should do:
  1. Register a new user (if no active registration exists), OR
  2. Validate the emails expected for today based on days since registration.

Uses RegistrationTracker for state persistence across runs.
"""
import logging
from dataclasses import dataclass, field
from typing import List, Optional

from email_automation.config.email_chain import EmailDefinition
from email_automation.config.email_schedule import get_emails_for_day
from email_automation.utils.registration_tracker import RegistrationRecord, RegistrationTracker
from email_automation.utils.date_helper import days_since

logger = logging.getLogger(__name__)


@dataclass
class SchedulePlan:
    """Describes what the current run should do."""
    needs_registration: bool
    active_registration: Optional[RegistrationRecord]
    days_since_registration: int
    emails_to_validate: List[EmailDefinition] = field(default_factory=list)
    notes: str = ""

    def summary(self) -> str:
        lines = [
            f"needs_registration : {self.needs_registration}",
            f"days_since_reg     : {self.days_since_registration}",
            f"emails_to_validate : {[e.email_id for e in self.emails_to_validate]}",
        ]
        if self.notes:
            lines.append(f"notes              : {self.notes}")
        return "\n".join(lines)


class Scheduler:
    """
    Reads registration history and produces a SchedulePlan
    that drives the GitHub Action for the day.
    """

    def __init__(
        self, tracker: Optional[RegistrationTracker] = None
    ) -> None:
        self._tracker = tracker or RegistrationTracker()

    def get_plan(self) -> SchedulePlan:
        """Return the SchedulePlan for today's run."""
        active = self._tracker.get_active_registration()

        if active is None:
            logger.info("No active registration found – new registration required.")
            return SchedulePlan(
                needs_registration=True,
                active_registration=None,
                days_since_registration=0,
                emails_to_validate=[],
                notes="New registration will be performed before email validation.",
            )

        day = days_since(active.registration_time)
        emails_today = get_emails_for_day(day)

        # Filter out emails already validated successfully
        emails_to_run = [
            e for e in emails_today
            if e.email_id not in active.emails_validated
        ]

        logger.info(
            "Active registration: %s | Day %d | Emails today: %s",
            active.email,
            day,
            [e.email_id for e in emails_to_run],
        )

        return SchedulePlan(
            needs_registration=False,
            active_registration=active,
            days_since_registration=day,
            emails_to_validate=emails_to_run,
            notes=(
                f"Validating {len(emails_to_run)} email(s) for Day {day} "
                f"of registration {active.email}"
            ),
        )

    def build_registration_data(self, record: RegistrationRecord) -> dict:
        """
        Build the registration_data dict consumed by EmailValidator.
        Converts RegistrationRecord to the expected format.
        Includes pre-computed (after_date, before_date) windows for every
        email in the chain so tests can look them up without inline calculation.
        """
        from email_automation.utils.date_helper import to_gmail_date_str, email_date_window
        from email_automation.config.email_chain import EMAIL_CHAIN
        from datetime import datetime, timezone

        reg_time = datetime.fromisoformat(record.registration_time)
        if reg_time.tzinfo is None:
            reg_time = reg_time.replace(tzinfo=timezone.utc)

        reg_date_gmail = to_gmail_date_str(reg_time)

        email_date_windows = {
            e.email_id: email_date_window(reg_date_gmail, e.day_offset)
            for e in EMAIL_CHAIN
        }

        return {
            "email": record.email,
            "first_name": record.first_name,
            "last_name": record.last_name,
            "registration_date_gmail": reg_date_gmail,
            "email_date_windows": email_date_windows,
        }
