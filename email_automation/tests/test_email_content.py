"""
Tests for email body content validation.
Verifies keyword presence, OTP detection, normalisation behaviour,
and placeholder substitution.
"""
import pytest

from email_automation.config.email_chain import EMAIL_CHAIN, EMAIL_CHAIN_MAP
from email_automation.validators.body_validator import BodyValidator
from email_automation.utils.text_normalizer import TextNormalizer


# ── Unit tests ────────────────────────────────────────────────────────────────

class TestBodyValidatorUnit:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.validator = BodyValidator()
        self.normalizer = TextNormalizer()
        self.first_name = "Automation_FN_20250701_120000"

    # ── Normalisation behaviour ───────────────────────────────────────────────

    def test_html_entities_decoded(self):
        html = "<p>Track your Q&amp;A session here</p>"
        norm = self.normalizer.normalize_html(html)
        assert "q&a session" in norm

    def test_extra_whitespace_collapsed(self):
        html = "<p>Hello    World   </p>"
        norm = self.normalizer.normalize_html(html)
        assert "hello world" in norm

    def test_html_tags_stripped(self):
        html = "<b>Bold</b> <i>Italic</i> plain"
        norm = self.normalizer.normalize_html(html)
        assert "<b>" not in norm
        assert "bold italic plain" in norm

    def test_multi_line_text_normalised(self):
        html = "<p>Line one\n\n\nLine two</p>"
        norm = self.normalizer.normalize_html(html)
        assert "line one line two" in norm

    def test_unicode_normalised(self):
        text = "Café – test"  # é and –
        norm = self.normalizer.normalize(text)
        assert "cafe" in norm or "café" in norm  # NFKD may decompose

    # ── Keyword matching ──────────────────────────────────────────────────────

    def test_keyword_found_in_plain_body(self):
        html = "<p>Thank you for choosing Mocha Accounting for your business needs.</p>"
        result = self.validator.validate(
            "email_1", html,
            ["thank you for choosing mocha accounting"],
        )
        assert result.passed, str(result)

    def test_missing_keyword_fails(self):
        html = "<p>Some unrelated content here.</p>"
        result = self.validator.validate(
            "email_1", html,
            ["thank you for choosing mocha accounting"],
        )
        assert not result.passed
        assert "thank you for choosing mocha accounting" in result.missing_keywords

    def test_all_keywords_must_be_present(self):
        html = "<p>Keyword A but not the second one.</p>"
        result = self.validator.validate(
            "test", html,
            ["keyword a", "keyword b"],
        )
        assert not result.passed
        assert "keyword b" in result.missing_keywords

    def test_keyword_check_is_case_insensitive(self):
        html = "<p>INVOICING MADE SIMPLE</p>"
        result = self.validator.validate(
            "email_2", html, ["invoicing made simple"]
        )
        assert result.passed

    def test_keyword_check_ignores_formatting_tags(self):
        html = "<p><b>Invoicing</b> <em>Made</em> <u>Simple</u></p>"
        result = self.validator.validate(
            "email_2", html, ["invoicing made simple"]
        )
        assert result.passed

    # ── OTP check (Email 1) ───────────────────────────────────────────────────

    def test_otp_detected_in_body(self):
        html = "<p>Your verification code is: 837291</p>"
        result = self.validator.validate(
            "email_1", html, [], check_otp=True
        )
        assert result.otp_found is True
        assert result.passed

    def test_otp_missing_fails_when_required(self):
        html = "<p>No code here, just text.</p>"
        result = self.validator.validate(
            "email_1", html, [], check_otp=True
        )
        assert result.otp_found is False
        assert not result.passed
        assert "<6-digit OTP>" in result.missing_keywords

    def test_five_digit_number_not_treated_as_otp(self):
        html = "<p>Your code is 12345 only.</p>"
        assert not self.normalizer.contains_six_digit_otp("your code is 12345 only")

    def test_six_digit_number_treated_as_otp(self):
        assert self.normalizer.contains_six_digit_otp("code is 123456 valid")

    # ── Placeholder substitution ──────────────────────────────────────────────

    def test_first_name_placeholder_resolved_in_keywords(self):
        """A keyword containing {first_name} should be resolved before matching."""
        html = f"<p>Welcome to Mocha Accounting, {self.first_name}!</p>"
        result = self.validator.validate(
            "email_2", html,
            ["{first_name}"],
            first_name=self.first_name,
        )
        assert result.passed, str(result)

    # ── Email 2 keywords ──────────────────────────────────────────────────────

    def test_email_2_required_keywords_pass_on_full_body(self):
        """Simulate a realistic Email 2 body and verify all keywords are found."""
        html = """
        <html><body>
        <p>Welcome to Mocha Accounting, Automation_FN!</p>
        <p>Congratulations! Your Mocha Accounting account is now fully verified and ready to go.</p>
        <h3>Invoicing Made Simple</h3><p>Create professional invoices in minutes.</p>
        <h3>Inventory Management</h3><p>Keep real-time track of your stock levels.</p>
        <h3>Purchase Order Tracking</h3><p>Streamline your procurement process.</p>
        <h3>Quick Start Guide</h3>
        <p>Need help? Contact support@mochatechnologies.com</p>
        </body></html>
        """
        email_def = EMAIL_CHAIN_MAP["email_2"]
        result = self.validator.validate(
            "email_2", html, email_def.required_keywords
        )
        assert result.passed, f"Missing: {result.missing_keywords}"

    # ── Demo invitation keywords ──────────────────────────────────────────────

    def test_email_3_demo_keywords_present(self):
        html = """
        <html><body>
        <p>Ready to unlock the full potential of Mocha Accounting?
        We're offering you a free, personalized walkthrough that will show you exactly
        how our software can transform your business financial management.</p>
        <p>Reduce accounting errors by up to 75%. Zero cost, No obligation demo.
        Save 80+ hours of manual work monthly.</p>
        <p>Can't find a time? Email support@mochatechnologies.com</p>
        <a href="#">Schedule Your Free 1:1 Session</a>
        </body></html>
        """
        email_def = EMAIL_CHAIN_MAP["email_3"]
        result = self.validator.validate("email_3", html, email_def.required_keywords)
        assert result.passed, f"Missing: {result.missing_keywords}"

    def test_duplicate_keyword_does_not_fail(self):
        html = "<p>invoicing made simple invoicing made simple</p>"
        result = self.validator.validate(
            "test", html, ["invoicing made simple"]
        )
        assert result.passed


# ── Integration tests (live Gmail) ────────────────────────────────────────────

class TestBodyValidationLive:
    """Live Gmail body tests – skip if email not yet received."""

    @pytest.mark.parametrize("email_id", [
        "email_1", "email_2", "email_3", "email_3_1",
        "email_4", "email_4_1", "email_5", "email_5_1",
        "email_6", "email_7", "email_7_1",
    ])
    def test_email_body_contains_required_keywords(
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

        after_date, before_date = registration_data["email_date_windows"][email_id]
        email_data = gmail_helper.find_email_by_subject(
            subject_fragment=email_def.subject_search_fragment,
            after_date=after_date,
            before_date=before_date,
            recipient=registration_data.get("email"),
        )
        if email_data is None:
            pytest.fail(f"{email_id} not found in Gmail inbox.")

        body = email_data.body_html or email_data.body_plain
        validator = BodyValidator()
        result = validator.validate(
            email_id=email_id,
            body_html=body,
            required_keywords=email_def.required_keywords,
            check_otp=(email_id == "email_1"),
            first_name=registration_data.get("first_name"),
        )
        assert result.passed, (
            f"{email_id} body validation failed.\n"
            f"Missing keywords: {result.missing_keywords}"
        )
