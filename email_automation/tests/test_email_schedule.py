"""
Tests for the scheduling logic.
Verifies that the Scheduler selects the correct emails for each day
relative to the registration date, without requiring live Gmail access.
"""
import pytest

from email_automation.config.email_chain import EMAIL_CHAIN
from email_automation.config.email_schedule import (
    get_emails_for_day,
    get_emails_up_to_day,
    get_immediate_emails,
    get_schedule_summary,
    get_total_journey_days,
)
from email_automation.config.constants import EMAIL_DAY_OFFSETS


# ── Schedule definition tests ─────────────────────────────────────────────────

class TestEmailScheduleDefinition:

    def test_total_journey_is_18_days(self):
        assert get_total_journey_days() == 18

    def test_email_chain_has_eleven_emails(self):
        assert len(EMAIL_CHAIN) == 11

    @pytest.mark.parametrize("day,expected_ids", [
        (0,  ["email_1", "email_2"]),
        (2,  ["email_3"]),
        (4,  ["email_3_1"]),
        (6,  ["email_4"]),
        (8,  ["email_4_1"]),
        (10, ["email_5"]),
        (12, ["email_5_1"]),
        (14, ["email_6"]),
        (16, ["email_7"]),
        (18, ["email_7_1"]),
    ])
    def test_correct_emails_for_day(self, day, expected_ids):
        emails = get_emails_for_day(day)
        actual_ids = [e.email_id for e in emails]
        assert sorted(actual_ids) == sorted(expected_ids), (
            f"Day {day}: expected {expected_ids}, got {actual_ids}"
        )

    def test_day_0_contains_two_emails(self):
        emails = get_emails_for_day(0)
        assert len(emails) == 2

    def test_all_other_days_contain_one_email(self):
        days_to_check = [2, 4, 6, 8, 10, 12, 14, 16, 18]
        for day in days_to_check:
            emails = get_emails_for_day(day)
            assert len(emails) == 1, f"Expected 1 email on Day {day}, got {len(emails)}"

    def test_no_emails_on_unexpected_day(self):
        for odd_day in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20]:
            assert get_emails_for_day(odd_day) == [], (
                f"Should be no emails on Day {odd_day}"
            )

    def test_get_emails_up_to_day_accumulates_correctly(self):
        emails_by_day_2 = get_emails_up_to_day(2)
        ids = [e.email_id for e in emails_by_day_2]
        assert "email_1" in ids
        assert "email_2" in ids
        assert "email_3" in ids
        assert "email_3_1" not in ids

    def test_immediate_emails_are_email_1_and_2(self):
        immediate = get_immediate_emails()
        ids = [e.email_id for e in immediate]
        assert "email_1" in ids
        assert "email_2" in ids

    def test_schedule_summary_contains_all_days(self):
        summary = get_schedule_summary()
        expected_days = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
        assert set(summary.keys()) == expected_days

    def test_day_offsets_constant_matches_chain(self):
        """EMAIL_DAY_OFFSETS dict in constants must match actual chain definitions."""
        for email_def in EMAIL_CHAIN:
            expected_offset = EMAIL_DAY_OFFSETS.get(email_def.email_id)
            assert expected_offset is not None, (
                f"{email_def.email_id} missing from EMAIL_DAY_OFFSETS"
            )
            assert email_def.day_offset == expected_offset, (
                f"{email_def.email_id}: chain offset={email_def.day_offset}, "
                f"constants offset={expected_offset}"
            )


# ── Scheduler tests (requires registration history) ───────────────────────────

class TestSchedulerPlan:

    def test_scheduler_plan_has_required_fields(self, schedule_plan):
        assert hasattr(schedule_plan, "needs_registration")
        assert hasattr(schedule_plan, "days_since_registration")
        assert hasattr(schedule_plan, "emails_to_validate")

    def test_scheduler_no_registration_needed_when_active(self, active_registration, schedule_plan):
        """If an active registration exists the scheduler must NOT require a new one."""
        assert not schedule_plan.needs_registration

    def test_scheduler_selects_emails_for_current_day(self, schedule_plan, days_since_registration):
        expected_ids = [
            e.email_id for e in get_emails_for_day(days_since_registration)
        ]
        scheduled_ids = [e.email_id for e in schedule_plan.emails_to_validate]
        # All expected IDs should be present (some may have been validated already)
        for eid in scheduled_ids:
            assert eid in expected_ids, (
                f"{eid} should not be scheduled for Day {days_since_registration}"
            )

    def test_future_emails_not_in_plan(self, schedule_plan, days_since_registration):
        """Emails for future days must not appear in today's plan."""
        for email_def in schedule_plan.emails_to_validate:
            assert email_def.day_offset <= days_since_registration, (
                f"{email_def.email_id} (Day {email_def.day_offset}) "
                f"should not be scheduled on Day {days_since_registration}"
            )

    def test_registration_data_has_required_keys(self, registration_data):
        for key in ("email", "first_name", "last_name", "registration_date_gmail"):
            assert key in registration_data, f"Missing key: {key}"

    def test_days_since_registration_non_negative(self, days_since_registration):
        assert days_since_registration >= 0
