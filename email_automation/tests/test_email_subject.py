"""
Tests for email subject validation.
Covers positive, negative, and edge cases.
"""
import pytest

from email_automation.config.email_chain import EMAIL_CHAIN_MAP
from email_automation.validators.subject_validator import SubjectValidator
from email_automation.utils.text_normalizer import TextNormalizer


# ── Unit tests for SubjectValidator (no live Gmail) ───────────────────────────

class TestSubjectValidatorUnit:
    """Pure unit tests that do not require Gmail access."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.validator = SubjectValidator()
        self.first_name = "Automation_FN_20250701_120000"

    # ── Email 1 (OTP in subject) ──────────────────────────────────────────────

    def test_email_1_subject_passes_with_valid_otp(self):
        template = "Hi {first_name} , your signup code is {otp}"
        actual = f"Hi {self.first_name} , your signup code is 123456"
        result = self.validator.validate("email_1", template, actual, self.first_name)
        assert result.passed, str(result)

    def test_email_1_subject_fails_without_otp(self):
        template = "Hi {first_name} , your signup code is {otp}"
        actual = f"Hi {self.first_name} , your signup code is ABC"  # not 6 digits
        result = self.validator.validate("email_1", template, actual, self.first_name)
        assert not result.passed

    def test_email_1_subject_fails_with_wrong_first_name(self):
        template = "Hi {first_name} , your signup code is {otp}"
        actual = "Hi WrongName , your signup code is 123456"
        result = self.validator.validate("email_1", template, actual, self.first_name)
        # Wrong first name → mismatch in the non-OTP prefix
        assert not result.passed

    # ── Email 2 (first name only) ─────────────────────────────────────────────

    def test_email_2_subject_passes_with_correct_first_name(self):
        template = "Hi {first_name} , Welcome to Mocha! Here are your account details"
        actual = f"Hi {self.first_name} , Welcome to Mocha! Here are your account details"
        result = self.validator.validate("email_2", template, actual, self.first_name)
        assert result.passed, str(result)

    def test_email_2_subject_fails_with_different_first_name(self):
        template = "Hi {first_name} , Welcome to Mocha! Here are your account details"
        actual = "Hi DifferentName , Welcome to Mocha! Here are your account details"
        result = self.validator.validate("email_2", template, actual, self.first_name)
        assert not result.passed

    # ── Static subjects (Emails 3–7.1) ────────────────────────────────────────

    @pytest.mark.parametrize("email_id,expected_subject", [
        ("email_3",   "Start strong with a personalized Mocha walkthrough!"),
        ("email_3_1", "Still Curious About Mocha Accounting? Let's Connect!"),
        ("email_4",   "Simplify Your Finances with Mocha Accounting"),
        ("email_4_1", "Don't Miss Out: Your Accounting Game-Changer Awaits"),
        ("email_5",   "Master Your Invoicing with Mocha Accounting"),
        ("email_5_1", "We're Here to Help - Free Demo Invitation Still Open"),
        ("email_6",   "Take Control of Your Inventory with Mocha Accounting"),
        ("email_7",   "How a Hotel Business Saved 80 Hours Monthly with Mocha Accounting"),
        ("email_7_1", "Last Chance - Your Free Mocha Accounting Demo Ends Soon"),
    ])
    def test_static_subject_passes_exact_match(self, email_id, expected_subject):
        email_def = EMAIL_CHAIN_MAP[email_id]
        result = self.validator.validate(
            email_id, email_def.subject_template, expected_subject
        )
        assert result.passed, str(result)

    def test_wrong_subject_fails(self):
        email_def = EMAIL_CHAIN_MAP["email_3"]
        result = self.validator.validate(
            "email_3", email_def.subject_template, "Completely wrong subject"
        )
        assert not result.passed

    def test_empty_subject_fails(self):
        email_def = EMAIL_CHAIN_MAP["email_4"]
        result = self.validator.validate(
            "email_4", email_def.subject_template, ""
        )
        assert not result.passed

    def test_subject_comparison_is_case_insensitive(self):
        email_def = EMAIL_CHAIN_MAP["email_3"]
        result = self.validator.validate(
            "email_3",
            email_def.subject_template,
            "start strong with a personalized mocha walkthrough!",
        )
        assert result.passed, "Subject validation should be case-insensitive"

    def test_extra_whitespace_ignored(self):
        email_def = EMAIL_CHAIN_MAP["email_4"]
        spaced = "Simplify  Your  Finances  with  Mocha  Accounting"
        result = self.validator.validate(
            "email_4", email_def.subject_template, spaced
        )
        # Normaliser collapses whitespace; should still pass
        assert result.passed, "Extra whitespace should not cause failure"


# ── Integration tests (require active registration + Gmail) ───────────────────

class TestSubjectValidationLive:
    """Live Gmail tests – skip if no active registration."""

    def test_email_1_subject_in_inbox(
        self, gmail_helper, active_registration, registration_data
    ):
        """Verify Email 1 subject contains registered first name and a 6-digit OTP."""
        email_def = EMAIL_CHAIN_MAP["email_1"]
        email_data = gmail_helper.find_email_by_subject(
            subject_fragment=email_def.subject_search_fragment,
            after_date=registration_data.get("registration_date_gmail"),
        )
        if email_data is None:
            pytest.skip("Email 1 not yet received – skipping live subject test.")

        validator = SubjectValidator()
        result = validator.validate(
            email_id="email_1",
            subject_template=email_def.subject_template,
            actual_subject=email_data.subject,
            first_name=registration_data["first_name"],
        )
        assert result.passed, str(result)

    def test_email_2_subject_in_inbox(
        self, gmail_helper, active_registration, registration_data
    ):
        """Verify Email 2 subject contains the registered first name."""
        email_def = EMAIL_CHAIN_MAP["email_2"]
        email_data = gmail_helper.find_email_by_subject(
            subject_fragment=email_def.subject_search_fragment,
            after_date=registration_data.get("registration_date_gmail"),
        )
        if email_data is None:
            pytest.skip("Email 2 not yet received – skipping live subject test.")

        validator = SubjectValidator()
        result = validator.validate(
            email_id="email_2",
            subject_template=email_def.subject_template,
            actual_subject=email_data.subject,
            first_name=registration_data["first_name"],
        )
        assert result.passed, str(result)

    @pytest.mark.parametrize("email_id", [
        "email_3", "email_3_1", "email_4", "email_4_1",
        "email_5", "email_5_1", "email_6", "email_7", "email_7_1",
    ])
    def test_static_subject_in_inbox(
        self, gmail_helper, registration_data, days_since_registration, email_id
    ):
        """Verify static subject emails when their day has arrived."""
        email_def = EMAIL_CHAIN_MAP[email_id]
        if email_def.day_offset > days_since_registration:
            pytest.skip(
                f"{email_id} expected on Day {email_def.day_offset}; "
                f"currently Day {days_since_registration}."
            )
        email_data = gmail_helper.find_email_by_subject(
            subject_fragment=email_def.subject_search_fragment,
            after_date=registration_data.get("registration_date_gmail"),
        )
        if email_data is None:
            pytest.fail(
                f"{email_id} should have arrived by Day {days_since_registration} "
                f"but was not found in Gmail."
            )

        validator = SubjectValidator()
        result = validator.validate(
            email_id=email_id,
            subject_template=email_def.subject_template,
            actual_subject=email_data.subject,
        )
        assert result.passed, str(result)
