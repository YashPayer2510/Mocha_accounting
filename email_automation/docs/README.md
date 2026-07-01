# Mocha Accounting – Email Automation Validation Suite

Automated framework that validates the complete 11-email onboarding journey
sent by Mocha Accounting. Runs daily via GitHub Actions, persists state
across runs, and emails an HTML report to the team.

---

## Project Structure

```
email_automation/
├── config/
│   ├── constants.py          # All constants, paths, retry settings
│   ├── email_chain.py        # EmailDefinition objects – subjects, keywords, day offsets
│   └── email_schedule.py     # Helper functions: get_emails_for_day(), etc.
├── validators/
│   ├── email_validator.py    # Orchestrates subject + body + recipient validation
│   ├── subject_validator.py  # Subject comparison with placeholder / OTP support
│   ├── body_validator.py     # Keyword presence checks on normalised body text
│   └── recipient_validator.py# To / Delivered-To header validation
├── utils/
│   ├── date_helper.py        # UTC dates, days_since(), Gmail date format
│   ├── gmail_helper.py       # Gmail API wrapper (imports existing get_gmail_service)
│   ├── text_normalizer.py    # HTML → plain text → lowercase / whitespace collapse
│   ├── registration_tracker.py # Reads/writes registration_history.json
│   └── enhanced_registration.py # Registration subclass that captures generated values
├── services/
│   ├── email_service.py      # High-level: validate_todays_emails()
│   └── scheduler.py          # Determines: register now OR validate today's emails
├── fixtures/
│   └── conftest.py           # All shared pytest fixtures
├── tests/
│   ├── conftest.py           # Loads fixtures via pytest_plugins
│   ├── test_registration_runner.py  # Browser test – performs daily registration
│   ├── test_email_chain.py          # E2E chain + history tests
│   ├── test_email_subject.py        # Subject validation (unit + live)
│   ├── test_email_content.py        # Body keyword validation (unit + live)
│   ├── test_email_recipient.py      # Recipient validation (unit + live)
│   └── test_email_schedule.py       # Scheduling logic (unit + integration)
├── storage/
│   └── registration_history.json   # Persisted across GitHub Action runs
├── logs/                     # Auto-created; one log file per run
├── reports/                  # HTML pytest reports; one per run
├── github/
│   └── daily_email_chain.yml # New GitHub Action (does NOT replace existing ones)
├── conftest.py               # sys.path bootstrap (project root → Python path)
└── docs/
    └── README.md             # This file
```

---

## Email Journey

| Email ID   | Name                        | Day | Subject |
|------------|-----------------------------|-----|---------|
| email_1    | OTP Verification            | 0   | Hi {first_name} , your signup code is {otp} |
| email_2    | Welcome / Account Active    | 0   | Hi {first_name} , Welcome to Mocha! Here are your account details |
| email_3    | Invite to Demo              | 2   | Start strong with a personalized Mocha walkthrough! |
| email_3_1  | Demo Reminder 1             | 4   | Still Curious About Mocha Accounting? Let's Connect! |
| email_4    | Accounting Feature Highlight| 6   | Simplify Your Finances with Mocha Accounting |
| email_4_1  | Demo Reminder 2             | 8   | Don't Miss Out: Your Accounting Game-Changer Awaits |
| email_5    | Invoicing Feature Highlight | 10  | Master Your Invoicing with Mocha Accounting |
| email_5_1  | Demo Reminder 3             | 12  | We're Here to Help - Free Demo Invitation Still Open |
| email_6    | Inventory Feature Highlight | 14  | Take Control of Your Inventory with Mocha Accounting |
| email_7    | Case Study                  | 16  | How a Hotel Business Saved 80 Hours Monthly with Mocha Accounting |
| email_7_1  | Final Demo CTA              | 18  | Last Chance - Your Free Mocha Accounting Demo Ends Soon |

---

## Prerequisites

