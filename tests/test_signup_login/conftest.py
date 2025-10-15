import os
import sys
import time
import logging
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
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

from utilities.signup_login_data_reader import SignupLoginDataReader
load_dotenv()

# Get config from .env
USERNAME = os.getenv('VALIDLOGINUSERNAME').split(',')
PASSWORD = os.getenv('VALIDLOGINPASSWORD').split(',')
URL = os.getenv('URL')
REGISTRATION_URL = os.getenv("REGISTRATION_URL", URL)
BROWSER = os.getenv('BROWSER', 'chrome')
REPORT_DIR = os.getenv("REPORT_DIR", "reports")
LOGS_DIR = os.getenv("LOG_DIR", "logs")
ALLURE_RESULTS_DIR = os.getenv("ALLURE_RESULTS_DIR")

# Create directories
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# Logging setup
log_file = os.path.join(LOGS_DIR, f"selenium_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Report path
report_dir = os.path.join(REPORT_DIR, datetime.now().strftime("%Y%m%d_%H%M%S"))
os.makedirs(report_dir, exist_ok=True)
report_path = os.path.join(report_dir, "report.html")

allure_results_path = os.path.join(ALLURE_RESULTS_DIR, datetime.now().strftime("%Y%m%d_%H%M%S"))
os.makedirs(allure_results_path, exist_ok=True)

# Pytest hook for report path
def pytest_configure(config):
    config.option.htmlpath = report_path
    config.option.allure_report_dir = allure_results_path

# Register custom marker for conditional login
def pytest_collection_modifyitems(items):
    for item in items:
        if 'needs_login' in item.keywords:
            item.user_properties.append(("needs_login", True))

# WebDriver setup fixture
@pytest.fixture
def sign_login_setup(request):
    browser = BROWSER.lower()
    _driver = None
    logger.info(f"Starting test with {browser.capitalize()} browser")

    try:
        # 1. Driver setup
        if browser == "chrome":
            options = ChromeOptions()
            #options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--force-device-scale-factor=0.85")
            options.add_argument("--disable-extensions")
            options.add_argument("--remote-debugging-port=9222")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.set_capability("unhandledPromptBehavior", "accept")
            options.add_argument(f"--user-data-dir={mkdtemp()}")
            _driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        elif browser == "firefox":
            options = FirefoxOptions()
            _driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

        elif browser == "edge":
            options = EdgeOptions()
            _driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        _driver.maximize_window()
        _driver.implicitly_wait(3)

        # 2. URL selection logic
        is_registration = request.node.get_closest_marker("is_registration")
        if is_registration:
            _driver.get(REGISTRATION_URL)
            logger.info(f"Navigated to registration: {REGISTRATION_URL}")
        else:
            _driver.get(URL)
            logger.info(f"Navigated to URL: {URL}")

        yield _driver

    except Exception as e:
        logger.error(f"Driver setup failed: {e}")
        pytest.fail(f"Driver setup failed: {e}")

    finally:
        if _driver:
            logger.info("Closing browser")
            _driver.quit()

# Generic data fixture generator
def generate_data_fixture(file_name: str, reader_class: Union[Type[SignupLoginDataReader]]):
    def fixture():
        try:
            return reader_class.read_json(file_name)
        except Exception as e:
            pytest.fail(f"Could not load test data from {file_name}: {e}")
    return fixture

# Login/Registration data fixtures
login_test_data = pytest.fixture(scope="session")(generate_data_fixture("login_data.json", SignupLoginDataReader))
registration_test_data = pytest.fixture(scope="session")(generate_data_fixture("registration_test_data.json", SignupLoginDataReader))
