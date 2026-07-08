"""
Tests for email recipient validation.
Ensures every onboarding email is addressed to the registered Gmail address.
"""
import pytest
from dataclasses import dataclass
from datetime import datetime, timezone

from email_automation.config.email_chain import EMAIL_CHAIN_MAP
from email_automation.utils.gmail_helper import EmailData
from email_automation.validators.recipient_validator import RecipientValidator
from email_automation.utils.date_helper import email_date_window


# ── Unit tests (no live Gmail) ────────────────────────────────────────────────

class TestRecipientValidatorUnit:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.validator = RecipientValidator()
        self.registered_email = "mochaautotest+20250701120000@gmail.com"

    def _make_email_data(self, to_header: str, delivered_to: str = "") -> EmailData:
        return EmailData(
            message_id="msg001",
            thread_id="thread001",
            subject="Test",
            sender="noreply@mochaaccounting.com",
            recipient=to_header,
            delivered_to=delivered_to or to_header,
            received_time=datetime.now(timezone.utc),
            body_plain="",
            body_html="",
            snippet="",
        )

    def test_exact_recipient_passes(self):
        data = self._make_email_data(self.registered_email)
        result = self.validator.validate("email_1", data, self.registered_email)
        assert result.passed, str(result)

    def test_wrong_recipient_fails(self):
        data = self._make_email_data("different@example.com")
        result = self.validator.validate("email_1", data, self.registered_email)
        assert not result.passed, "Wrong recipient should fail"

    def test_plus_addressed_recipient_passes(self):
        """Plus-addressing: To may be the full +timestamp address."""
        data = self._make_email_data(
            to_header=self.registered_email,
            delivered_to=self.registered_email,
        )
        result = self.validator.validate("email_1", data, self.registered_email)
        assert result.passed

    def test_recipient_in_delivered_to_only_passes(self):
        """Gmail may put base address in To and plus address in Delivered-To."""
        data = self._make_email_data(
            to_header="mochaautotest@gmail.com",
            delivered_to=self.registered_email,
        )
        result = self.validator.validate("email_1", data, self.registered_email)
        assert result.passed, "Should find registered email in Delivered-To"

    def test_recipient_check_is_case_insensitive(self):
        data = self._make_email_data(self.registered_email.upper())
        result = self.validator.validate("email_1", data, self.registered_email)
        assert result.passed

    def test_empty_registered_email_skipped(self):
        """Validator should not crash on empty expected recipient."""
        data = self._make_email_data(self.registered_email)
        result = self.validator.validate("email_1", data, "")
        # Empty expected = substring "" is in every string, so passes
        assert result.passed

    def test_result_contains_actual_header_values(self):
        data = self._make_email_data(
            "Mismatch <other@example.com>", "other@example.com"
        )
        result = self.validator.validate("email_2", data, self.registered_email)
        assert result.actual_to_header == "Mismatch <other@example.com>"


# ── Integration tests (live Gmail) ────────────────────────────────────────────

class TestRecipientValidationLive:

    @pytest.mark.parametrize("email_id", [
        "email_1", "email_2", "email_3", "email_3_1",
        "email_4", "email_4_1", "email_5", "email_5_1",
        "email_6", "email_7", "email_7_1",
    ])
    def test_email_delivered_to_registered_address(
        self,
        gmail_helper,
        registration_data,
        days_since_registration,
        email_id,
    ):
        email_def = EMAIL_CHAIN_MAP[email_id]
        if email_def.day_offset > days_since_registration:
            pytest.skip(
                f"{email_id} expected on Day {email_def.day_offset}; "
                f"currently Day {days_since_registration}."
            )

        after_date, before_date = email_date_window(
            registration_data["registration_date_gmail"], email_def.day_offset
        )
        email_data = gmail_helper.find_email_by_subject(
            subject_fragment=email_def.subject_search_fragment,
            after_date=after_date,
            before_date=before_date,
            recipient=registration_data.get("email"),
        )
        if email_data is None:
            pytest.fail(f"{email_id} not found in Gmail inbox.")

        validator = RecipientValidator()
        result = validator.validate(
            email_id=email_id,
            email_data=email_data,
            expected_recipient=registration_data["email"],
        )
        assert result.passed, str(result)
