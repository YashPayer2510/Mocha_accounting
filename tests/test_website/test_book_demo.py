import logging
import os
import time

import pytest

from pages.web_site_pages.book_demo_page import Book_Demo_Flow
from pages.web_site_pages.internal_admin_table import  InternalAdminTable
from utilities.website_data_reader import WebSiteDataReader
book_demo_test_data = WebSiteDataReader.read_json("book_demo_test_data.json")
invalid_emails = book_demo_test_data["invalid_emails"]

internal_admin_demo_management_username= os.getenv('INTERNAL_ADMIN_DEMO_MANAGEMENT_USERNAME')
internal_admin_demo_management_password= os.getenv('INTERNAL_ADMIN_DEMO_MANAGEMENT_PASSWORD')
internal_admin_demo_management_url = os.getenv('INTERNAL_ADMIN_DEMO_MANAGEMENT_URL')

# Verify the login flow with valid credentials
logger = logging.getLogger(__name__)
@pytest.mark.is_registration
def test_valid_details_book_demo_form(website_setup, book_demo_test_data):
    driver = website_setup
    book_demo = Book_Demo_Flow(driver)
    book_demo.book_demo_btn_click()
    logger.info("Clicked on Book a Demo button")
    unique_email = book_demo.book_demo_enter_email(book_demo_test_data)
    logger.info("Entered the full name")
    book_demo.book_demo_enter_email(book_demo_test_data)
    logger.info("Entered the email")
    book_demo.book_demo_dd_select_country_code(book_demo_test_data)
    logger.info("Country Code selected")
    book_demo.book_demo_enter_phone_number(book_demo_test_data)
    logger.info("Entered the email")
    book_demo.book_demo_dd_select_job_title(book_demo_test_data)
    logger.info("Job title selected")
    book_demo.book_demo_enter_message(book_demo_test_data)
    logger.info("Entered the message")
    book_demo.book_demo_click_next_btn()
    logger.info("Clicked on next button")


# Verify the login flow with invalid credentials and validation message
@pytest.mark.is_registration
@pytest.mark.parametrize("email_data", invalid_emails)
def test_invalid_email_book_demo_form(website_setup, book_demo_test_data, email_data):
    driver = website_setup
    book_demo = Book_Demo_Flow(driver)
    book_demo.book_demo_btn_click()
    logger.info("Clicked on Book a Demo button")
    book_demo.book_demo_enter_full_name(book_demo_test_data)
    logger.info("Entered the full name")
    actual_msg = book_demo.get_email_html5_validation_message(email_data["email"])
    logger.info("Entered the email")
    assert email_data["msg"] in actual_msg

# Verify the login flow validation message when the username and password is kept blank.
@pytest.mark.is_registration
def test_mandatory_fields_blank_demo_form(website_setup, book_demo_test_data):
    driver = website_setup
    book_demo = Book_Demo_Flow(driver)
    book_demo.book_demo_btn_click()
    logger.info("Clicked on Book a Demo button")
    book_demo.book_demo_click_next_btn()
    logger.info("Clicked on Next")
    book_demo.book_demo_get_blank_name_validation(book_demo_test_data)
    logger.info("Asserted the expected blank validation and displayed blank validation for full name")
    book_demo.book_demo_get_blank_email_validation(book_demo_test_data)
    logger.info("Asserted the expected blank validation and displayed blank validation for email name")
    book_demo.book_demo_get_blank_phone_no_validation(book_demo_test_data)
    logger.info("Asserted the expected blank validation and displayed blank validation for phone no")
    book_demo.book_demo_get_blank_job_title_validation(book_demo_test_data)
    logger.info("Asserted the expected blank validation and displayed blank validation for job title")

