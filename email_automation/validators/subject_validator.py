"""
Subject validator – resolves placeholders then compares against the
actual email subject received from Gmail.

Strategy
────────
1. Substitute {first_name} with the captured registration first name.
2. For subjects containing {otp}, compile a regex (6-digit OTP is dynamic).
3. For purely static subjects, perform an exact normalised comparison.
"""
import logging
import re
from dataclasses import dataclass
from typing import Optional

from email_automation.utils.text_normalizer import TextNormalizer

logger = logging.getLogger(__name__)

_OTP_PATTERN = r"\d{6}"


@dataclass
class SubjectValidationResult:
    passed: bool
    email_id: str
    expected_template: str
    resolved_expected: str
    actual_subject: str
    message: str = ""

    def __str__(self) -> str:
        status = "PASS" if self.passed else "FAIL"
        return (
            f"[{status}] Subject({self.email_id}): "
            f"expected='{self.resolved_expected}' | actual='{self.actual_subject}' | {self.message}"
        )


class SubjectValidator:
    """Validates email subject lines with placeholder support."""

    def __init__(self) -> None:
        self._normalizer = TextNormalizer()

    def validate(
        self,
        email_id: str,
        subject_template: str,
        actual_subject: str,
        first_name: Optional[str] = None,
    ) -> SubjectValidationResult:
        """
        Validate *actual_subject* against *subject_template*.

        Args:
            email_id:         e.g. "email_1"
            subject_template: The template from EmailDefinition.
            actual_subject:   The raw subject from Gmail headers.
            first_name:       Registration first name; replaces {first_name}.
        """
        resolved = self._resolve_template(subject_template, first_name)
        actual_norm = self._normalizer.normalize_subject(actual_subject)

        # Subjects containing {otp} need regex matching
        if "{otp}" in subject_template:
            return self._validate_with_otp(email_id, subject_template, resolved, actual_norm)

        # Static or first-name-only subjects: normalised exact match
        resolved_norm = self._normalizer.normalize_subject(resolved)
        passed = resolved_norm.lower() == actual_norm.lower()
        msg = "exact match" if passed else f"mismatch (resolved='{resolved_norm}')"
        return SubjectValidationResult(
            passed=passed,
            email_id=email_id,
            expected_template=subject_template,
            resolved_expected=resolved,
            actual_subject=actual_subject,
            message=msg,
        )

    # ── Private helpers ───────────────────────────────────────────────────────

    def _resolve_template(self, template: str, first_name: Optional[str]) -> str:
        resolved = template
        if first_name:
            resolved = resolved.replace("{first_name}", first_name)
        return resolved

    def _validate_with_otp(
        self,
        email_id: str,
        template: str,
        resolved: str,
        actual_norm: str,
    ) -> SubjectValidationResult:
        """Build a regex from the resolved template and match against actual."""
        # Escape everything except the {otp} placeholder
        before_otp, _, after_otp = resolved.partition("{otp}")
        pattern = (
            re.escape(before_otp.strip().lower())
            + r"\s*"
            + _OTP_PATTERN
            + r"\s*"
            + re.escape(after_otp.strip().lower())
        )
        passed = bool(re.search(pattern, actual_norm.lower()))
        msg = "OTP regex match" if passed else f"OTP pattern '{pattern}' not found in subject"
        return SubjectValidationResult(
            passed=passed,
            email_id=email_id,
            expected_template=template,
            resolved_expected=resolved.replace("{otp}", "<OTP:6-digit>"),
            actual_subject=actual_norm,
            message=msg,
        )
