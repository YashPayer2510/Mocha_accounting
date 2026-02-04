import os
import sys
import time
import logging
from pathlib import Path
from datetime import datetime
from tempfile import mkdtemp
from typing import Type, Union

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from dotenv import load_dotenv

from utilities.website_data_reader import WebSiteDataReader

# -------------------- ENV CONFIG --------------------
load_dotenv()

USERNAME = os.getenv("VALIDLOGINUSERNAME", "").split(",")
PASSWORD = os.getenv("VALIDLOGINPASSWORD", "").split(",")
URL = os.getenv("URL")
REGISTRATION_URL = os.getenv("REGISTRATION_URL", URL)
BROWSER = os.getenv("BROWSER", "chrome")
REPORT_DIR = os.getenv("REPORT_DIR", "reports")
LOGS_DIR = os.getenv("LOG_DIR", "logs")
ALLURE_RESULTS_DIR = os.getenv("ALLURE_RESULTS_DIR", "allure-results")

# -------------------- LOGGING SETUP --------------------
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(ALLURE_RESULTS_DIR, exist_ok=True)

log_file = os.path.join(LOGS_DIR, f"selenium_test_{datetime.now():%Y%m%d_%H%M%S}.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# -------------------- REPORT PATHS --------------------
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_dir = os.path.join(REPORT_DIR, timestamp)
os.makedirs(report_dir, exist_ok=True)
report_path = os.path.join(report_dir, "report.html")

allure_results_path = os.path.join(ALLURE_RESULTS_DIR, timestamp)
os.makedirs(allure_results_path, exist_ok=True)

# -------------------- PYTEST CONFIG --------------------
def pytest_configure(config):
    config.option.htmlpath = report_path
    config.option.allure_report_dir = allure_results_path

def pytest_collection_modifyitems(items):
    for item in items:
        if "needs_login" in item.keywords:
            item.user_properties.append(("needs_login", True))

# -------------------- FIXTURES --------------------
@pytest.fixture
def website_setup(request):
    """Fixture for setting up and tearing down WebDriver."""
    browser = BROWSER.lower()
    _driver = None
    logger.info(f"Starting test with {browser.capitalize()} browser")

    try:
        # ---- Chrome ----
        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-extensions")
            options.add_argument("--force-device-scale-factor=0.85")
            options.add_argument("--remote-debugging-port=9222")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.set_capability("unhandledPromptBehavior", "accept")
            options.add_argument("--window-size=1920,1080")

            #  Headless for CI
            if os.getenv("GITHUB_ACTIONS", "").lower() == "true":
                options.add_argument("--headless=new")
            else:
                options.add_argument(f"--user-data-dir={mkdtemp()}")

            _driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

        # ---- Firefox ----
        elif browser == "firefox":
            options = FirefoxOptions()
            if os.getenv("GITHUB_ACTIONS", "").lower() == "true":
                options.add_argument("--headless")
            _driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )

        # ---- Edge ----
        elif browser == "edge":
            options = EdgeOptions()
            if os.getenv("GITHUB_ACTIONS", "").lower() == "true":
                options.add_argument("--headless=new")
            _driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=options
            )

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        #_driver.maximize_window()
        _driver.implicitly_wait(5)

        # ---- Navigation ----
        is_registration = request.node.get_closest_marker("is_registration")
        target_url = REGISTRATION_URL if is_registration else URL
        _driver.get(target_url)
        logger.info(f"Navigated to: {target_url}")

        yield _driver

    except Exception as e:
        logger.error(f"Driver setup failed: {e}")
        pytest.fail(f"Driver setup failed: {e}")

    finally:
        if _driver:
            logger.info("Closing browser")
            try:
                _driver.quit()
            except Exception as e:
                logger.warning(f"Error during driver quit: {e}")

# -------------------- DATA FIXTURE GENERATOR --------------------
def generate_data_fixture(file_name: str, reader_class: Union[Type[WebSiteDataReader]]):
    def fixture():
        try:
            return reader_class.read_json(file_name)
        except Exception as e:
            pytest.fail(f"Could not load test data from {file_name}: {e}")
    return fixture

book_demo_test_data = pytest.fixture(scope="session")(generate_data_fixture("book_demo_test_data.json", WebSiteDataReader))