# Verify the dates displayed is correct on book slot page.
@pytest.mark.is_registration
def verify_next_7_working_days_dates(website_setup, book_demo_test_data):
    driver = website_setup
    book_demo = Book_Demo_Flow(driver)
    book_demo.book_demo_btn_click()
    logger.info("Clicked on Book a Demo button")
    book_demo.book_demo_enter_full_name(book_demo_test_data)
    logger.info("Entered the full name")
    unique_email = book_demo.book_demo_enter_email(book_demo_test_data)
    logger.info("Entered the email")
    book_demo.book_demo_dd_select_country_code(book_demo_test_data)
    logger.info("Country Code selected")
    book_demo.book_demo_enter_phone_number(book_demo_test_data)
    logger.info("Entered the email")
    book_demo.book_demo_dd_select_job_title(book_demo_test_data)
    logger.info("Job title selected")
    book_demo.book_demo_enter_message(book_demo_test_data)
    logger.info("Entered the message")
    book_demo.book_demo_click_next_btn()
    logger.info("Cliked on next button")
    book_demo.verify_next_7_working_days_dates()
    logger.info("todays date and next 7 days dates displayed are verified")
    return unique_email

# Verify the time slots of each 7 days and validation message when no slot is available.
@pytest.mark.is_registration
def test_book_slots_verify_msg_and_each_days_slots(website_setup, book_demo_test_data):
    driver = website_setup
    book_demo = Book_Demo_Flow(driver)
    book_demo.book_demo_btn_click()
    logger.info("Clicked on Book a Demo button")
    book_demo.book_demo_enter_full_name(book_demo_test_data)
    logger.info("Entered the full name")
    unique_email = book_demo.book_demo_enter_email(book_demo_test_data)
    logger.info("Entered the email")
    book_demo.book_demo_dd_select_country_code(book_demo_test_data)
    logger.info("Country Code selected")
    book_demo.book_demo_enter_phone_number(book_demo_test_data)
    logger.info("Entered the email")
    book_demo.book_demo_dd_select_job_title(book_demo_test_data)
    logger.info("Job title selected")
    book_demo.book_demo_enter_message(book_demo_test_data)
    logger.info("Entered the message")
    book_demo.book_demo_click_next_btn()
    logger.info("Cliked on next button")
    book_demo.verify_time_slots_for_all_7_days(book_demo_test_data)
    logger.info("verified the slots of each day, expected message if no slot present or error generated")
    return unique_email

# Verify the date and time selected with the displayed date and time on the confirmation page.
# Verify the email added while booking demo is reflected in the internal demo portal table.
@pytest.mark.is_registration
def test_book_demo_email_reflects_in_admin(website_setup, book_demo_test_data):
    driver = website_setup
    book_demo = Book_Demo_Flow(driver)
    internal_admin = InternalAdminTable(driver)
    book_demo.book_demo_btn_click()
    logger.info("Clicked on Book a Demo button")
    book_demo.book_demo_enter_full_name(book_demo_test_data)
    logger.info("Entered the full name")
    unique_email =book_demo.book_demo_enter_email(book_demo_test_data)
    logger.info("Entered the email")
    book_demo.book_demo_dd_select_country_code(book_demo_test_data)
    logger.info("Country Code selected")
    book_demo.book_demo_enter_phone_number(book_demo_test_data)
    logger.info("Entered the email")
    book_demo.book_demo_dd_select_job_title(book_demo_test_data)
    logger.info("Job title selected")
    book_demo.book_demo_enter_message(book_demo_test_data)
    logger.info("Entered the message")
    book_demo.book_demo_click_next_btn()
    logger.info("Cliked on next button")
    book_demo.date_and_time_slot_selected()
    logger.info("Clicked on date and time slot")
    internal_admin.internal_admin_demo_enter_enter_url(internal_admin_demo_management_url)
    logger.info("Navigated to the internal admin URL")
    internal_admin.internal_admin_demo_enter_username(internal_admin_demo_management_username)
    logger.info("Enter the username")
    internal_admin.internal_admin_demo_enter_password(internal_admin_demo_management_password)
    logger.info("Enter the password")
    internal_admin.internal_admin_demo_click_sign_in_btn()
    logger.info("Clicked on sign-in btn")
    time.sleep(10)
    internal_admin.verify_email_in_table(unique_email)
    logger.info("Searching for email")










