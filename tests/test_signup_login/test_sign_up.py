import logging
import os
import time

import pytest

from pages.registration import Registration
from utilities.get_mail_otp import get_latest_otp_email
from pages.login_page import LoginPage


logger = logging.getLogger(__name__)

@pytest.mark.is_registration
def test_ete_registration_india(sign_login_setup, registration_test_data):
    driver = sign_login_setup
    registration = Registration(driver)
    login = LoginPage(driver)

    registration.registration_signup_sign_up_btn()
    logger.info("Clicked on Sign-up for free button")

    registration.registration_signup_first_name(registration_test_data)
    logger.info("Entered the first name")

    registration.registration_signup_last_name(registration_test_data)
    logger.info("Entered the last name")

    unique_email_id = registration.registration_signup_email(registration_test_data)
    logger.info(f"Entered the email: {unique_email_id}")

    registration.registration_signup_phone_number_country(registration_test_data)
    logger.info("Selected country for phone number")

    registration.registration_signup_phone_number(registration_test_data)
    logger.info("Entered phone number")

    registration.registration_signup_agreed_to_policy_chkbx(registration_test_data)
    logger.info("Agreed to policy checkbox checked")

    registration.registration_signup_submit_btn(registration_test_data)
    logger.info("Clicked on Sign-up button")
    time.sleep(5)
    # Fetch OTP using the unique email
    otp = get_latest_otp_email()
    time.sleep(2)
    registration.registration_enter_otp(otp)
    logger.info("Entered Otp")
    time.sleep(5)
    registration.registration_enter_password(registration_test_data)
    logger.info("Set the password")
    registration.registration_next_btn()
    logger.info("click on next button")
    time.sleep(5)
    login.enter_username(unique_email_id)
    logger.info("Entered email-id")
    login.enter_password(registration_test_data["registration_password"])
    logger.info("Entered password")
    login.click_loginbutton()
    logger.info("Clicked on Login button")
    time.sleep(5)
    registration.registration_organization_details_enter_org_name(registration_test_data)
    logger.info("Entered Organization name")
    registration.registration_organization_address_inp(registration_test_data)
    logger.info("Entered Organization address")
    registration.registration_organization_industry(registration_test_data)
    logger.info("Entered Organization website")
    registration.registration_next_btn()
    logger.info("click on next button")
    time.sleep(5)
    registration.registration_organization_choose_mocha_product_accounting()
    logger.info("Mocha Accounting product chosen")
    registration.registration_organization_tax_legal_submit_btn()
    logger.info("click on next button")
    time.sleep(5)
    registration.registration_organization_kickstart_your_journey_popup_setup_btn()
    logger.info("click on setup button")
    time.sleep(5)
    registration.registration_organization_accounting_details_base_currency(registration_test_data)
    logger.info("Selected base currency")
    registration.registration_organization_accounting_details_first_month_of_financial_year(registration_test_data)
    logger.info("Selected base first month for finance year")
    registration.registration_organization_accounting_details_first_month_of_tax_year(registration_test_data)
    logger.info("Selected base first month for tax year")
    registration.registration_next_btn()
    logger.info("click on next button")
    time.sleep(5)
    registration.registration_organization_other_preference_language_dd(registration_test_data)
    logger.info("Selected language")
    registration.registration_organization_other_preference_date_format_dd(registration_test_data)
    logger.info("Selected date format")
    #registration.registration_organization_other_preference_currency_format_dd(registration_test_data)
    #logger.info("Selected currency format")
    #registration.registration_organization_other_preference_time_zone_dd(registration_test_data)
    #logger.info("Selected time zone")
    registration.registration_organization_other_preference_time_format_dd(registration_test_data)
    logger.info("Selected time format")
    registration.registration_next_btn()
    logger.info("click on next button")
    time.sleep(5)
    registration.registration_organization_details_enter_org_lgl_name(registration_test_data)
    logger.info("Entered Organization legal name")
    registration.registration_organization_tax_legal_organization_id(registration_test_data)
    logger.info("Entered the Organization id")
    registration.registration_organization_tax_legal_tax_form_dd(registration_test_data)
    logger.info("Selected the Tax form")
    registration.registration_organization_tax_legal_gst_treatment_dd(registration_test_data)
    logger.info("Selected the gst treatment")
    registration.registration_organization_tax_legal_tax_no(registration_test_data)
    logger.info("Entered the tax no")
    registration.registration_organization_tax_legal_submit_btn()
    logger.info("Clicked on Submit button")
    time.sleep(20)
    registration.registration_organization_close_ads_popup()
    logger.info("Closed Ads popup")
    time.sleep(10)
    registration.registration_asset_given_org_name_and_displayed_org_name()
    logger.info("Asserted the displayed and given organization name")




