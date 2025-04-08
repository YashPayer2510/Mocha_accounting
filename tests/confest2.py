import logging
import time
import json
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
import sys
import os

from utilities.data_reader import DataReader

# Add the project root to the Python path for module discovery
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def test_data():
    """Read test data from JSON."""
    try:
        data = DataReader.read_json("test_data.json")
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Failed to load test data: {e}")
        pytest.fail("Could not load test data.")


@pytest.fixture(scope="function")
def setup(test_data):
    """Set up WebDriver for tests."""
    browser = test_data.get("browser", "chrome").lower()
    driver = None
    logger.info(f"Starting test with {browser.capitalize()} browser")

    try:
        if browser == "chrome":
            options = ChromeOptions()
            #options.add_argument("--headless")  # Uncomment to enable headless mode
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            #options.add_argument("--force-device-scale-factor=0.75")
            options.set_capability("unhandledPromptBehavior", "accept")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            logger.info("Chrome driver initialized")
        elif browser == "firefox":
            options = FirefoxOptions()
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
            logger.info("Firefox driver initialized")
        elif browser == "edge":
            options = EdgeOptions()
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
            logger.info("Edge driver initialized")
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get(test_data["url"])
        logger.info(f"Navigated to URL: {test_data['url']}")
        time.sleep(5)
        yield driver
    except Exception as e:
        logger.error(f"Driver setup failed: {e}")
        pytest.fail(f"Driver setup failed: {e}")
    finally:
        if driver:
            logger.info("Closing browser")
            driver.quit()
