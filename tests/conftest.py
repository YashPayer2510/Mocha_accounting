import os
import sys
import time
import logging
from datetime import datetime
#from tempfile import mkdtemp

import pytest
#from tempfile import mkdtemp
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

from utilities.data_reader import DataReader
from utilities.expense_data_reader import ExpenseDataReader

# Setup paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Load environment variables
load_dotenv()

# Get config from .env
USERNAME = os.getenv('VALIDLOGINUSERNAME').split(',')
PASSWORD = os.getenv('VALIDLOGINPASSWORD').split(',')
URL = os.getenv('URL')
BROWSER = os.getenv('BROWSER', 'chrome')
REPORT_DIR = os.getenv("REPORT_DIR", "reports")
LOGS_DIR = os.getenv("LOG_DIR", "logs")
ALLURE_RESULTS_DIR= os.getenv("ALLURE_RESULTS_DIR")

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

# Load test data
@pytest.fixture(scope="session")
def login_test_data():
    try:
        data = DataReader.read_json("login_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def createcustomer_test_data():
    try:
        data = DataReader.read_json("createcustomer_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def create_invoice_test_data():
    try:
        data = DataReader.read_json("create_invoice_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def receive_payment_test_data():
    try:
        data = DataReader.read_json("receive_payment_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def create_credit_memo_test_data():
    try:
        data = DataReader.read_json("create_credit_memo_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def create_sales_receipt_test_data():
    try:
        data = DataReader.read_json("create_sales_receipt_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def create_refund_receipt_test_data():
    try:
        data = DataReader.read_json("create_refund_receipt_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def all_sales_test_data():
    try:
        data = DataReader.read_json("all_sales_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def customer_list_test_data():
    try:
        data = DataReader.read_json("customer_list_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def customer_transaction_list_test_data():
    try:
        data = DataReader.read_json("customer_transaction_list_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def create_product_service_test_data():
    try:
        data = DataReader.read_json("create_product_service_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def create_vendor_test_data():
    try:
        data = ExpenseDataReader.read_json("create_vendor_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def expense_list_test_data():
    try:
        data = ExpenseDataReader.read_json("expense_list_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def create_bill_test_data():
    try:
        data = ExpenseDataReader.read_json("create_bill_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def create_expense_test_data():
    try:
        data = ExpenseDataReader.read_json("create_expense_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def create_check_test_data():
    try:
        data = ExpenseDataReader.read_json("create_check_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def create_purchase_order_test_data():
    try:
        data = ExpenseDataReader.read_json("create_purchase_order_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def create_vendor_credit_test_data():
    try:
        data = ExpenseDataReader.read_json("create_vendor_credit_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")

@pytest.fixture(scope="session")
def bill_payment_test_data():
    try:
        data = ExpenseDataReader.read_json("bill_payment_test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")


# WebDriver setup fixture
@pytest.fixture(scope="function")
def setup():
    browser = BROWSER.lower()
    driver = None
    logger.info(f"Starting test with {browser.capitalize()} browser")

    try:
        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--force-device-scale-factor=0.85")
            #options.add_argument("--headless=new")
            options.add_argument("--disable-extensions")
            options.add_argument("--remote-debugging-port=9222")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.set_capability("unhandledPromptBehavior", "accept")
            #options.add_argument(f"--user-data-dir={mkdtemp()}")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        elif browser == "edge":
            options = EdgeOptions()
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get(URL)
        logger.info(f"Navigated to URL: {URL}")
        login(driver)

        yield driver

    except Exception as e:
        logger.error(f"Driver setup failed: {e}")
        pytest.fail(f"Driver setup failed: {e}")
    finally:
        if driver:
            logout(driver)
            logger.info("Closing browser")
            driver.quit()

# Login method
def login(driver):
    try:
        from pages.login_page import LoginPage
        login_page = LoginPage(driver)
        login_page.enter_username(USERNAME[0])
        login_page.enter_password(PASSWORD[0])
        login_page.click_loginbutton()
        logger.info("Login successful.")
    except Exception as e:
        logger.error(f"Login failed: {e}")
        raise

# Logout method
def logout(driver):
    try:
        from pages.login_page import LoginPage
        logout_page = LoginPage(driver)
        time.sleep(4)
        logout_page.click_logged_out_profile()
        logout_page.click_logged_out_button()
        logger.info("Logout successful.")
    except Exception as e:
        logger.error(f"Logout failed: {e}")
        raise


