import logging
import  random
import time
from datetime import datetime

from selenium.common import ElementClickInterceptedException, StaleElementReferenceException, NoSuchElementException, \
    TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class Actions:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self, locator):
        #self.driver.find_element(*locator).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, value):
        # self.driver.find_element(*locator).clear()
        #self.driver.find_element(*locator).send_keys(value)
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).clear()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).send_keys(value)

    def clear_text(self, locator):
        element = self.driver.find_element(*locator)
        element.click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(
            Keys.BACKSPACE).perform()
        element.clear()

    def wait_for_overlay_to_disappear(self, timeout=10):
        """Wait for any overlay to disappear before interacting with the element."""
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "div[style*='z-index: 1000']"))
        )

    def send_text(self, locator, value):
        element = self.driver.find_element(*locator)

        # Select all text in the input field
        ActionChains(self.driver).move_to_element(element).click().key_down(Keys.CONTROL).send_keys('a').key_up(
            Keys.CONTROL).perform()
        element.send_keys(value)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def get_attribute(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element.text.strip()

    def get_attribute_value(self, locator, attribute_name="value", timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.get_attribute(attribute_name).strip() if element.get_attribute(attribute_name) else ""

    def get_attribute_error(self, locator, attribute_name="errortext", timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.get_attribute(attribute_name).strip() if element.get_attribute(attribute_name) else ""




    def select_value_from_dropdown(self, locator, value):
        element = Select(self.driver.find_element(*locator))
        element.select_by_value(value)

    def select_options_from_dropdown(self, locator):
        return Select(self.driver.find_element(*locator))

    def select_text_from_dropdown(self, locator, value):
        element = Select(self.driver.find_element(*locator))
        element.select_by_visible_text(value)

    def wait_for_element(self, locator, timeout=100):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_visible(self, locator, timeout=30):

        try:
            # Wait for the page to load completely
            WebDriverWait(self.driver, timeout).until(
                lambda driver: self.driver.execute_script("return document.readyState") == "complete"
            )
            # Wait for the element to be visible
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception as e:
            print(f"Error waiting for page load or element to be visible: {locator}, Exception: {e}")
            return False

    def wait_for_element_to_load(self, timeinsecond):
        time.sleep(timeinsecond)

    def wait_for_page_load(self, timeout):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def wait_for(self, locator):
        WebDriverWait(self.driver, 80).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=50):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_element_invisible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_text_to_be_present(self, locator, text, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def is_element_present_and_visible(self, locator):
        """Check if an element is present and visible."""
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except Exception as e:
            print(f"Error checking element visibility: {locator}, Exception: {e}")
            return False

    def is_element_selected(self, locator):
        """Check if an element is present and visible."""
        try:
            element = self.driver.find_element(*locator)
            return element.is_selected()
        except Exception as e:
            print(f"Error checking element visibility: {locator}, Exception: {e}")
            return False

    def is_element_enabled(self, locator):
        """Check if an element is present and visible."""
        try:
            element = self.driver.find_element(*locator)
            return element.is_enabled()
        except Exception as e:
            print(f"Error checking element visibility: {locator}, Exception: {e}")
            return False

    def switch_to_iframe_by_id(self, locator):
        # Locate the iframe element by its ID
        iframe_element = self.driver.find_element(*locator)
        self.driver.switch_to.frame(iframe_element)

    def switch_back_to_default_content(self):
        # Switch back to the main document (default content)
        self.driver.switch_to.default_content()

    def navigate_to_url(self, url):
        self.driver.get(url)

    def click_on_element_with_js(self, element):
        """
        Click on an element using JavaScript Executor.

        :param element: The WebElement to click.
        """
        try:
            # Ensure the element is visible and interactable
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            raise Exception(f"Unable to click on element using JavaScript: {e}")

    def scroll_with_retry(self, driver, max_retries=5, scroll_distance=500, delay=1):
        retries = 0
        previous_scroll_position = -1

        while retries < max_retries:
            # Get the current scroll position
            current_scroll_position = self.driver.execute_script("return window.scrollY;")

            # Break if the page has stopped scrolling
            if current_scroll_position == previous_scroll_position:
                print("Scrolling complete.")
                break

            # Perform the scroll
            driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
            print(f"Attempt {retries + 1}: Scrolled by {scroll_distance} pixels.")

            # Update the previous scroll position
            previous_scroll_position = current_scroll_position

            # Wait before the next scroll attempt
            time.sleep(delay)

            # Increment retries
            retries += 1

        if retries == max_retries:
            print("Max retries reached. Scrolling stopped.")

    def scroll_to_the_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_the_element(self, locator, wait_time=20):
        #element = self.driver.find_element(locator)
        #self.driver.execute_script("arguments[0].scrollIntoView(true);", element)  # Scroll to the element
        wait = WebDriverWait(self.driver, wait_time)
        #Wait until the element is present in the DOM
        element = wait.until(EC.presence_of_element_located(locator))
        # Scroll the element into view
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        # Ensure the element is visible after scrolling
        wait.until(EC.visibility_of(element))

    def dropdown_equals(self, dropdown_locator, de_options_locator, value, wait_time=50):
        wait = WebDriverWait(self.driver, wait_time)

        # Click the dropdown
        dropdown = self.driver.find_element(*dropdown_locator)
        dropdown.click()
        time.sleep(1)

        # Type the desired value
        dropdown.send_keys(value)
        time.sleep(1)

        # Wait for dropdown options to be visible
        wait.until(EC.visibility_of_element_located(de_options_locator))
        options = self.driver.find_elements(*de_options_locator)

        # Loop through options to find the EXACT match only
        matched = False
        for option in options:
            option_text = option.text.strip()
            if option_text.lower() == value.lower():
                option.click()
                matched = True
                #print(f"✅ Selected exact match: {option_text}")
                break

        if not matched:
            raise Exception(f"❌ No exact match found for '{value}'")


    def dropdown_contains(self, dropdown_locator, dc_options_locator, value, wait_time=20):
        wait = WebDriverWait(self.driver, wait_time)
        dropdown = wait.until(EC.element_to_be_clickable(dropdown_locator))
        dropdown.click()
        time.sleep(2)
        dropdown.send_keys(value)
        wait.until(EC.visibility_of_element_located(dc_options_locator))
        options = self.driver.find_elements(*dc_options_locator)
        best_match = None
        for option in options:
            option_text = option.text.strip().lower()
            if value.lower() in option_text:  # Partial match
                best_match = option
                break
        if best_match:
            best_match.click()

    def force_dropdown_contains(self, dropdown_locator, options_locator, value, wait_time=20):
        wait = WebDriverWait(self.driver, wait_time)

        # Retry mechanism
        for attempt in range(3):
            try:
                # Scroll to element
                elem = wait.until(EC.presence_of_element_located(dropdown_locator))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)

                # Wait for clickability
                elem = wait.until(EC.element_to_be_clickable(dropdown_locator))

                # Click using JavaScript
                self.driver.execute_script("arguments[0].click();", elem)

                # Type slowly
                for char in value:
                    elem.send_keys(char)
                    time.sleep(0.1)

                # Wait for options
                wait.until(EC.visibility_of_element_located(options_locator))

                # Select matching option
                options = self.driver.find_elements(*options_locator)
                for option in options:
                    if value.lower() in option.text.lower():
                        self.driver.execute_script("arguments[0].click();", option)
                        return True

            except Exception as e:
                if attempt == 2:  # Last attempt
                    raise
                time.sleep(1)

        return False
    def dropdown_no_inp(self, dropdown_locator, de_options_locator, value, wait_time=10):
        wait = WebDriverWait(self.driver, wait_time)

        # Click the dropdown to open options
        dropdown = wait.until(EC.element_to_be_clickable(dropdown_locator))
        dropdown.click()

        # Wait until the dropdown options are visible
        wait.until(EC.visibility_of_element_located(de_options_locator))

        # Fetch all options
        options = self.driver.find_elements(*de_options_locator)

        for option in options:
            if option.text.strip().lower() == value.lower():
                option.click()  # Select the matched option
                return True  # Option found and selected

        raise ValueError(f"Option '{value}' not found in dropdown")

    def dropdown_select(self, dropdown_locator, value):
        dropdown_element = self.driver.find_element(*dropdown_locator)
        dropdown_element.click()
        select = Select(dropdown_element)
        value = value.strip().title()
        select.select_by_visible_text(value)

    def click_with_retry(self, locator, max_attempts=2, delay=1):
        """
        Click an element with retry mechanism

        Args:
            driver: WebDriver instance
            locator: Tuple of (By, selector) e.g., (By.ID, 'myButton')
            max_attempts: Maximum number of retry attempts
            delay: Delay between retries in seconds

        Returns:
            True if click succeeded, False if all attempts failed
        """
        attempts = 0
        while attempts < max_attempts:
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(locator)).click()

                return True
            except (ElementClickInterceptedException, StaleElementReferenceException, NoSuchElementException) as e:
                attempts += 1
                print(f"Click attempt {attempts} failed. Retrying in {delay} seconds...")
                if attempts < max_attempts:
                    time.sleep(delay)

        print(f"Failed to click element after {max_attempts} attempts")
        return False


    def is_future_date(self, current_month_year, target_month_year):
        current_date = datetime.strptime(current_month_year, "%B %Y")
        target_date = datetime.strptime(target_month_year, "%B %Y")
        return target_date > current_date

    def select_date(self, input_locator, datepicker_month_class, next_btn_class, prev_btn_class, asof_date, wait_time=10):
        wait = WebDriverWait(self.driver, wait_time)
        """
        asof_date: A string like "April 2025, April 15, 2025"
        """
        parts = asof_date.split(", ")
        months_year = parts[0]  # e.g., "April 2025"
        date_to_select = parts[1]  # e.g., "April 15, 2025"

        # Click on the date input field
        self.driver.find_element(*input_locator).click()

        # Get current month from the date picker
        current_month_year = self.driver.find_element(*datepicker_month_class).text.strip()

        # Navigate to the correct month
        while current_month_year.lower() != months_year.lower():
            if self.is_future_date(current_month_year, months_year):
                self.driver.find_element(*next_btn_class).click()
            else:
                self.driver.find_element(*prev_btn_class).click()
            time.sleep(0.5)
            current_month_year = self.driver.find_element(*datepicker_month_class).text.strip()

        # Wait until the correct month is visible
        wait.until(EC.text_to_be_present_in_element
            (datepicker_month_class, months_year))

        # Select the desired date
        xpath = f"//div[contains(@aria-label, '{date_to_select}')]"
        day_to_select = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        day_to_select.click()

    def wait_until_url_contains(self, text, timeout=20):
        """
        Wait until the current URL contains the given substring.
        :param text: Substring expected in the URL.
        :param timeout: Max wait time in seconds.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(text)
            )
            return True
        except Exception as e:
            raise Exception(f"URL did not contain '{text}' within {timeout} seconds. "
                            f"Current URL: {self.driver.current_url}") from e

    def wait_until_url_contains_any(self, substrings, timeout=30):
        """
        Wait until the URL contains ANY of the provided substrings.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: any(s in d.current_url for s in substrings)
            )
            return True
        except Exception:
            raise TimeoutException(
                f"Timed out waiting for URL to contain ANY of {substrings}. "
                f"Current URL: {self.driver.current_url}"
            )

    def element_exists(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    def refresh_page(self, timeout=10):
        """
        Refresh the current page and wait until it is fully loaded.
        :param timeout: Maximum wait time for page load.
        """
        try:
            self.driver.refresh()  # Refresh the browser
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            logging.info("Page refreshed and fully loaded.")
        except Exception as e:
            logging.error(f"Error while refreshing the page: {e}")
            raise

    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_all_elements(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return self.driver.find_elements(*locator)
        except TimeoutException:
            return []




