@pytest.mark.is_registration
def test_ete_registration_non_india(sign_login_setup, registration_test_data):
    driver = sign_login_setup
    registration = Registration(driver)
    login = LoginPage(driver)

    registration.registration_signup_sign_up_btn()
    logger.info("Clicked on Sign-up for free button")

    registration.registration_signup_first_name(registration_test_data)
    logger.info("Entered the first name")

    registration.registration_signup_last_name(registration_test_data)
    logger.info("Entered the last name")

    unique_email_id = registration.registration_signup_email(registration_test_data)
    logger.info(f"Entered the email: {unique_email_id}")

    registration.registration_signup_phone_number_country(registration_test_data)
    logger.info("Selected country for phone number")

    registration.registration_signup_phone_number(registration_test_data)
    logger.info("Entered phone number")

    registration.registration_signup_agreed_to_policy_chkbx(registration_test_data)
    logger.info("Agreed to policy checkbox checked")

    registration.registration_signup_submit_btn(registration_test_data)
    logger.info("Clicked on Sign-up button")
    time.sleep(5)
    # Fetch OTP using the unique email
    otp = get_latest_otp_email()
    time.sleep(2)
    registration.registration_enter_otp(otp)
    logger.info("Entered Otp")
    time.sleep(5)
    registration.registration_enter_password(registration_test_data)
    logger.info("Set the password")
    registration.registration_next_btn()
    logger.info("click on next button")
    time.sleep(5)
    login.enter_username(unique_email_id)
    logger.info("Entered email-id")
    login.enter_password(registration_test_data["registration_password"])
    logger.info("Entered password")
    login.click_loginbutton()
    logger.info("Clicked on Login button")
    time.sleep(5)
    registration.registration_organization_details_enter_org_name(registration_test_data)
    logger.info("Entered Organization name")
    registration.registration_organization_address_entermanually()
    logger.info("Click on Enter Manually checkbox")
    registration.registration_organization_address_inp_manually(registration_test_data)
    logger.info("Entered Organization address")
    registration.registration_organization_address_country(registration_test_data)
    logger.info("Entered Country")
    registration.registration_organization_address_state(registration_test_data)
    logger.info("Entered state")
    registration.registration_organization_address_city(registration_test_data)
    logger.info("Entered city")
    registration.registration_organization_address_zip(registration_test_data)
    logger.info("Entered zip")
    registration.registration_organization_industry(registration_test_data)
    logger.info("Entered Organization website")
    registration.registration_next_btn()
    logger.info("click on next button")
    time.sleep(5)
    #registration.registration_organization_choose_mocha_product_accounting()
    #logger.info("Mocha Accounting product chosen")
    #registration.registration_organization_tax_legal_submit_btn()
    #logger.info("click on next button")
    #time.sleep(5)
    #registration.registration_organization_kickstart_your_journey_popup_setup_btn()
    #logger.info("click on setup button")
    #time.sleep(5)
    registration.registration_organization_accounting_details_base_currency(registration_test_data)
    logger.info("Selected base currency")
    registration.registration_organization_accounting_details_first_month_of_financial_year(registration_test_data)
    logger.info("Selected base first month for finance year")
    registration.registration_organization_accounting_details_first_month_of_tax_year(registration_test_data)
    logger.info("Selected base first month for tax year")
    registration.registration_next_btn()
    logger.info("click on next button")
    time.sleep(5)
    registration.registration_organization_other_preference_language_dd(registration_test_data)
    logger.info("Selected language")
    registration.registration_organization_other_preference_date_format_dd(registration_test_data)
    logger.info("Selected date format")
    #registration.registration_organization_other_preference_currency_format_dd(registration_test_data)
    #logger.info("Selected currency format")
    #registration.registration_organization_other_preference_time_zone_dd(registration_test_data)
    #logger.info("Selected time zone")
    registration.registration_organization_other_preference_time_format_dd(registration_test_data)
    logger.info("Selected time format")
    registration.registration_next_btn()
    logger.info("click on next button")
    time.sleep(5)
    registration.registration_organization_details_enter_org_lgl_name(registration_test_data)
    logger.info("Entered Organization legal name")
    registration.registration_organization_tax_legal_organization_id(registration_test_data)
    logger.info("Entered the Organization id")
    registration.registration_organization_tax_legal_tax_form_dd(registration_test_data)
    logger.info("Selected the Tax form")
    registration.registration_organization_tax_legal_einssn(registration_test_data)
    logger.info("Entered EIN/SSN")
    registration.registration_organization_tax_legal_submit_btn()
    logger.info("Clicked on Submit button")
    time.sleep(20)
    registration.registration_organization_close_ads_popup()
    logger.info("Closed Ads popup")
    time.sleep(10)
    registration.registration_asset_given_org_name_and_displayed_org_name()
    logger.info("Asserted the displayed and given organization name")


















