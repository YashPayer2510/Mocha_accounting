"""
EmailValidator – orchestrates subject, body, and recipient validation
for a single EmailDefinition and returns a unified result.
"""
import logging
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from email_automation.config.email_chain import EmailDefinition
from email_automation.config.constants import SENDER_EMAIL
from email_automation.utils.gmail_helper import EmailData, GmailHelper
from email_automation.utils.date_helper import to_gmail_date_str
from email_automation.validators.subject_validator import SubjectValidator, SubjectValidationResult
from email_automation.validators.body_validator import BodyValidator, BodyValidationResult
from email_automation.validators.recipient_validator import RecipientValidator, RecipientValidationResult

logger = logging.getLogger(__name__)


@dataclass
class ValidationResult:
    passed: bool
    email_id: str
    email_name: str
    subject_result: Optional[SubjectValidationResult] = None
    body_result: Optional[BodyValidationResult] = None
    recipient_result: Optional[RecipientValidationResult] = None
    sender_verified: bool = False
    email_found: bool = False
    errors: list = field(default_factory=list)

    def summary_line(self) -> str:
        status = "PASS" if self.passed else "FAIL"
        parts = [f"[{status}] {self.email_id} ({self.email_name})"]
        if not self.email_found:
            parts.append("EMAIL NOT FOUND")
        else:
            if self.subject_result:
                parts.append(f"Subject={'OK' if self.subject_result.passed else 'FAIL'}")
            if self.body_result:
                parts.append(f"Body={'OK' if self.body_result.passed else 'FAIL'}")
            if self.recipient_result:
                parts.append(f"Recipient={'OK' if self.recipient_result.passed else 'FAIL'}")
            parts.append(f"Sender={'OK' if self.sender_verified else 'FAIL'}")
        if self.errors:
            parts.append(f"errors={self.errors}")
        return " | ".join(parts)


class EmailValidator:
    """
    Validates one onboarding email against its EmailDefinition.

    Usage
    ─────
    validator = EmailValidator(gmail_helper, registration_data)
    result = validator.validate(email_def, registration_date_str)
    """

    def __init__(
        self,
        gmail_helper: GmailHelper,
        registration_data: Dict[str, Any],
    ) -> None:
        self._gmail = gmail_helper
        self._reg_data = registration_data
        self._subject_v = SubjectValidator()
        self._body_v = BodyValidator()
        self._recipient_v = RecipientValidator()

    @property
    def _first_name(self) -> str:
        return self._reg_data.get("first_name", "")

    @property
    def _registered_email(self) -> str:
        return self._reg_data.get("email", "")

    @property
    def _registration_date(self) -> str:
        """Returns a Gmail-compatible date string 'YYYY/MM/DD'."""
        return self._reg_data.get("registration_date_gmail", "")

    def validate(
        self,
        email_def: EmailDefinition,
        retries: int = 5,
        retry_delay: int = 30,
    ) -> ValidationResult:
        """
        Fetch the email from Gmail and run all validations.
        Returns a ValidationResult regardless of whether the email arrived.
        """
        logger.info("Validating %s – '%s'", email_def.email_id, email_def.name)

        # ── 1. Fetch email ────────────────────────────────────────────────────
        email_data: Optional[EmailData] = self._gmail.wait_for_email(
            subject_fragment=email_def.subject_search_fragment,
            after_date=self._registration_date or None,
            recipient=self._registered_email or None,
            retries=retries,
            delay=retry_delay,
        )

        if email_data is None:
            logger.error("Email not found: %s", email_def.email_id)
            return ValidationResult(
                passed=False,
                email_id=email_def.email_id,
                email_name=email_def.name,
                email_found=False,
                errors=[f"Email '{email_def.name}' was not received."],
            )

        result = ValidationResult(
            passed=True,
            email_id=email_def.email_id,
            email_name=email_def.name,
            email_found=True,
        )

        # ── 2. Subject validation ─────────────────────────────────────────────
        try:
            result.subject_result = self._subject_v.validate(
                email_id=email_def.email_id,
                subject_template=email_def.subject_template,
                actual_subject=email_data.subject,
                first_name=self._first_name or None,
            )
            logger.info(result.subject_result)
        except Exception as exc:
            result.errors.append(f"Subject validation error: {exc}")
            result.passed = False

        # ── 3. Body validation ────────────────────────────────────────────────
        body_content = email_data.body_html or email_data.body_plain
        try:
            result.body_result = self._body_v.validate(
                email_id=email_def.email_id,
                body_html=body_content,
                required_keywords=email_def.required_keywords,
                check_otp=(email_def.email_id == "email_1"),
                first_name=self._first_name or None,
            )
            logger.info(result.body_result)
        except Exception as exc:
            result.errors.append(f"Body validation error: {exc}")
            result.passed = False

        # ── 4. Recipient validation ───────────────────────────────────────────
        if self._registered_email:
            try:
                result.recipient_result = self._recipient_v.validate(
                    email_id=email_def.email_id,
                    email_data=email_data,
                    expected_recipient=self._registered_email,
                )
                logger.info(result.recipient_result)
            except Exception as exc:
                result.errors.append(f"Recipient validation error: {exc}")
                result.passed = False

        # ── 5. Sender verification ────────────────────────────────────────────
        result.sender_verified = SENDER_EMAIL.lower() in email_data.sender.lower()
        if not result.sender_verified:
            result.errors.append(
                f"Unexpected sender '{email_data.sender}'; expected '{SENDER_EMAIL}'"
            )

        # ── 6. Roll up pass/fail ──────────────────────────────────────────────
        sub_ok = (result.subject_result is None or result.subject_result.passed)
        body_ok = (result.body_result is None or result.body_result.passed)
        rec_ok = (result.recipient_result is None or result.recipient_result.passed)
        result.passed = sub_ok and body_ok and rec_ok and result.sender_verified and not result.errors

        logger.info(result.summary_line())
        return result
