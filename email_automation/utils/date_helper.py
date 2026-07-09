"""Date / time utilities for the email automation suite."""
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional

logger = logging.getLogger(__name__)


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def days_since(iso_timestamp: str) -> int:
    """Return calendar days elapsed since an ISO-8601 UTC timestamp.

    Uses date subtraction (not hours/24) so that a registration on Jul 2
    at 11:24 UTC shows day_offset=2 on Jul 4 at 04:00 UTC, matching the
    email schedule which counts calendar days, not 24-hour periods.
    """
    try:
        reg_time = datetime.fromisoformat(iso_timestamp)
        if reg_time.tzinfo is None:
            reg_time = reg_time.replace(tzinfo=timezone.utc)
        return max(0, (utcnow().date() - reg_time.date()).days)
    except Exception as exc:
        logger.error("Could not parse timestamp '%s': %s", iso_timestamp, exc)
        return 0


def to_gmail_date_str(dt: Optional[datetime] = None) -> str:
    """Format a datetime as 'YYYY/MM/DD' for Gmail API `after:` queries."""
    if dt is None:
        dt = utcnow()
    return dt.strftime("%Y/%m/%d")


def iso_now() -> str:
    """Current UTC time as ISO-8601 string."""
    return utcnow().isoformat()


def iso_date_today() -> str:
    """Today's UTC date as 'YYYY-MM-DD'."""
    return utcnow().strftime("%Y-%m-%d")


def email_expected_on_day(day_offset: int, registration_iso: str) -> datetime:
    """Return the UTC datetime when a day-offset email is expected."""
    reg_time = datetime.fromisoformat(registration_iso)
    if reg_time.tzinfo is None:
        reg_time = reg_time.replace(tzinfo=timezone.utc)
    return reg_time + timedelta(days=day_offset)
