"""
Shared pytest fixtures for the email automation suite.
Loaded by email_automation/tests/conftest.py via pytest_plugins.
"""
import json
import logging
import os
import sys
from typing import Any, Dict, Optional

import pytest

# ── Path bootstrap (needed when fixtures module is imported directly) ─────────
_PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from email_automation.config.constants import LOG_DIR, LOG_FORMAT, LOG_DATE_FORMAT
from email_automation.config.email_chain import EMAIL_CHAIN, EMAIL_CHAIN_MAP
from email_automation.services.email_service import EmailService
from email_automation.services.scheduler import Scheduler
from email_automation.utils.gmail_helper import GmailHelper
from email_automation.utils.registration_tracker import RegistrationTracker
from email_automation.utils.text_normalizer import TextNormalizer

# ── Logging setup ─────────────────────────────────────────────────────────────

def _configure_logging(log_filename: str) -> None:
    log_path = os.path.join(LOG_DIR, log_filename)
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(),
        ],
        force=True,
    )


# ── Session-scoped fixtures ───────────────────────────────────────────────────

@pytest.fixture(scope="session", autouse=True)
def configure_email_validation_logging():
    """Set up email_validation.log for the entire test session."""
    _configure_logging("email_validation.log")
    yield


@pytest.fixture(scope="session")
def registration_tracker() -> RegistrationTracker:
    return RegistrationTracker()


@pytest.fixture(scope="session")
def gmail_helper() -> GmailHelper:
    """Initialise GmailHelper once per test session (reuses OAuth token)."""
    return GmailHelper()


@pytest.fixture(scope="session")
def text_normalizer() -> TextNormalizer:
    return TextNormalizer()


@pytest.fixture(scope="session")
def email_service(registration_tracker, gmail_helper) -> EmailService:
    return EmailService(tracker=registration_tracker, gmail=gmail_helper)


@pytest.fixture(scope="session")
def scheduler(registration_tracker) -> Scheduler:
    return Scheduler(tracker=registration_tracker)


@pytest.fixture(scope="session")
def schedule_plan(scheduler):
    """The SchedulePlan computed once for the whole test session."""
    return scheduler.get_plan()


@pytest.fixture(scope="session")
def active_registration(registration_tracker):
    """
    Returns the active RegistrationRecord, or skips all tests in the session
    if no registration has been performed yet.
    """
    rec = registration_tracker.get_active_registration()
    if rec is None:
        pytest.skip(
            "No active registration found. Run test_registration_runner.py first."
        )
    return rec


@pytest.fixture(scope="session")
def registration_data(scheduler, active_registration) -> Dict[str, Any]:
    """Dict passed to EmailValidator with email, first_name, registration_date_gmail."""
    return scheduler.build_registration_data(active_registration)


@pytest.fixture(scope="session")
def days_since_registration(active_registration) -> int:
    from email_automation.utils.date_helper import days_since
    return days_since(active_registration.registration_time)


@pytest.fixture(scope="session")
def email_chain():
    """The full email chain list (EmailDefinition objects)."""
    return EMAIL_CHAIN


@pytest.fixture(scope="session")
def email_chain_map():
    """Dict mapping email_id → EmailDefinition."""
    return EMAIL_CHAIN_MAP


# ── Registration test data (reuses existing data/registration_test_data.json) ─

@pytest.fixture(scope="session")
def registration_test_data() -> Dict[str, Any]:
    data_path = os.path.join(_PROJECT_ROOT, "data", "registration_test_data.json")
    with open(data_path, "r", encoding="utf-8") as fh:
        return json.load(fh)


# ── Browser setup for registration runner (mirrors existing conftest pattern) ─

@pytest.fixture(scope="function")
def email_reg_driver(request):
    """
    WebDriver fixture for the registration runner.
    Mirrors the existing conftest fixture pattern without modifying any
    existing conftest file.
    """
    import time
    from tempfile import mkdtemp
    from dotenv import load_dotenv
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from webdriver_manager.chrome import ChromeDriverManager

    load_dotenv()
    URL = os.getenv("REGISTRATION_URL", os.getenv("URL", ""))
    BROWSER = os.getenv("BROWSER", "chrome").lower()

    _driver = None
    try:
        if BROWSER == "chrome":
            opts = ChromeOptions()
            opts.add_argument("--disable-gpu")
            opts.add_argument("--no-sandbox")
            opts.add_argument("--disable-dev-shm-usage")
            opts.add_argument("--force-device-scale-factor=0.85")
            opts.add_argument("--start-maximized")
            opts.add_argument("--window-size=1920,1080")
            opts.add_argument(f"--user-data-dir={mkdtemp()}")
            opts.add_experimental_option("excludeSwitches", ["enable-logging"])
            opts.set_capability("unhandledPromptBehavior", "accept")
            _driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()), options=opts
            )
        else:
            raise ValueError(f"Unsupported browser for email reg: {BROWSER}")

        _driver.implicitly_wait(3)
        _driver.get(URL)
        logging.info("Navigated to registration URL: %s", URL)
        yield _driver
    except Exception as exc:
        logging.error("Driver setup failed: %s", exc)
        pytest.fail(f"Driver setup failed: {exc}")
    finally:
        if _driver:
            try:
                _driver.quit()
            except Exception:
                pass
