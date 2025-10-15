# utilities/gmail_auth_setup.py
from google_auth_oauthlib.flow import InstalledAppFlow
import json

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly", "https://www.googleapis.com/auth/gmail.modify"]

def generate_token():
    flow = InstalledAppFlow.from_client_secrets_file("utilities/credentials.json", SCOPES)
    creds = flow.run_local_server(port=0)  # Opens browser for login
    with open("utilities/token.json", "w") as token_file:
        token_file.write(creds.to_json())
    print("✅ Token generated and saved to utilities/token.json")

if __name__ == "__main__":
    generate_token()
