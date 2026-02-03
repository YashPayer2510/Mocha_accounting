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
    time.sleep(2)
    registration.registration_signup_sign_up_btn()
    logger.info("Clicked on Sign-up for free button")
    registration.registration_signup_first_name(registration_test_data)
    logger.info("Entered the first name")
    registration.registration_signup_last_name(registration_test_data)
    logger.info("Entered the last name")
    unique_email_id = registration.registration_signup_email(registration_test_data)
    logger.info(f"Entered the email: {unique_email_id}")
    registration.registration_signup_phone_number_country_india(registration_test_data)
    logger.info("Selected country for phone number")
    registration.registration_signup_phone_number_india(registration_test_data)
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
    time.sleep(2)
    registration.registration_enter_password(registration_test_data)
    #registration.registration_enter_password_new(registration_test_data)
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
    registration.registration_organization_details_enter_company_name(registration_test_data)
    logger.info("Entered Organization name")
    registration.registration_organization_address_india_inp(registration_test_data)
    logger.info("Entered Organization address")
    registration.registration_next_btn()
    logger.info("click on next button")
    time.sleep(5)
    registration.registration_pricing_plan_start_for_free_btn()
    logger.info("click on start for free button")
    registration.registration_pricing_plan_nxt_btn()
    logger.info("click on next button")
    registration.registration_pricing_plan_procd_btn()
    logger.info("click on proceed button")
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
    time.sleep(2)
    registration.registration_signup_sign_up_btn()
    logger.info("Clicked on Sign-up for free button")
    registration.registration_signup_first_name(registration_test_data)
    logger.info("Entered the first name")
    registration.registration_signup_last_name(registration_test_data)
    logger.info("Entered the last name")
    unique_email_id = registration.registration_signup_email(registration_test_data)
    logger.info(f"Entered the email: {unique_email_id}")
    registration.registration_signup_phone_number_country_non_india(registration_test_data)
    logger.info("Selected country for phone number")
    registration.registration_signup_phone_number_non_india(registration_test_data)
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
    time.sleep(2)
    #registration.registration_enter_password_new(registration_test_data)
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
    registration.registration_organization_details_enter_company_name(registration_test_data)
    logger.info("Entered Organization name")
    registration.registration_organization_address_entermanually()
    logger.info("Clicked on the enter manually check box")
    registration.registration_organization_address_inp_manually(registration_test_data)
    logger.info("Entered the Address line 1")
    registration.registration_organization_address_country_nonindia(registration_test_data)
    logger.info("Country selected")
    registration.registration_organization_address_state(registration_test_data)
    logger.info("State selected")
    registration.registration_organization_address_city(registration_test_data)
    logger.info("Entered City")
    registration.registration_organization_address_zip(registration_test_data)
    logger.info("Entered Zip")
    registration.registration_next_btn()
    logger.info("click on next button")
    time.sleep(5)
    registration.registration_pricing_plan_americano_purchase_btn()
    logger.info("Americano plan selected")
    registration.registration_pricing_plan_nxt_btn()
    logger.info("click on next button")
    registration.registration_pricing_plan_procd_btn()
    logger.info("click on proceed button")
    time.sleep(20)
    registration.registration_organization_close_ads_popup()
    logger.info("Closed Ads popup")
    time.sleep(10)
    registration.registration_asset_given_org_name_and_displayed_org_name()
    logger.info("Asserted the displayed and given organization name")


















