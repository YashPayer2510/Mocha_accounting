"""Date / time utilities for the email automation suite."""
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional

logger = logging.getLogger(__name__)


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def days_since(iso_timestamp: str) -> int:
    """Return whole days elapsed since an ISO-8601 UTC timestamp."""
    try:
        reg_time = datetime.fromisoformat(iso_timestamp)
        if reg_time.tzinfo is None:
            reg_time = reg_time.replace(tzinfo=timezone.utc)
        delta = utcnow() - reg_time
        return max(0, delta.days)
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
