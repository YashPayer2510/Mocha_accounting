"""
EmailService – high-level orchestration layer.

Ties together the Scheduler, GmailHelper, EmailValidator, and
RegistrationTracker to validate the complete email journey.
Designed to be called from pytest tests and from the GitHub Action.
"""
import logging
from datetime import datetime, timezone
from typing import List, Optional

from email_automation.config.email_chain import EMAIL_CHAIN_MAP, EmailDefinition
from email_automation.services.scheduler import Scheduler, SchedulePlan
from email_automation.utils.gmail_helper import GmailHelper
from email_automation.utils.registration_tracker import RegistrationTracker, ValidationRun
from email_automation.validators.email_validator import EmailValidator, ValidationResult
from email_automation.utils.date_helper import iso_date_today

logger = logging.getLogger(__name__)


class EmailService:
    """
    Entry point for running email chain validations.

    Typical daily flow
    ──────────────────
    service = EmailService()
    results = service.validate_todays_emails()
    """

    def __init__(
        self,
        tracker: Optional[RegistrationTracker] = None,
        gmail: Optional[GmailHelper] = None,
    ) -> None:
        self._tracker = tracker or RegistrationTracker()
        self._scheduler = Scheduler(self._tracker)
        self._gmail = gmail or GmailHelper()

    # ── Public API ────────────────────────────────────────────────────────────

    def get_todays_plan(self) -> SchedulePlan:
        """Return the scheduler plan without running any validations."""
        return self._scheduler.get_plan()

    def validate_todays_emails(
        self,
        retries: int = 5,
        retry_delay: int = 30,
    ) -> List[ValidationResult]:
        """
        Validate all emails expected for today.
        Returns one ValidationResult per expected email.
        Does NOT raise; failures are captured inside ValidationResult.
        """
        plan = self._scheduler.get_plan()

        if plan.needs_registration:
            logger.warning(
                "validate_todays_emails() called but no active registration exists. "
                "Run the registration test first."
            )
            return []

        if not plan.emails_to_validate:
            logger.info(
                "No emails expected for Day %d of registration %s.",
                plan.days_since_registration,
                plan.active_registration.email,  # type: ignore[union-attr]
            )
            return []

        reg_data = self._scheduler.build_registration_data(plan.active_registration)  # type: ignore[arg-type]
        validator = EmailValidator(self._gmail, reg_data)

        results: List[ValidationResult] = []
        for email_def in plan.emails_to_validate:
            result = self._safe_validate(validator, email_def, retries, retry_delay)
            results.append(result)
            # Update tracker regardless of pass/fail
            self._tracker.mark_email_validated(
                registration_email=plan.active_registration.email,  # type: ignore[union-attr]
                email_id=email_def.email_id,
                status="passed" if result.passed else "failed",
            )

        # Persist the full run summary
        run = ValidationRun(
            run_date=iso_date_today(),
            emails_checked=[r.email_id for r in results],
            emails_passed=[r.email_id for r in results if r.passed],
            emails_failed=[r.email_id for r in results if not r.passed and r.email_found],
            emails_missing=[r.email_id for r in results if not r.email_found],
        )
        self._tracker.record_validation_run(
            registration_email=plan.active_registration.email,  # type: ignore[union-attr]
            run=run,
        )

        self._log_summary(results)
        return results

    def validate_single_email(
        self,
        email_id: str,
        retries: int = 5,
        retry_delay: int = 30,
    ) -> Optional[ValidationResult]:
        """Validate one specific email by ID (useful for targeted re-runs)."""
        email_def = EMAIL_CHAIN_MAP.get(email_id)
        if not email_def:
            logger.error("Unknown email_id: %s", email_id)
            return None

        plan = self._scheduler.get_plan()
        if plan.active_registration is None:
            logger.error("No active registration; cannot validate.")
            return None

        reg_data = self._scheduler.build_registration_data(plan.active_registration)
        validator = EmailValidator(self._gmail, reg_data)
        return self._safe_validate(validator, email_def, retries, retry_delay)

    # ── Private helpers ───────────────────────────────────────────────────────

    @staticmethod
    def _safe_validate(
        validator: EmailValidator,
        email_def: EmailDefinition,
        retries: int,
        retry_delay: int,
    ) -> ValidationResult:
        try:
            return validator.validate(email_def, retries=retries, retry_delay=retry_delay)
        except Exception as exc:
            logger.exception("Unexpected error validating %s", email_def.email_id)
            from email_automation.validators.email_validator import ValidationResult
            return ValidationResult(
                passed=False,
                email_id=email_def.email_id,
                email_name=email_def.name,
                errors=[str(exc)],
            )

    @staticmethod
    def _log_summary(results: List[ValidationResult]) -> None:
        passed = sum(1 for r in results if r.passed)
        total = len(results)
        logger.info("=" * 60)
        logger.info("Validation summary: %d/%d passed", passed, total)
        for r in results:
            logger.info("  %s", r.summary_line())
        logger.info("=" * 60)
