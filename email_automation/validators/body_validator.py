"""
Body validator – checks that required keywords exist in the normalised
email body and (for Email 1) that a 6-digit OTP is present.
"""
import logging
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from email_automation.utils.text_normalizer import TextNormalizer

logger = logging.getLogger(__name__)


@dataclass
class BodyValidationResult:
    passed: bool
    email_id: str
    keywords_found: Dict[str, bool] = field(default_factory=dict)
    otp_found: Optional[bool] = None   # None if not applicable
    missing_keywords: List[str] = field(default_factory=list)
    message: str = ""

    def __str__(self) -> str:
        status = "PASS" if self.passed else "FAIL"
        missing = ", ".join(self.missing_keywords) if self.missing_keywords else "none"
        return (
            f"[{status}] Body({self.email_id}): "
            f"missing_keywords=[{missing}] | {self.message}"
        )


class BodyValidator:
    """Validates email body content using keyword-presence checks."""

    def __init__(self) -> None:
        self._normalizer = TextNormalizer()

    def validate(
        self,
        email_id: str,
        body_html: str,
        required_keywords: List[str],
        *,
        check_otp: bool = False,
        first_name: Optional[str] = None,
    ) -> BodyValidationResult:
        """
        Args:
            email_id:          e.g. "email_1"
            body_html:         Raw HTML body from Gmail.
            required_keywords: List of phrases that must appear in the body.
            check_otp:         True for Email 1 – additionally verify a 6-digit OTP exists.
            first_name:        If provided, {first_name} in keywords is resolved.
        """
        # Normalise keywords (resolve {first_name} if supplied)
        resolved_keywords = [
            (kw.replace("{first_name}", first_name) if first_name else kw)
            for kw in required_keywords
        ]

        keywords_found = self._normalizer.keywords_present(
            body_html, resolved_keywords, is_html=True
        )
        missing = [kw for kw, found in keywords_found.items() if not found]

        # OTP check (Email 1)
        otp_found: Optional[bool] = None
        if check_otp:
            body_text = self._normalizer.html_to_text(body_html)
            otp_found = self._normalizer.contains_six_digit_otp(body_text)
            if not otp_found:
                missing.append("<6-digit OTP>")

        passed = len(missing) == 0
        msg = f"{len(keywords_found) - len(missing)}/{len(keywords_found)} keywords found"
        if check_otp:
            msg += f" | OTP present: {otp_found}"

        return BodyValidationResult(
            passed=passed,
            email_id=email_id,
            keywords_found=keywords_found,
            otp_found=otp_found,
            missing_keywords=missing,
            message=msg,
        )
