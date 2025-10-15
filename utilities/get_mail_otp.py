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
    # Load token.json if exists
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    # Refresh or create a new token if needed
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open(TOKEN_PATH, "w") as token_file:
                token_file.write(creds.to_json())
        else:
            raise Exception("Token not found. Run gmail_auth_setup.py first.")

    return build("gmail", "v1", credentials=creds)

def get_latest_otp_email():
    """
    Fetch the latest unread email and extract a 6-digit OTP from the email body (not snippet).
    """
    try:
        time.sleep(5)
        service = get_gmail_service()
        logging.info("Fetching latest unread emails...")

        results = service.users().messages().list(
            userId="me", maxResults=5, q="is:unread"
        ).execute()

        messages = results.get("messages", [])
        if not messages:
            logging.error("No new OTP emails found.")
            raise Exception("No new OTP emails found")

        for msg in messages:
            msg_data = service.users().messages().get(userId="me", id=msg["id"], format="full").execute()

            # Extract the payload parts (body is base64 encoded)
            payload = msg_data["payload"]
            parts = payload.get("parts", [])
            email_body = ""

            for part in parts:
                if part["mimeType"] == "text/html":
                    data = part["body"]["data"]
                    email_body = base64.urlsafe_b64decode(data).decode("utf-8")
                    break

            if not email_body:
                logging.warning("No HTML body found, skipping this email.")
                continue

            # Parse HTML with BeautifulSoup
            soup = BeautifulSoup(email_body, "html.parser")
            text = soup.get_text()
            logging.info(f"Extracted email text: {text}")

            # Find the first 6-digit code in the body text
            otp_match = re.search(r"\b\d{6}\b", text)
            if otp_match:
                otp = otp_match.group(0)
                logging.info(f"✅ Extracted OTP: {otp}")

                # Mark email as read so next run fetches new one
                service.users().messages().modify(
                    userId="me", id=msg["id"], body={"removeLabelIds": ["UNREAD"]}
                ).execute()

                return otp

        raise Exception("OTP not found in latest emails")

    except Exception as e:
        logging.error(f"Failed to fetch OTP: {e}")
        raise