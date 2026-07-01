"""
Email schedule helpers – determines which emails to validate
on a given day relative to the registration date.
"""
from typing import Dict, List

from email_automation.config.email_chain import EMAIL_CHAIN, EmailDefinition


def get_emails_for_day(days_since_registration: int) -> List[EmailDefinition]:
    """Return emails whose day_offset equals the given day."""
    return [e for e in EMAIL_CHAIN if e.day_offset == days_since_registration]


def get_emails_up_to_day(days_since_registration: int) -> List[EmailDefinition]:
    """Return all emails expected from Day 0 through the given day (inclusive)."""
    return [e for e in EMAIL_CHAIN if e.day_offset <= days_since_registration]


def get_immediate_emails() -> List[EmailDefinition]:
    """Return emails that arrive immediately (Day 0, is_immediate=True)."""
    return [e for e in EMAIL_CHAIN if e.is_immediate]


def get_schedule_summary() -> Dict[int, List[str]]:
    """Human-readable map of day → list of email names."""
    summary: Dict[int, List[str]] = {}
    for email_def in EMAIL_CHAIN:
        day = email_def.day_offset
        summary.setdefault(day, []).append(f"{email_def.email_id}: {email_def.name}")
    return summary


def get_total_journey_days() -> int:
    """Number of days spanned by the entire email journey."""
    return max(e.day_offset for e in EMAIL_CHAIN)
