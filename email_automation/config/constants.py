"""Central constants for the Mocha Accounting email automation suite."""
import os

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # email_automation/
PROJECT_ROOT = os.path.dirname(BASE_DIR)

LOG_DIR = os.path.join(BASE_DIR, "logs")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
STORAGE_DIR = os.path.join(BASE_DIR, "storage")
REGISTRATION_HISTORY_FILE = os.path.join(STORAGE_DIR, "registration_history.json")

# ── Gmail ──────────────────────────────────────────────────────────────────────
SENDER_EMAIL = "noreply@mochaaccounting.com"
SUPPORT_EMAIL = "support@mochatechnologies.com"
GMAIL_QUERY_SENDER = f"from:{SENDER_EMAIL}"

# ── Retry / Timeout ────────────────────────────────────────────────────────────
EMAIL_RETRY_COUNT = 5
EMAIL_RETRY_DELAY_SECONDS = 30   # wait between retry attempts
EMAIL_TIMEOUT_SECONDS = 300      # 5 min total max wait for immediate emails
DAY2_EMAIL_WAIT_SECONDS = 60     # short wait for Day-2+ emails (should already be present)

# ── Subject Placeholders ───────────────────────────────────────────────────────
PLACEHOLDER_FIRST_NAME = "{first_name}"
PLACEHOLDER_OTP = "{otp}"
PLACEHOLDER_EMAIL = "{email}"
PLACEHOLDER_DEMO_LINK = "{demo_link}"
PLACEHOLDER_DATE = "{date}"
PLACEHOLDER_COMPANY_NAME = "{company_name}"
PLACEHOLDER_PLAN_NAME = "{plan_name}"
PLACEHOLDER_FULL_NAME = "{full_name}"

# ── Email journey day offsets (days since registration) ───────────────────────
EMAIL_DAY_OFFSETS: dict[str, int] = {
    "email_1":   0,   # immediately after signup
    "email_2":   0,   # immediately after email verification
    "email_3":   2,
    "email_3_1": 4,
    "email_4":   6,
    "email_4_1": 8,
    "email_5":   10,
    "email_5_1": 12,
    "email_6":   14,
    "email_7":   16,
    "email_7_1": 18,
}

TOTAL_JOURNEY_DAYS = 18
REGISTRATION_ACTIVE_DAYS = TOTAL_JOURNEY_DAYS + 2  # keep history for 20 days

# ── Registration ───────────────────────────────────────────────────────────────
REGISTRATION_EMAIL_BASE = "mochaautotest"
REGISTRATION_EMAIL_DOMAIN = "gmail.com"

# ── Environments ──────────────────────────────────────────────────────────────
ENVIRONMENTS: dict[str, str] = {
    "staging":    "https://staging.mochaaccounting.com",
    "qa":         "https://qa.mochaaccounting.com",
    "production": "https://app.mochaaccounting.com",
}
DEFAULT_ENV = "production"

# ── Reporting ─────────────────────────────────────────────────────────────────
REPORT_EMAIL_SUBJECT = "Daily Email Automation Report – Mocha Accounting"
REPORT_EMAIL_TO = "yash.payer@mochatechnologies.com"

# ── Logging ────────────────────────────────────────────────────────────────────
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s — %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Create dirs on import so downstream code can assume they exist
for _d in (LOG_DIR, REPORT_DIR, STORAGE_DIR):
    os.makedirs(_d, exist_ok=True)
