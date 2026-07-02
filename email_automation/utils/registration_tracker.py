"""
Persists registration history across GitHub Action runs.

Stores a list of RegistrationRecord objects in a JSON file so that
daily validation runs can find the registered email address and determine
which emails are due today.
"""
import json
import logging
from dataclasses import asdict, dataclass, field
from typing import List, Optional

from email_automation.config.constants import (
    REGISTRATION_ACTIVE_DAYS,
    REGISTRATION_HISTORY_FILE,
)
from email_automation.utils.date_helper import days_since, iso_now, iso_date_today

logger = logging.getLogger(__name__)


@dataclass
class ValidationRun:
    """Records the outcome of a single daily validation pass."""
    run_date: str
    emails_checked: List[str]
    emails_passed: List[str]
    emails_failed: List[str]
    emails_missing: List[str]
    notes: str = ""


@dataclass
class RegistrationRecord:
    """All data captured during one registration + its subsequent validations."""
    email: str
    first_name: str
    last_name: str
    registration_time: str           # ISO-8601 UTC
    registration_date: str           # YYYY-MM-DD
    status: str                      # "active" | "completed" | "failed"
    emails_validated: List[str] = field(default_factory=list)
    last_validation: Optional[str] = None
    execution_history: List[dict] = field(default_factory=list)


class RegistrationTracker:
    """Read / write helper for registration_history.json."""

    def __init__(self, history_file: str = REGISTRATION_HISTORY_FILE) -> None:
        self.history_file = history_file

    # ── Public API ────────────────────────────────────────────────────────────

    def load_history(self) -> List[RegistrationRecord]:
        try:
            with open(self.history_file, "r", encoding="utf-8") as fh:
                raw = json.load(fh)
            return [RegistrationRecord(**r) for r in raw.get("registrations", [])]
        except FileNotFoundError:
            return []
        except Exception as exc:
            logger.error("Failed to load registration history: %s", exc)
            return []

    def save_history(self, records: List[RegistrationRecord]) -> None:
        data = {"registrations": [asdict(r) for r in records]}
        try:
            with open(self.history_file, "w", encoding="utf-8") as fh:
                json.dump(data, fh, indent=2, ensure_ascii=False)
            logger.info("Registration history saved (%d records).", len(records))
        except Exception as exc:
            logger.error("Failed to save registration history: %s", exc)

    def get_active_registration(self) -> Optional[RegistrationRecord]:
        """
        Return the most recent registration that is still within the
        journey window (active for up to REGISTRATION_ACTIVE_DAYS days).
        """
        records = self.load_history()
        for rec in reversed(records):
            if rec.status in ("active", "completed"):
                age = days_since(rec.registration_time)
                if age <= REGISTRATION_ACTIVE_DAYS:
                    return rec
        return None

    def needs_registration(self) -> bool:
        """True if no active registration exists and a new one should be run."""
        return self.get_active_registration() is None

    def add_registration(
        self, email: str, first_name: str, last_name: str
    ) -> RegistrationRecord:
        """Create a new record and append it to history."""
        records = self.load_history()
        rec = RegistrationRecord(
            email=email,
            first_name=first_name,
            last_name=last_name,
            registration_time=iso_now(),
            registration_date=iso_date_today(),
            status="active",
        )
        records.append(rec)
        self.save_history(records)
        logger.info("New registration recorded: %s", email)
        return rec

    def mark_email_validated(
        self, registration_email: str, email_id: str, status: str
    ) -> None:
        """Append an email_id to the validated list of a registration record."""
        records = self.load_history()
        for rec in records:
            if rec.email == registration_email:
                if email_id not in rec.emails_validated:
                    rec.emails_validated.append(email_id)
                rec.last_validation = iso_now()
                if rec.status == "active" and status == "failed":
                    pass  # keep active; individual failure tracked in history
                break
        self.save_history(records)

    def record_validation_run(
        self, registration_email: str, run: ValidationRun
    ) -> None:
        """Append a full ValidationRun to a record's execution_history."""
        records = self.load_history()
        for rec in records:
            if rec.email == registration_email:
                rec.execution_history.append(asdict(run))
                rec.last_validation = iso_now()
                # Mark completed if all 11 emails have been validated
                if len(set(rec.emails_validated)) >= 11:
                    rec.status = "completed"
                break
        self.save_history(records)

    def get_days_since_registration(self, registration_email: str) -> int:
        """Return days elapsed since the given registration email was registered."""
        records = self.load_history()
        for rec in records:
            if rec.email == registration_email:
                return days_since(rec.registration_time)
        return 0
