"""
End-to-end email chain tests.
Validates the full onboarding journey: registration history, email arrival,
report generation, and scheduler correctness across multiple days.
"""
import json
import os
import pytest

from email_automation.config.email_chain import EMAIL_CHAIN, EMAIL_CHAIN_MAP
from email_automation.config.constants import REGISTRATION_HISTORY_FILE
from email_automation.services.email_service import EmailService
from email_automation.utils.registration_tracker import RegistrationTracker
from email_automation.utils.date_helper import days_since


# ── Registration history tests ────────────────────────────────────────────────

class TestRegistrationHistory:

    def test_history_file_exists(self):
        assert os.path.exists(REGISTRATION_HISTORY_FILE), (
            f"registration_history.json not found at {REGISTRATION_HISTORY_FILE}"
        )

    def test_history_file_is_valid_json(self):
        with open(REGISTRATION_HISTORY_FILE, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        assert "registrations" in data

    def test_history_contains_at_least_one_record(self, registration_tracker):
        records = registration_tracker.load_history()
        assert len(records) >= 1, "At least one registration must be present."

    def test_active_registration_has_required_fields(self, active_registration):
        assert active_registration.email
        assert active_registration.first_name
        assert active_registration.registration_time
        assert active_registration.status in ("active", "completed")

    def test_registration_email_format_is_correct(self, active_registration):
        """Registered email must match mochaautotest+TIMESTAMP@gmail.com pattern."""
        import re
        pattern = r"^mochaautotest\+\d{8}_\d{6}@gmail\.com$"
        assert re.match(pattern, active_registration.email), (
            f"Email '{active_registration.email}' doesn't match expected pattern."
        )

    def test_tracker_marks_email_validated(self, registration_tracker, active_registration):
        """mark_email_validated must persist to JSON without corrupting records."""
        initial_validated = list(active_registration.emails_validated)
        # Use a dummy email_id that won't overlap with real ones
        test_id = "__test_marker__"
        registration_tracker.mark_email_validated(
            active_registration.email, test_id, "passed"
        )
        updated = registration_tracker.get_active_registration()
        assert test_id in updated.emails_validated
        # Clean up
        records = registration_tracker.load_history()
        for rec in records:
            if rec.email == active_registration.email:
                rec.emails_validated = initial_validated
        registration_tracker.save_history(records)

    def test_needs_registration_false_when_active(self, registration_tracker):
        assert not registration_tracker.needs_registration()


# ── Full email chain validation ───────────────────────────────────────────────

class TestEmailChainValidation:
    """
    Validates all emails due today using EmailService.
    Emails for future days are automatically skipped by the scheduler.
    """

    def test_todays_validation_runs_without_exception(self, email_service):
        """EmailService must return results list (even if empty) without crashing."""
        results = email_service.validate_todays_emails(retries=2, retry_delay=5)
        assert isinstance(results, list)

    def test_all_due_emails_return_results(
        self, email_service, schedule_plan
    ):
        expected_count = len(schedule_plan.emails_to_validate)
        results = email_service.validate_todays_emails(retries=2, retry_delay=5)
        assert len(results) == expected_count, (
            f"Expected {expected_count} result(s), got {len(results)}"
        )

    def test_email_1_arrives_after_registration(
        self, gmail_helper, registration_data
    ):
        """Email 1 (OTP) must be findable in Gmail after registration."""
        email_def = EMAIL_CHAIN_MAP["email_1"]
        email_data = gmail_helper.find_email_by_subject(
            subject_fragment=email_def.subject_search_fragment,
            after_date=registration_data.get("registration_date_gmail"),
        )
        assert email_data is not None, (
            "Email 1 (OTP email) was not found in Gmail inbox after registration."
        )

    def test_email_2_arrives_after_verification(
        self, gmail_helper, registration_data
    ):
        """Email 2 (Welcome) must be findable in Gmail after registration."""
        email_def = EMAIL_CHAIN_MAP["email_2"]
        email_data = gmail_helper.find_email_by_subject(
            subject_fragment=email_def.subject_search_fragment,
            after_date=registration_data.get("registration_date_gmail"),
        )
        assert email_data is not None, (
            "Email 2 (Welcome email) was not found in Gmail inbox after registration."
        )

    @pytest.mark.parametrize("email_id,day_offset", [
        ("email_3",   2),
        ("email_3_1", 4),
        ("email_4",   6),
        ("email_4_1", 8),
        ("email_5",   10),
        ("email_5_1", 12),
        ("email_6",   14),
        ("email_7",   16),
        ("email_7_1", 18),
    ])
    def test_scheduled_email_arrives_when_due(
        self,
        gmail_helper,
        registration_data,
        days_since_registration,
        email_id,
        day_offset,
    ):
        if day_offset > days_since_registration:
            pytest.skip(
                f"{email_id} expected on Day {day_offset}; "
                f"currently Day {days_since_registration}."
            )
        email_def = EMAIL_CHAIN_MAP[email_id]
        email_data = gmail_helper.find_email_by_subject(
            subject_fragment=email_def.subject_search_fragment,
            after_date=registration_data.get("registration_date_gmail"),
        )
        assert email_data is not None, (
            f"{email_id} expected by Day {day_offset} but not found in Gmail."
        )

    def test_missing_email_does_not_crash_suite(self, email_service):
        """
        Requesting validation of a non-existent email_id must return None
        gracefully, not raise an exception.
        """
        result = email_service.validate_single_email(
            "nonexistent_email_id", retries=1, retry_delay=1
        )
        assert result is None

    def test_sender_is_mocha_noreply_for_all_received_emails(
        self, gmail_helper, registration_data, days_since_registration
    ):
        """All emails from Mocha must have noreply@mochaaccounting.com as sender."""
        from email_automation.config.constants import SENDER_EMAIL
        emails = gmail_helper.get_recent_emails_from_sender(
            after_date=registration_data.get("registration_date_gmail"),
            max_results=20,
        )
        for em in emails:
            assert SENDER_EMAIL.lower() in em.sender.lower(), (
                f"Unexpected sender '{em.sender}' for subject '{em.subject}'"
            )

    def test_duplicate_email_detection(
        self, gmail_helper, registration_data, days_since_registration
    ):
        """
        No two emails with the same subject fragment should exist
        for the same registration (prevents duplicate sends).
        """
        from email_automation.config.constants import SENDER_EMAIL
        emails = gmail_helper.get_recent_emails_from_sender(
            after_date=registration_data.get("registration_date_gmail"),
            max_results=30,
        )
        subject_counts: dict = {}
        for em in emails:
            key = em.subject.strip().lower()
            subject_counts[key] = subject_counts.get(key, 0) + 1

        duplicates = {k: v for k, v in subject_counts.items() if v > 1}
        assert not duplicates, (
            f"Duplicate emails detected (same subject sent more than once): {duplicates}"
        )

    def test_report_dir_exists_after_run(self):
        from email_automation.config.constants import REPORT_DIR
        assert os.path.isdir(REPORT_DIR), f"Report directory missing: {REPORT_DIR}"

    def test_log_dir_exists(self):
        from email_automation.config.constants import LOG_DIR
        assert os.path.isdir(LOG_DIR), f"Log directory missing: {LOG_DIR}"