### Python dependencies
```bash
pip install pytest pytest-html webdriver-manager selenium python-dotenv \
            beautifulsoup4 lxml \
            google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### Environment variables (`.env` file)
```
URL=https://app.mochaaccounting.com
REGISTRATION_URL=https://app.mochaaccounting.com
BROWSER=chrome
VALIDLOGINUSERNAME=your@email.com
VALIDLOGINPASSWORD=yourpassword
```

### Gmail credentials
Place `token.json` and `credentials.json` in the `utilities/` directory.
These are the same files used by the existing `get_mail_otp.py` utility.

### GitHub Secrets required
| Secret | Purpose |
|--------|---------|
| `GMAIL_TOKEN` | Gmail OAuth token JSON |
| `GMAIL_CREDENTIALS` | Gmail OAuth credentials JSON |
| `EMAIL_USER` | SMTP sender email |
| `EMAIL_PASS` | SMTP password / app password |
| `GH_PAT` | GitHub personal access token (for git push) |

---

## Running Locally

### Step 1 – Register a new user (needs browser / display)
```bash
# On Linux with Xvfb:
xvfb-run pytest email_automation/tests/test_registration_runner.py -v

# On Windows:
pytest email_automation/tests/test_registration_runner.py -v
```
The test is automatically **skipped** if an active registration already exists.

### Step 2 – Validate today's emails (no browser needed)
```bash
pytest email_automation/tests/ \
  --ignore=email_automation/tests/test_registration_runner.py \
  -v \
  --html=email_automation/reports/report.html \
  --self-contained-html
```

### Step 3 – Run only scheduling / unit tests (no Gmail required)
```bash
pytest email_automation/tests/test_email_schedule.py \
       email_automation/tests/test_email_subject.py::TestSubjectValidatorUnit \
       email_automation/tests/test_email_content.py::TestBodyValidatorUnit \
       email_automation/tests/test_email_recipient.py::TestRecipientValidatorUnit \
       -v
```

---

## How Scheduling Works

On each daily GitHub Action run the `Scheduler` checks `registration_history.json`:

```
Run starts
    │
    ▼
Active registration?  ──No──▶  Run registration test  ──▶  Save email + first_name to history
    │
   Yes
    │
    ▼
days_since(registration_time) = N
    │
    ▼
get_emails_for_day(N)   ──▶  [email_1, email_2] on Day 0
                              [email_3]           on Day 2
                              ...
    │
    ▼
Validate each email  ──▶  Update history  ──▶  Generate report  ──▶  Send email
```

Emails for **future days** are **never** requested – the test is simply skipped.  
This means the GitHub Action can run safely every day for 18 days with
zero manual intervention.

---

## Validation Logic

For every email the framework checks:

1. **Recipient** – `To` or `Delivered-To` header contains the registered email address.
2. **Sender** – From address must be `noreply@mochaaccounting.com`.
3. **Subject** – After placeholder resolution:
   - `{first_name}` → actual first name from registration
   - `{otp}` → regex pattern `\d{6}` (6-digit number)
   - Static subjects → exact normalised comparison
4. **Body** – Required keywords must be present in the normalised plain text:
   - HTML stripped, entities decoded, whitespace collapsed, lowercased
   - Each keyword independently checked (missing ones reported)
   - Email 1 additionally checks for a 6-digit OTP in the body

### What is intentionally NOT validated
- HTML formatting, fonts, colours, images
- Icon characters
- Alignment / spacing
- Bullet styles

---

## Failure Handling

- Each email is validated independently; a failure does not stop other validations.
- If an email is not found, `wait_for_email()` retries up to `EMAIL_RETRY_COUNT` times
  (default 5) with `EMAIL_RETRY_DELAY_SECONDS` (default 30s) between attempts.
- All failures are recorded in `registration_history.json` and reported in the HTML report.
- The GitHub Action uses `continue-on-error: true` so the report email is always sent.

---

## Adding / Updating Email Definitions

Edit `email_automation/config/email_chain.py`:

```python
EmailDefinition(
    email_id="email_3",
    subject_template="Start strong with a personalized Mocha walkthrough!",
    subject_search_fragment="Start strong with a personalized Mocha walkthrough",
    required_keywords=[
        "personalized walkthrough",
        "reduce accounting errors by up to 75%",
        ...
    ],
    day_offset=2,
    ...
)
```

No other files need changes for subject or keyword updates.

---

## Existing Files – NOT Modified

This suite reuses but does NOT modify:

| File | Used for |
|------|---------|
| `pages/registration.py` | Base class for `EnhancedRegistration` |
| `utilities/get_mail_otp.py` | `get_gmail_service()` and `get_latest_otp_email()` |
| `utilities/gmail_auth_setup.py` | OAuth token management |
| `tests/test_signup_login/test_sign_up.py` | Reference only |
| `.github/workflows/daily_login_cron.yml` | Structure reference for new workflow |
