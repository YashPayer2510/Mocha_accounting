import logging
import time
import datetime
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.actions import Actions
from tests.test_website.conftest import timestamp
from datetime import datetime, timedelta

class Book_Demo_Flow:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 50)

    book_demo_btn = (By.XPATH,"//button[contains(@class,'whitespace-nowrap')][normalize-space()='Book a Demo']")
    book_demo_full_name = (By.XPATH,"//input[contains(@name,'name')]")
    book_demo_email = (By.XPATH,"//input[contains(@name,'email')]")
    book_demo_select_country_code = (By.XPATH,"//select[@name='countryCode']")
    book_demo_phone_no = (By.XPATH,"//input[contains(@name,'contactNumber')]")
    book_demo_select_job_title = (By.XPATH,"//select[@name='jobTitle']")
    book_demo_inp_message = (By.XPATH,"//textarea[@placeholder='Message']")
    book_demo_next_btn = (By.XPATH,"//button[@type='submit']")
    book_demo_blank_name_validation = (By.XPATH,"//div[normalize-space()='Name is required']")
    book_demo_blank_email_validation = (By.XPATH, "//div[normalize-space()='Email is required']")
    book_demo_blank_phone_no_validation = (By.XPATH, "//div[normalize-space()='Phone number is required']")
    book_demo_blank_job_title_validation = (By.XPATH, "//div[normalize-space()='Please select a job title']")
    book_demo_slots_all_days = (By.XPATH,"//div[contains(@class,'flex-wrap') and contains(@class,'gap-2')] //button[contains(@class,'rounded')]")
    book_demo_slots_time = (By.XPATH,"//p[normalize-space()='Available Time Slots:']/following-sibling::div//button[contains(@class,'rounded')]")
    book_demo_slots_no_slot_msg = (By.XPATH,"//p[normalize-space()='Available Time Slots:']/following-sibling::div[normalize-space()='No slots available for this date.']")
    book_demo_slots_today = (By.XPATH,"//div[contains(@class,'flex-wrap') and contains(@class,'gap-2')] //button[contains(@class,'rounded')][1]")
    book_demo_slots_day_2 = (By.XPATH,"//div[contains(@class,'flex-wrap') and contains(@class,'gap-2')] //button[contains(@class,'rounded')][2]")
    book_demo_slots_day_3 = (By.XPATH,"//div[contains(@class,'flex-wrap') and contains(@class,'gap-2')] //button[contains(@class,'rounded')][3]")
    book_demo_slots_day_4 = (By.XPATH,"//div[contains(@class,'flex-wrap') and contains(@class,'gap-2')] //button[contains(@class,'rounded')][4]")
    book_demo_slots_day_5 = (By.XPATH,"//div[contains(@class,'flex-wrap') and contains(@class,'gap-2')] //button[contains(@class,'rounded')][5]")
    book_demo_slots_day_6 = (By.XPATH,"//div[contains(@class,'flex-wrap') and contains(@class,'gap-2')] //button[contains(@class,'rounded')][6]")
    book_demo_slots_day_7 = (By.XPATH,"//div[contains(@class,'flex-wrap') and contains(@class,'gap-2')] //button[contains(@class,'rounded')][7]")
    book_demo_slots_firs_time_slot = (By.XPATH,"//p[normalize-space()='Available Time Slots:']/following-sibling::div//button[contains(@class,'rounded')][1]")
    book_demo_slots_confirm_btn = (By.XPATH,"//button[normalize-space()='Confirm Booking']")
    book_demo_booked_slot_time_confirmation_page = (By.XPATH,"//p[normalize-space()='Time']/parent::*//p[contains(@class,'font-semibold')]")
    book_demo_booked_slot_date_confirmation_page = (By.XPATH, "//p[normalize-space()='Date']/following-sibling::p[@class='font-semibold']")


    def book_demo_btn_click(self):
        self.actions.wait_for_element(self.book_demo_btn)
        self.actions.click(self.book_demo_btn)

    def book_demo_enter_full_name(self, book_demo_test_data):
        self.actions.wait_for_element(self.book_demo_full_name)
        unique_name_id = f"{book_demo_test_data['full_name']}+{timestamp}"
        self.actions.send_keys(self.book_demo_full_name,unique_name_id)

    def book_demo_enter_email(self, book_demo_test_data):
        self.actions.wait_for_element(self.book_demo_email)
        unique_email_id = f"{book_demo_test_data['email']}+{timestamp}@gmail.com"
        self.actions.send_keys(self.book_demo_email, unique_email_id)
        return unique_email_id

    def book_demo_dd_select_country_code(self, book_demo_test_data):
        self.actions.wait_for_element(self.book_demo_select_country_code)
        self.actions.dropdown_select(self.book_demo_select_country_code, book_demo_test_data["country_code"])

    def book_demo_enter_phone_number(self, book_demo_test_data):
        self.actions.wait_for_element(self.book_demo_phone_no)
        self.actions.send_keys(self.book_demo_phone_no, book_demo_test_data["phone_number"] )

    def book_demo_dd_select_job_title(self, book_demo_test_data):
        self.actions.wait_for_element(self.book_demo_select_job_title)
        self.actions.dropdown_select(self.book_demo_select_job_title, book_demo_test_data["job_title"])

    def book_demo_enter_message(self, book_demo_test_data):
        self.actions.wait_for_element(self.book_demo_inp_message)
        self.actions.send_keys(self.book_demo_inp_message, book_demo_test_data["message"])

    def book_demo_click_next_btn(self):
        self.actions.wait_for_element(self.book_demo_next_btn)
        self.actions.scroll_to_the_element(self.book_demo_next_btn)
        self.actions.click(self.book_demo_next_btn)

    def book_demo_get_blank_name_validation(self, book_demo_test_data):
        expected_blank_fullname_validation = book_demo_test_data["expected_fullname_validation"]
        actual_blank_fullname_validation = self.actions.get_text(self.book_demo_blank_name_validation)
        assert expected_blank_fullname_validation == actual_blank_fullname_validation, "Name field is blank"

    def book_demo_get_blank_email_validation(self, book_demo_test_data):
        expected_blank_email_validation = book_demo_test_data["expected_blank_email_validation"]
        actual_blank_email_validation = self.actions.get_text(self.book_demo_blank_email_validation)
        assert expected_blank_email_validation == actual_blank_email_validation, "Email field is blank"

    def book_demo_get_blank_phone_no_validation(self, book_demo_test_data):
        expected_blank_phone_no_validation = book_demo_test_data["expected_blank_phone_no_validation"]
        actual_blank_phone_no_validation = self.actions.get_text(self.book_demo_blank_phone_no_validation)
        assert expected_blank_phone_no_validation == actual_blank_phone_no_validation, "Phone no field is blank"

    def book_demo_get_blank_job_title_validation(self, book_demo_test_data):
        expected_blank_job_title_validation = book_demo_test_data["expected_blank_job_title_validation"]
        actual_blank_job_title_validation = self.actions.get_text(self.book_demo_blank_job_title_validation)
        assert expected_blank_job_title_validation == actual_blank_job_title_validation, "Job title field is blank"

    def book_demo_get_incorrect_validation_messages(self, book_demo_test_data):
        expected_validation_msg = book_demo_test_data["expected_validation_without_@"]
        actual_validation_msg =  self.driver.execute_script(
            "return arguments[0].validationMessage;", self.book_demo_email
        )
        print(actual_validation_msg)
        assert expected_validation_msg in actual_validation_msg

    def book_demo_get_click_confirm_booking_btn(self):
        self.actions.wait_for_element(self.book_demo_slots_confirm_btn)
        self.actions.click(self.book_demo_slots_confirm_btn)

    def get_email_html5_validation_message(self, email_value: str):
        self.actions.wait_for_element(self.book_demo_email)
        email_element = self.driver.find_element(*self.book_demo_email)
        email_element.clear()
        email_element.send_keys(email_value)
        # Trigger native HTML5 validation properly
        self.driver.execute_script("arguments[0].reportValidity();", email_element)
        actual_validation_msg = self.driver.execute_script(
            "return arguments[0].validationMessage;", email_element
        )
        return actual_validation_msg.strip()

    def verify_next_7_working_days_dates(self):
        elements = self.driver.find_elements(*self.book_demo_slots_all_days)
        ui_dates = [el.text.strip() for el in elements]

        today = datetime.now()

        # If today is Sat (5) or Sun (6), move to next Monday
        if today.weekday() == 5:  # Saturday
            current_day = today + timedelta(days=2)
        elif today.weekday() == 6:  # Sunday
            current_day = today + timedelta(days=1)
        else:
            current_day = today

        expected_dates = []

        # Collect 7 working days
        while len(expected_dates) < 7:
            if current_day.weekday() not in (5, 6):  # Skip weekends
                formatted_date = current_day.strftime("%a, %b ") + str(current_day.day)
                expected_dates.append(formatted_date)

            current_day += timedelta(days=1)

        assert ui_dates == expected_dates, \
            f"\nExpected: {expected_dates}\nGot: {ui_dates}"

    def verify_time_slots_for_all_7_days(self, book_demo_test_data):
        expected_no_slot_msg = book_demo_test_data["expected_no_slot_msg"]

        all_dates = self.actions.get_all_elements(self.book_demo_slots_all_days)

        assert len(all_dates) == 7, f"Expected 7 dates, found {len(all_dates)}"

        for date in all_dates:
            date_text = date.text.strip()
            date.click()
            # Case 1: No slot message present
            if self.actions.is_element_present(self.book_demo_slots_no_slot_msg):
                actual_msg = self.actions.get_text(self.book_demo_slots_no_slot_msg).strip()

                assert actual_msg == expected_no_slot_msg, \
                    f"[{date_text}] Expected '{expected_no_slot_msg}' but got '{actual_msg}'"

            # Case 2: Slots present
            elif self.actions.is_element_present(self.book_demo_slots_time):
                slots = self.actions.get_all_elements(self.book_demo_slots_time)

                assert len(slots) > 0, \
                    f"[{date_text}] Slots section visible but no slots found!"

            # Case 3: Broken page
            else:
                raise AssertionError(
                    f"[{date_text}] Neither slots nor 'No slots' message displayed."
                )

    from datetime import datetime
    import time

    def date_and_time_slot_selected(self):
        all_dates = self.actions.get_all_elements(self.book_demo_slots_all_days)

        slot_found = False
        selected_date_text = ""
        slot_time_value = ""

        for date in all_dates:
            selected_date_text = date.text.strip()  # e.g. "Wed, Feb 4"
            date.click()
            time.sleep(2)

            # Case 1: No slots → move to next day
            if self.actions.is_element_present(self.book_demo_slots_no_slot_msg):
                print(f"[{selected_date_text}] No slots available. Moving to next day.")
                continue

            # Case 2: Slots present → click first slot and STOP
            elif self.actions.is_element_present(self.book_demo_slots_time):
                slot_time_value = self.actions.get_text(
                    self.book_demo_slots_firs_time_slot)  # e.g. "06:00 PM – 06:30 PM"
                print(f"[{selected_date_text}] Slots found. Booking first slot: {slot_time_value}")
                self.actions.click(self.book_demo_slots_firs_time_slot)
                slot_found = True
                break

            # Case 3: Broken page
            else:
                raise AssertionError(
                    f"[{selected_date_text}] Neither slots nor 'No slots' message displayed."
                )

        # If no slots found in any day
        if not slot_found:
            raise AssertionError("No slots available in any of the next 7 days.")

        # Click Confirm
        self.actions.click(self.book_demo_slots_confirm_btn)

        # Capture values from confirmation page
        date_displayed_on_confirmation_page = self.actions.get_text(
            self.book_demo_booked_slot_date_confirmation_page
        ).strip()

        time_displayed_on_confirmation_page = self.actions.get_text(
            self.book_demo_booked_slot_time_confirmation_page
        ).strip()

        print(f"Selected Date (Slot Page): {selected_date_text}")
        print(f"Selected Time (Slot Page): {slot_time_value}")
        print(f"Confirmation Date: {date_displayed_on_confirmation_page}")
        print(f"Confirmation Time: {time_displayed_on_confirmation_page}")

        # -------- Normalize Selected Date (Slot page) --------
        # "Wed, Feb 4"
        selected_date_obj = datetime.strptime(selected_date_text, "%a, %b %d")
        current_year = datetime.now().year
        selected_date_obj = selected_date_obj.replace(year=current_year)

        # -------- Normalize Confirmation Date --------
        # "Wednesday, February 4, 2026"
        confirmation_date_obj = datetime.strptime(
            date_displayed_on_confirmation_page,
            "%A, %B %d, %Y"
        )

        # -------- Normalize Selected Time --------
        selected_start_time = slot_time_value.split("–")[0].strip()
        selected_time_obj = datetime.strptime(selected_start_time, "%I:%M %p")

        # -------- Normalize Confirmation Time --------
        confirmation_start_time = time_displayed_on_confirmation_page.split("–")[0].strip()
        confirmation_time_obj = datetime.strptime(confirmation_start_time, "%I:%M %p")

        # -------- Assertions --------
        assert selected_date_obj.date() == confirmation_date_obj.date(), \
            f"Date mismatch! Slot: {selected_date_obj.date()} | Confirmation: {confirmation_date_obj.date()}"

        assert selected_time_obj.time() == confirmation_time_obj.time(), \
            f"Time mismatch! Slot: {selected_time_obj.time()} | Confirmation: {confirmation_time_obj.time()}"

        print("Date and Time on confirmation page matches selected slot.")













