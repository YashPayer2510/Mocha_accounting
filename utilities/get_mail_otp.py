import base64
import os
import re
import logging
import json
import time

from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_PATH = os.path.join(BASE_DIR, "token.json")
CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials.json")
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly", "https://www.googleapis.com/auth/gmail.modify"]

def get_gmail_service():
    creds = None

    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    # Refresh or create new token if needed
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open(TOKEN_PATH, "w") as token_file:
                token_file.write(creds.to_json())
        else:
            from google_auth_oauthlib.flow import InstalledAppFlow
            if not os.path.exists(CREDENTIALS_PATH):
                raise Exception("Missing credentials.json. Please add it to regenerate token.")

            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)

            with open(TOKEN_PATH, "w") as token_file:
                token_file.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def extract_email_body(payload):
    """Recursively extract email body from payload (html or plain)."""
    if "parts" in payload:
        for part in payload["parts"]:
            body = extract_email_body(part)
            if body:
                return body
    else:
        mime_type = payload.get("mimeType", "")
        data = payload.get("body", {}).get("data")
        if data and mime_type in ["text/plain", "text/html"]:
            return base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")
    return ""

def try_fetch_otp_once(service):
    """Fetch OTP once — used internally by retry wrapper."""
    results = service.users().messages().list(
        userId="me", maxResults=5, q="is:unread"
    ).execute()

    messages = results.get("messages", [])
    if not messages:
        logging.warning("No new unread emails found.")
        return None

    for msg in messages:
        msg_data = service.users().messages().get(userId="me", id=msg["id"], format="full").execute()

        payload = msg_data.get("payload", {})
        email_body = extract_email_body(payload)

        if not email_body:
            logging.warning("No body found, skipping this email.")
            continue

        soup = BeautifulSoup(email_body, "html.parser")
        text = soup.get_text()
        logging.debug(f"Email text snippet: {text[:200]}...")  # safer logging

        otp_match = re.search(r"\b\d{6}\b", text)
        if otp_match:
            otp = otp_match.group(0)
            logging.info(f" Extracted OTP: {otp}")

            # Mark email as read
            service.users().messages().modify(
                userId="me", id=msg["id"], body={"removeLabelIds": ["UNREAD"]}
            ).execute()

            return otp

    return None


def get_latest_otp_email(retries=5, delay=50):
    """
    Fetch the latest unread email and extract a 6-digit OTP from the email body.
    Retries up to 5 times, waiting 10 seconds between attempts.
    """
    try:
        service = get_gmail_service()
        logging.info(f"Fetching OTP with up to {retries} retries (every {delay}s)...")

        for attempt in range(1, retries + 1):
            otp = try_fetch_otp_once(service)
            if otp:
                return otp

            logging.warning(f"Attempt {attempt}/{retries} failed: OTP not found yet. Retrying in {delay}s...")
            time.sleep(delay)

        raise Exception(f"❌ OTP not found after {retries} attempts.")

    except Exception as e:
        logging.error(f"Failed to fetch OTP: {e}")
        raise
