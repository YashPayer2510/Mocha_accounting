"""
HTML → plain-text → normalisation utilities.

The goal is content-level comparison that ignores formatting, icons,
whitespace, and HTML artefacts so that validators can focus on meaning.
"""
import re
import unicodedata
from typing import List, Dict

from bs4 import BeautifulSoup


class TextNormalizer:
    """Converts and normalises email body content for comparison."""

    # HTML entities that BeautifulSoup may not decode automatically
    _ENTITY_MAP = {
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
        "&nbsp;": " ",
        "&mdash;": "—",
        "&ndash;": "–",
        "&rsquo;": "'",
        "&lsquo;": "'",
        "&rdquo;": '"',
        "&ldquo;": '"',
        "&#39;": "'",
    }

    def html_to_text(self, html: str) -> str:
        """Strip HTML tags and return plain text, preserving word boundaries."""
        soup = BeautifulSoup(html, "html.parser")
        for tag in soup(["script", "style", "meta", "link", "head"]):
            tag.decompose()
        # Replace block-level tags with spaces so words don't merge
        for tag in soup.find_all(["br", "p", "div", "li", "td", "th", "tr"]):
            tag.insert_before(" ")
        return soup.get_text(separator=" ")

    def decode_entities(self, text: str) -> str:
        for entity, char in self._ENTITY_MAP.items():
            text = text.replace(entity, char)
        return text

    def normalize(self, text: str) -> str:
        """
        Full normalisation pipeline:
        decode → NFKD unicode → lowercase → collapse whitespace.
        """
        text = self.decode_entities(text)
        text = unicodedata.normalize("NFKD", text)
        text = text.lower()
        # Collapse any whitespace sequence (spaces, tabs, newlines) to a single space
        text = re.sub(r"[\s​ ]+", " ", text)
        text = text.strip()
        return text

    def normalize_html(self, html: str) -> str:
        """Full pipeline: html_to_text → normalize."""
        return self.normalize(self.html_to_text(html))

    def normalize_subject(self, subject: str) -> str:
        """Normalise a subject line (decode entities + collapse whitespace; keep case)."""
        subject = self.decode_entities(subject)
        subject = re.sub(r"\s+", " ", subject).strip()
        return subject

    def keywords_present(
        self, body: str, keywords: List[str], *, is_html: bool = True
    ) -> Dict[str, bool]:
        """
        Check whether each keyword exists in the normalised body.
        Returns a dict of keyword → found.
        """
        normalized_body = self.normalize_html(body) if is_html else self.normalize(body)
        return {kw: self.normalize(kw) in normalized_body for kw in keywords}

    def contains_six_digit_otp(self, text: str) -> bool:
        """Return True if text contains a 6-digit number (OTP)."""
        return bool(re.search(r"\b\d{6}\b", text))

    def extract_otp(self, text: str) -> str | None:
        """Extract the first 6-digit number from text, or None."""
        match = re.search(r"\b(\d{6})\b", text)
        return match.group(1) if match else None
