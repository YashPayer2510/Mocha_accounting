"""
Gmail helper – thin wrapper around the existing Gmail utilities.

Imports get_gmail_service() from utilities.get_mail_otp (existing file,
NOT modified) and adds richer search / body-extraction capabilities
needed for onboarding email validation.
"""
import base64
import logging
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Optional

from email_automation.config.constants import (
    SENDER_EMAIL,
    GMAIL_QUERY_SENDER,
    EMAIL_RETRY_COUNT,
    EMAIL_RETRY_DELAY_SECONDS,
)

# ── Reuse existing auth (do NOT modify that file) ─────────────────────────────
from utilities.get_mail_otp import get_gmail_service  # noqa: E402

logger = logging.getLogger(__name__)


@dataclass
class EmailData:
    """Structured representation of a single Gmail message."""
    message_id: str
    thread_id: str
    subject: str
    sender: str
    recipient: str           # value of the 'To' header
    delivered_to: str        # value of 'Delivered-To' header (plus-addressed)
    received_time: datetime
    body_plain: str
    body_html: str
    snippet: str
    label_ids: List[str] = field(default_factory=list)

    @property
    def is_unread(self) -> bool:
        return "UNREAD" in self.label_ids


class GmailHelper:
    """
    Provides email search, retrieval, and filtering for the
    Mocha Accounting email automation suite.
    """

    def __init__(self) -> None:
        self._service = get_gmail_service()

    # ── Public API ────────────────────────────────────────────────────────────

    def find_email_by_subject(
        self,
        subject_fragment: str,
        after_date: Optional[str] = None,   # "YYYY/MM/DD"
        before_date: Optional[str] = None,  # "YYYY/MM/DD"
        recipient: Optional[str] = None,
        max_results: int = 50,
    ) -> Optional[EmailData]:
        """
        Search Gmail for the most recent email matching subject_fragment.

        Args:
            subject_fragment: Distinctive phrase from the expected subject.
            after_date:        Gmail 'after:' filter, format 'YYYY/MM/DD'.
            before_date:       Gmail 'before:' filter, format 'YYYY/MM/DD'.
                               Use with after_date to narrow search to exactly
                               the one day the email is expected to arrive.
            recipient:         Expected To address (checked in headers, not
                               via Gmail query to handle plus-addressing).
            max_results:       How many candidate messages to fetch.
        """
        query = self._build_query(
            subject_fragment=subject_fragment,
            after_date=after_date,
            before_date=before_date,
        )
        logger.debug("Gmail query: %s", query)

        try:
            results = self._service.users().messages().list(
                userId="me",
                maxResults=max_results,
                q=query,
            ).execute()
        except Exception as exc:
            logger.error("Gmail API list error: %s", exc)
            return None

        messages = results.get("messages", [])
        if not messages:
            logger.warning("No messages found for query: %s", query)
            return None

        for msg in messages:
            email_data = self._fetch_email_data(msg["id"])
            if email_data is None:
                continue
            # Optional recipient filter (header-level check, handles plus-addressing)
            if recipient and not self._recipient_matches(email_data, recipient):
                continue
            return email_data

        return None

    def wait_for_email(
        self,
        subject_fragment: str,
        after_date: Optional[str] = None,
        recipient: Optional[str] = None,
        retries: int = EMAIL_RETRY_COUNT,
        delay: int = EMAIL_RETRY_DELAY_SECONDS,
    ) -> Optional[EmailData]:
        """
        Poll Gmail until the expected email arrives or retries are exhausted.
        """
        logger.info(
            "Waiting for email with subject fragment '%s' (max %d retries, %ds apart)",
            subject_fragment, retries, delay,
        )
        for attempt in range(1, retries + 1):
            email_data = self.find_email_by_subject(
                subject_fragment=subject_fragment,
                after_date=after_date,
                recipient=recipient,
            )
            if email_data:
                logger.info("Email found on attempt %d/%d", attempt, retries)
                return email_data
            if attempt < retries:
                logger.warning(
                    "Attempt %d/%d: email not found yet. Retrying in %ds…",
                    attempt, retries, delay,
                )
                time.sleep(delay)
        logger.error(
            "Email with subject fragment '%s' not received after %d attempts.",
            subject_fragment, retries,
        )
        return None

    def get_recent_emails_from_sender(
        self,
        after_date: Optional[str] = None,
        max_results: int = 20,
    ) -> List[EmailData]:
        """Fetch recent emails from the Mocha sender for bulk inspection."""
        query = GMAIL_QUERY_SENDER
        if after_date:
            query += f" after:{after_date}"
        try:
            results = self._service.users().messages().list(
                userId="me", maxResults=max_results, q=query
            ).execute()
        except Exception as exc:
            logger.error("Gmail API list error: %s", exc)
            return []
        emails = []
        for msg in results.get("messages", []):
            data = self._fetch_email_data(msg["id"])
            if data:
                emails.append(data)
        return emails

    def mark_as_read(self, message_id: str) -> None:
        try:
            self._service.users().messages().modify(
                userId="me",
                id=message_id,
                body={"removeLabelIds": ["UNREAD"]},
            ).execute()
        except Exception as exc:
            logger.warning("Could not mark message %s as read: %s", message_id, exc)

    # ── Private helpers ───────────────────────────────────────────────────────

    def _build_query(
        self,
        subject_fragment: str,
        after_date: Optional[str],
        before_date: Optional[str] = None,
    ) -> str:
        parts = [GMAIL_QUERY_SENDER, f'subject:"{subject_fragment}"']
        if after_date:
            parts.append(f"after:{after_date}")
        if before_date:
            parts.append(f"before:{before_date}")
        return " ".join(parts)

    def _fetch_email_data(self, message_id: str) -> Optional[EmailData]:
        try:
            msg = self._service.users().messages().get(
                userId="me", id=message_id, format="full"
            ).execute()
        except Exception as exc:
            logger.error("Could not fetch message %s: %s", message_id, exc)
            return None

        payload = msg.get("payload", {})
        headers = {h["name"]: h["value"] for h in payload.get("headers", [])}

        subject = headers.get("Subject", "")
        sender = headers.get("From", "")
        recipient = headers.get("To", "")
        delivered_to = headers.get("Delivered-To", recipient)
        date_header = headers.get("Date", "")

        # internal_date is milliseconds since epoch
        internal_date_ms = int(msg.get("internalDate", 0))
        received_time = datetime.fromtimestamp(
            internal_date_ms / 1000, tz=timezone.utc
        )

        body_plain, body_html = self._extract_bodies(payload)

        return EmailData(
            message_id=message_id,
            thread_id=msg.get("threadId", ""),
            subject=subject,
            sender=sender,
            recipient=recipient,
            delivered_to=delivered_to,
            received_time=received_time,
            body_plain=body_plain,
            body_html=body_html,
            snippet=msg.get("snippet", ""),
            label_ids=msg.get("labelIds", []),
        )

    def _extract_bodies(self, payload: dict) -> tuple[str, str]:
        """Recursively extract text/plain and text/html from MIME parts."""
        plain_parts: List[str] = []
        html_parts: List[str] = []
        self._collect_bodies(payload, plain_parts, html_parts)
        return " ".join(plain_parts), " ".join(html_parts)

    def _collect_bodies(
        self,
        part: dict,
        plain_acc: List[str],
        html_acc: List[str],
    ) -> None:
        mime = part.get("mimeType", "")
        data = part.get("body", {}).get("data")
        if data:
            decoded = base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
            if mime == "text/plain":
                plain_acc.append(decoded)
            elif mime == "text/html":
                html_acc.append(decoded)
        for sub in part.get("parts", []):
            self._collect_bodies(sub, plain_acc, html_acc)

    @staticmethod
    def _recipient_matches(email_data: EmailData, expected: str) -> bool:
        """
        Check that the expected address appears in To or Delivered-To headers.
        Handles plus-addressing and case differences.
        """
        expected_lower = expected.lower()
        for field_val in (email_data.recipient, email_data.delivered_to):
            if expected_lower in field_val.lower():
                return True
        return False
