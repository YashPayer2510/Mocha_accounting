"""
Registration runner – performs a fresh Mocha Accounting registration
and saves the generated email + first_name to registration_history.json.

Run this test ONLY when a new registration is needed (the scheduler
determines this). The GitHub Action calls it via xvfb-run.

Reuses:
  - pages.registration.Registration  (via EnhancedRegistration subclass)
  - pages.login_page.LoginPage
  - utilities.get_mail_otp.get_latest_otp_email
  - data/registration_test_data.json
"""
import logging
import time

import pytest

from email_automation.utils.enhanced_registration import EnhancedRegistration
from email_automation.utils.registration_tracker import RegistrationTracker
from email_automation.services.scheduler import Scheduler
from pages.login_page import LoginPage
from utilities.get_mail_otp import get_latest_otp_email

logger = logging.getLogger(__name__)


# ── Helper ─────────────────────────────────────────────────────────────────────

def _should_register() -> bool:
    """Return True only when no active registration exists."""
    return RegistrationTracker().needs_registration()


# ── Tests ──────────────────────────────────────────────────────────────────────

@pytest.mark.is_registration
def test_daily_registration(email_reg_driver, registration_test_data):
    """
    Run a fresh India-based registration and save the result to
    registration_history.json.

    The test is skipped if an active registration already exists so that
    repeated GitHub Action triggers on the same day don't double-register.
    """
    if not _should_register():
        pytest.skip("Active registration already exists – skipping new registration.")

    driver = email_reg_driver
    reg = EnhancedRegistration(driver)
    login = LoginPage(driver)
    tracker = RegistrationTracker()

    # ── Step 1: Dismiss popup and click Sign-Up ────────────────────────────
    #time.sleep(5)
    #reg.registration_online_payment_popup_x_btn()
    #logger.info("Dismissed online payment popup.")
    #reg.registration_signup_sign_up_btn()
    #logger.info("Clicked Sign-up for free.")

    # ── Step 2: Fill personal details ─────────────────────────────────────
    reg.registration_signup_first_name(registration_test_data)
    reg.registration_signup_last_name(registration_test_data)
    unique_email = reg.registration_signup_email(registration_test_data)
    logger.info("Registered email: %s", unique_email)

    reg.registration_signup_phone_number_country_india(registration_test_data)
    reg.registration_signup_phone_number_india(registration_test_data)
    reg.registration_signup_agreed_to_policy_chkbx(registration_test_data)
    reg.registration_signup_submit_btn(registration_test_data)
    logger.info("Signup form submitted.")

    # ── Step 3: OTP verification ───────────────────────────────────────────
    time.sleep(10)
    otp = get_latest_otp_email()
    reg.registration_enter_otp(otp)
    logger.info("OTP entered: %s", otp)
    time.sleep(2)

    # ── Step 4: Password setup ─────────────────────────────────────────────
    reg.registration_enter_password(registration_test_data)
    reg.registration_next_btn()
    time.sleep(5)
    logger.info("Password set and Next clicked.")

    # ── Step 5: Login with new credentials ────────────────────────────────
    login.enter_username(unique_email)
    login.enter_password(registration_test_data["registration_password"])
    login.click_loginbutton()
    time.sleep(5)
    logger.info("Logged in successfully.")

    # ── Step 6: Organisation details ──────────────────────────────────────
    reg.registration_organization_details_enter_company_name(registration_test_data)
    reg.registration_organization_address_india_inp(registration_test_data)
    reg.registration_next_btn()
    time.sleep(5)

    # ── Step 7: Pricing plan (Espresso – free) ─────────────────────────────
    reg.registration_pricing_plan_start_for_free_btn()
    reg.registration_pricing_plan_nxt_btn()
    reg.registration_pricing_plan_procd_btn()
    time.sleep(20)
    logger.info("Pricing plan selected and proceeded.")

    # ── Step 8: Close ads popup ────────────────────────────────────────────
    reg.registration_organization_close_ads_popup()
    time.sleep(5)

    # ── Step 9: Persist registration to history ────────────────────────────
    record = tracker.add_registration(
        email=reg.captured_email,
        first_name=reg.captured_first_name,
        last_name=reg.captured_last_name,
    )
    logger.info(
        "Registration saved: email=%s, first_name=%s",
        record.email,
        record.first_name,
    )

    # ── Assertions ─────────────────────────────────────────────────────────
    assert record.email, "Registered email must not be empty."
    assert record.first_name, "Captured first name must not be empty."
    assert not tracker.needs_registration(), (
        "Tracker should report no new registration needed after saving."
    )

    logger.info("Registration test PASSED – history updated.")
