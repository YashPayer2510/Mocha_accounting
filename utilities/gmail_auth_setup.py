# utilities/gmail_auth_setup.py
import os
import logging
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Define Gmail scopes
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.modify"
]

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials.json")
TOKEN_PATH = os.path.join(BASE_DIR, "token.json")

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def get_or_create_gmail_token():
    """Generates or refreshes Gmail OAuth token automatically."""
    creds = None

    # ✅ Step 1: Load existing token if present
    if os.path.exists(TOKEN_PATH):
        logging.info("🔄 Loading existing token.json")
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    # ✅ Step 2: Refresh if expired, or create new one if missing
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            logging.info("♻️ Refreshing expired token...")
            creds.refresh(Request())
        else:
            logging.info("🌐 No valid token found — running new OAuth flow...")
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)

        # ✅ Step 3: Save token for reuse
        with open(TOKEN_PATH, "w") as token_file:
            token_file.write(creds.to_json())
            logging.info(f"✅ Token saved to: {TOKEN_PATH}")

    return creds


if __name__ == "__main__":
    creds = get_or_create_gmail_token()
    logging.info("✅ Gmail authentication setup completed successfully.")
