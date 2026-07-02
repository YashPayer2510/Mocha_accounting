"""
Recipient validator – confirms an email was delivered to the registered
address (supports Gmail plus-addressing).
"""
import logging
from dataclasses import dataclass

from email_automation.utils.gmail_helper import EmailData

logger = logging.getLogger(__name__)


@dataclass
class RecipientValidationResult:
    passed: bool
    email_id: str
    expected_recipient: str
    actual_to_header: str
    actual_delivered_to: str
    message: str = ""

    def __str__(self) -> str:
        status = "PASS" if self.passed else "FAIL"
        return (
            f"[{status}] Recipient({self.email_id}): "
            f"expected='{self.expected_recipient}' | "
            f"To='{self.actual_to_header}' | {self.message}"
        )


class RecipientValidator:
    """Validates email recipient using To / Delivered-To headers."""

    def validate(
        self,
        email_id: str,
        email_data: EmailData,
        expected_recipient: str,
    ) -> RecipientValidationResult:
        expected_lower = expected_recipient.lower().strip()

        # Check both To and Delivered-To (Gmail routes plus-addresses to base inbox)
        found = any(
            expected_lower in header.lower()
            for header in (email_data.recipient, email_data.delivered_to)
            if header
        )

        msg = "recipient matches" if found else (
            f"'{expected_recipient}' not found in To='{email_data.recipient}' "
            f"or Delivered-To='{email_data.delivered_to}'"
        )

        return RecipientValidationResult(
            passed=found,
            email_id=email_id,
            expected_recipient=expected_recipient,
            actual_to_header=email_data.recipient,
            actual_delivered_to=email_data.delivered_to,
            message=msg,
        )
