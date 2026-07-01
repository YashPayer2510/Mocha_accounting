import logging
import time
import datetime
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from actions.actions import Actions

class Payment_Gateway_Setup_Cashfree:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 50)


    pg_setup_setup_your_mocha_acc_popup_close = (By.XPATH,"//button[@aria-label='Close']")
    pg_setup_setup_your_mocha_acc_popup_skip_for_now_btn = (By.XPATH,"//button[normalize-space()='Skip For Now']")
    pg_setup_confirmation_popup_yes = (By.XPATH,"//button[normalize-space()='Yes, exit and finish later']")
    pg_setup_confirmation_popup_no = (By.XPATH,"//button[normalize-space()='NO, continue Account Setup now']")
    pg_setup_settings_gear_btn = (By.XPATH,"//a[@title='Settings']//*[name()='svg']")
    pg_setup_settings_integration_label= (By.XPATH, "//div[@class='card hover-grow']//h5//div[normalize-space()='Integration']")
    pg_setup_settings_integration_label_setup = (By.XPATH,"//span[normalize-space()='Setup']")
    pg_setup_settings_integration_cashfree_setup_btn = (By.XPATH,"(//p[contains(text(),'Accept payments via UPI, cards, wallets, and inter')]/following::button[normalize-space()='Setup'])[1]")
    pg_setup_settings_integration_cashfree_consent_checkbox = (By.XPATH,"//input[@type='checkbox']")
    pg_setup_settings_integration_cashfree_consent_cancel_btn = (By.XPATH,"//button[normalize-space()='Cancel']")
    pg_setup_settings_integration_cashfree_next_btn = (By.XPATH,"//button[normalize-space()='Next']")
    pg_setup_settings_integration_cashfree_consent_validation_msg = (By.XPATH,"//h3[@class='dialog-title']")
    pg_setup_settings_integration_cashfree_merchant_details_name = (By.XPATH,"//input[@placeholder='Name']")
    pg_setup_settings_integration_cashfree_merchant_details_name_req_validation = (By.XPATH,"//div[normalize-space()='Name is required']")
    pg_setup_settings_integration_cashfree_merchant_details_email = (By.XPATH,"//input[@name='email']")
    pg_setup_settings_integration_cashfree_merchant_details_email_req_validation = (By.XPATH,"//div[normalize-space()='Email is required']")
    pg_setup_settings_integration_cashfree_merchant_details_email_invalid_validation = (By.XPATH,"//div[normalize-space()='Invalid email']")
    pg_setup_settings_integration_cashfree_merchant_details_phone_no = (By.XPATH, "//input[@placeholder='Phone Number']")
    pg_setup_settings_integration_cashfree_merchant_details_phone_no_req_validation = (By.XPATH, "//div[normalize-space()='Phone number is required']")
    pg_setup_settings_integration_cashfree_merchant_details_phone_no_invalid_validation = (By.XPATH, "//div[normalize-space()='Phone number must be exactly 10 digits']")
    pg_setup_settings_integration_cashfree_merchant_details_pan = (By.XPATH, "//input[@name='merchant_pan']")
    pg_setup_settings_integration_cashfree_merchant_details_pan_req_validation = (By.XPATH, "//div[normalize-space()='PAN number is required']")
    pg_setup_settings_integration_cashfree_merchant_details_pan_invalid_validation = (By.XPATH, "//div[normalize-space()='PAN must be in format ABCDE1234F (5 letters, 4 numbers, 1 letter)']")
    pg_setup_settings_integration_cashfree_merchant_details_website = (By.XPATH, "//input[@name='website_url']")
    pg_setup_settings_integration_cashfree_merchant_details_website_req_validation = (By.XPATH, "//div[normalize-space()='Website URL is required']")
    pg_setup_settings_integration_cashfree_merchant_details_website_invalid_validation = (By.XPATH, "//div[normalize-space()='Invalid URL']")
    pg_setup_settings_integration_cashfree_back_btn = (By.XPATH, "//button[normalize-space()='Back']")
    pg_setup_settings_integration_cashfree_business_details_legal_name = (By.XPATH, "//input[@name='businessName']")
    pg_setup_settings_integration_cashfree_business_details_legal_name_req_validation = (By.XPATH, "//div[normalize-space()='Business name is required']")
    pg_setup_settings_integration_cashfree_business_details_type_dd = (By.XPATH,"//label[normalize-space(text())='Business Type']/following-sibling::div//input[contains(@id, 'react-select')]")
    pg_setup_settings_integration_cashfree_business_details_options_type_dd = (By.XPATH,"//div[contains(@class, 'option')]")
    pg_setup_settings_integration_cashfree_business_details_type_dd_req_validation = (By.XPATH, "//div[normalize-space()='Business type is required']")
    pg_setup_settings_integration_cashfree_business_details_category_dd = (By.XPATH,"//label[normalize-space(text())='Business Category']/following-sibling::div//input[contains(@id, 'react-select')]")
    pg_setup_settings_integration_cashfree_business_details_options_category_dd = (By.XPATH, "//div[contains(@class, 'option')]")
    pg_setup_settings_integration_cashfree_business_details_category_dd_req_validation = (By.XPATH, "//div[normalize-space()='Business category is required']")
    pg_setup_settings_integration_cashfree_business_details_subcategory_dd = (By.XPATH,"//label[normalize-space(text())='Business Sub-Category']/following-sibling::div//input[contains(@id, 'react-select')]")
    pg_setup_settings_integration_cashfree_business_details_options_subcategory_dd = (By.XPATH, "//div[contains(@class, 'option')]")
    pg_setup_settings_integration_cashfree_business_details_pan = (By.XPATH, "//input[@name='business_pan']")
    pg_setup_settings_integration_cashfree_business_details_pan_req_validation = (By.XPATH, "//div[normalize-space()='Business PAN is required']")
    pg_setup_settings_integration_cashfree_business_details_pan_invalid_validation = (By.XPATH, "//div[normalize-space()='Business PAN must be in format ABCDE1234F']")
    pg_setup_settings_integration_cashfree_business_details_gstin = (By.XPATH, "//input[@name='gstin']")
    pg_setup_settings_integration_cashfree_business_details_gstin_req_validation = (By.XPATH, "//div[normalize-space()='Business GSTIN is required']")
    pg_setup_settings_integration_cashfree_business_details_gstin_invalid_validation = (By.XPATH, "//div[normalize-space()='GSTIN must be a valid 15 character GST number']")
    pg_setup_settings_integration_cashfree_business_details_cin = (By.XPATH, "//input[@name='business_cin']")
    pg_setup_settings_integration_cashfree_business_details_cin_req_validation = (By.XPATH, "//div[normalize-space()='Business CIN is required']")
    pg_setup_settings_integration_cashfree_business_details_cin_invalid_validation = (By.XPATH, "//div[normalize-space()='CIN must be exactly 21 alphanumeric characters']")
    pg_setup_settings_integration_cashfree_business_details_address = (By.XPATH, "//input[@name='formatted_address']")
    pg_setup_settings_integration_cashfree_business_details_city = (By.XPATH, "//input[@name='locality']")
    pg_setup_settings_integration_cashfree_business_details_state = (By.XPATH, "//input[@name='administrative_area_level_1']")
    pg_setup_settings_integration_cashfree_business_details_zip = (By.XPATH, "//input[@name='postal_code']")
    pg_setup_settings_integration_cashfree_business_details_country = (By.XPATH, "//input[@name='country']")
    pg_setup_settings_integration_cashfree_bank_account_dd = (By.XPATH,"//label[normalize-space(text())='Bank Account']/following-sibling::div//input[contains(@id, 'react-select')]")
    pg_setup_settings_integration_cashfree_options_bank_account_dd = (By.XPATH,"//div[contains(@class, 'option')]")
    pg_setup_settings_integration_cashfree_bank_account_dd_req_validation = (By.XPATH,"//h3[@class='dialog-title']")
    pg_setup_settings_integration_cashfree_bank_account_type_dd = (By.XPATH,"//select[@name ='account_type']")
    pg_setup_settings_integration_cashfree_bank_account_type_dd_req_validation = (By.XPATH,"//h3[@class='dialog-title']")
    pg_setup_settings_integration_cashfree_options_bank_account_type_dd = (By.XPATH, "//select[@name ='account_type']//option")
    pg_setup_settings_integration_cashfree_bank_account_ifsc_code = (By.XPATH,"//input[@name='ifsc_code']")
    pg_setup_settings_integration_cashfree_bank_account_ifsc_code_req_validation = (By.XPATH, "//h3[@class='dialog-title']")


    def pgs_setup_your_mocha_acc_popup_close_btn(self):
        self.actions.wait_for_element(self.pg_setup_setup_your_mocha_acc_popup_close)
        self.actions.click(self.pg_setup_setup_your_mocha_acc_popup_close)

    def pgs_setup_your_mocha_acc_popup_skip_for_now_btn(self):
        self.actions.wait_for_element(self.pg_setup_setup_your_mocha_acc_popup_skip_for_now_btn)
        self.actions.click(self.pg_setup_setup_your_mocha_acc_popup_skip_for_now_btn)

    def pgs_confirmation_popup_yes(self):
        self.actions.wait_for_element(self.pg_setup_confirmation_popup_yes)
        self.actions.click(self.pg_setup_confirmation_popup_yes)

    def pgs_confirmation_popup_no(self):
        self.actions.wait_for_element(self.pg_setup_confirmation_popup_no)
        self.actions.click(self.pg_setup_confirmation_popup_no)

    def pgs_settings_gear_btn(self):
        self.actions.wait_for_element(self.pg_setup_settings_gear_btn)
        self.actions.click(self.pg_setup_settings_gear_btn)

    def pgs_settings_integration_label_hover(self):
        self.actions.wait_for_element(self.pg_setup_settings_integration_label)
        self.actions.hover_on_element(self.pg_setup_settings_integration_label)

    def pgs_settings_integration_label_setup_btn(self):
        self.actions.wait_for_element(self.pg_setup_settings_integration_label_setup)
        self.actions.click(self.pg_setup_settings_integration_label_setup)

    def pgs_settings_integration_cashfree_setup_btn(self):
        self.actions.wait_for_element(self.pg_setup_settings_integration_cashfree_setup_btn)
        self.actions.click(self.pg_setup_settings_integration_cashfree_setup_btn)

    def pgs_settings_integration_cashfree_consent_checkbox(self):
        self.actions.wait_for_element(self.pg_setup_settings_integration_cashfree_consent_checkbox)
        self.actions.click(self.pg_setup_settings_integration_cashfree_consent_checkbox)

    def pgs_settings_integration_cashfree_consent_cancel_btn(self):
        self.actions.wait_for_element(self.pg_setup_settings_integration_cashfree_consent_cancel_btn)
        self.actions.click(self.pg_setup_settings_integration_cashfree_consent_cancel_btn)

    def pgs_settings_integration_cashfree_next_btn(self):
        self.actions.wait_for_element(self.pg_setup_settings_integration_cashfree_next_btn)
        self.actions.click(self.pg_setup_settings_integration_cashfree_next_btn)

    def pgs_settings_integration_cashfree_verify_validation_without_consent_clicked(self, payment_gateway_setup_cashfree_test_data):
        actual_consent_validation_msg= self.actions.get_text(self.pg_setup_settings_integration_cashfree_consent_validation_msg)
        expected_consent_validation_msg = payment_gateway_setup_cashfree_test_data["consent_validation"]
        if self.actions.is_element_present(self.pg_setup_settings_integration_cashfree_consent_validation_msg):
            print("The validation is displayed")
            assert actual_consent_validation_msg == expected_consent_validation_msg, f"Validation message mismatch. Expected: '{expected_consent_validation_msg}', Got: '{actual_consent_validation_msg}'"
        else:
            assert False, "Validation message is NOT displayed when consent is not checked and Save is clicked."

    def pgs_settings_integration_cashfree_merchant_details_verify_validation_no_name(self,payment_gateway_setup_cashfree_test_data):
        self.actions.wait_for_element(self.pg_setup_settings_integration_cashfree_merchant_details_name)
        self.actions.clear_text(self.pg_setup_settings_integration_cashfree_merchant_details_name)

        actual_no_name_validation_msg = self.actions.get_text(self.pg_setup_settings_integration_cashfree_merchant_details_name_req_validation)
        expected_no_name_consent_validation_msg = payment_gateway_setup_cashfree_test_data["blank_name_validation"]
        if self.actions.is_element_present(self.pg_setup_settings_integration_cashfree_merchant_details_name_req_validation):
            print("The validation is displayed")
            assert actual_no_name_validation_msg == expected_no_name_consent_validation_msg, f"Validation message mismatch. Expected: '{expected_no_name_consent_validation_msg}', Got: '{actual_no_name_validation_msg}'"
        else:
            assert False, "Validation message is NOT displayed when name field is blank and next is clicked."

    def pgs_settings_integration_cashfree_merchant_details_verify_validation_no_email(self,payment_gateway_setup_cashfree_test_data):
        self.actions.wait_for_element(self.pg_setup_settings_integration_cashfree_merchant_details_email)
        self.actions.clear_text(self.pg_setup_settings_integration_cashfree_merchant_details_email)

        actual_no_email_validation_msg = self.actions.get_text(self.pg_setup_settings_integration_cashfree_merchant_details_email_req_validation)
        expected_no_email_consent_validation_msg = payment_gateway_setup_cashfree_test_data["blank_email_validation"]
        if self.actions.is_element_present(self.pg_setup_settings_integration_cashfree_merchant_details_email_req_validation):
            print("The validation is displayed")
            assert actual_no_email_validation_msg == expected_no_email_consent_validation_msg, f"Validation message mismatch. Expected: '{expected_no_email_consent_validation_msg}', Got: '{actual_no_email_validation_msg}'"
        else:
            assert False, "Validation message is NOT displayed when email field is blank and next is clicked."

    def pgs_settings_integration_cashfree_merchant_details_enter_valid_email(self,payment_gateway_setup_cashfree_test_data ):
        self.actions.wait_for_element(self.pg_setup_settings_integration_cashfree_merchant_details_email)
        self.actions.clear_text(self.pg_setup_settings_integration_cashfree_merchant_details_email)
        self.actions.send_keys(self.pg_setup_settings_integration_cashfree_merchant_details_email,payment_gateway_setup_cashfree_test_data["valid_email"])

    def pgs_settings_integration_cashfree_merchant_details_verify_validation_invalid_email(
            self, payment_gateway_setup_cashfree_test_data):

        invalid_emails = payment_gateway_setup_cashfree_test_data["invalid_email"]
        expected_msg = payment_gateway_setup_cashfree_test_data["invalid_email_validation"]

        for email in invalid_emails:
            print(f"Testing invalid email: {email}")

            self.actions.wait_for_element(self.pg_setup_settings_integration_cashfree_merchant_details_email)
            self.actions.clear_text(self.pg_setup_settings_integration_cashfree_merchant_details_email)
            self.actions.send_keys(
                self.pg_setup_settings_integration_cashfree_merchant_details_email,
                email
            )

            actual_msg = self.actions.get_text(
                self.pg_setup_settings_integration_cashfree_merchant_details_email_invalid_validation
            )

            if self.actions.is_element_present(
                    self.pg_setup_settings_integration_cashfree_merchant_details_email_invalid_validation):

                print(f"Validation displayed for: {email}")

                assert actual_msg == expected_msg, \
                    f"[{email}] Validation mismatch. Expected: '{expected_msg}', Got: '{actual_msg}'"

            else:
                assert False, f"[{email}] Validation NOT displayed for invalid email"


    def pgs_settings_integration_cashfree_merchant_details_verify_validation_no_phone_no(self,payment_gateway_setup_cashfree_test_data):
        self.actions.wait_for_element(self.pg_setup_settings_integration_cashfree_merchant_details_phone_no)
        self.actions.clear_text(self.pg_setup_settings_integration_cashfree_merchant_details_phone_no)

        actual_no_phone_no_validation_msg = self.actions.get_text(self.pg_setup_settings_integration_cashfree_merchant_details_phone_no_req_validation)
        expected_no_phone_no_consent_validation_msg = payment_gateway_setup_cashfree_test_data["blank_phone_no_validation"]
        if self.actions.is_element_present(self.pg_setup_settings_integration_cashfree_merchant_details_phone_no_req_validation):
            print("The validation is displayed")
            assert actual_no_phone_no_validation_msg == expected_no_phone_no_consent_validation_msg, f"Validation message mismatch. Expected: '{expected_no_phone_no_consent_validation_msg}', Got: '{actual_no_phone_no_validation_msg}'"
        else:
            assert False, "Validation message is NOT displayed when phone no field is blank and next is clicked."

    def pgs_settings_integration_cashfree_merchant_details_enter_valid_phone_no(self,payment_gateway_setup_cashfree_test_data ):
        self.actions.wait_for_element(self.pg_setup_settings_integration_cashfree_merchant_details_phone_no)
        self.actions.clear_text(self.pg_setup_settings_integration_cashfree_merchant_details_phone_no)
        self.actions.send_keys(self.pg_setup_settings_integration_cashfree_merchant_details_phone_no,payment_gateway_setup_cashfree_test_data["valid_phone_no"])

    def pgs_settings_integration_cashfree_merchant_details_verify_validation_invalid_phone_no(
            self, payment_gateway_setup_cashfree_test_data):

        invalid_phone_no = payment_gateway_setup_cashfree_test_data["invalid_phone_no"]
        expected_msg = payment_gateway_setup_cashfree_test_data["invalid_phone_no_validation"]

        for phone_no in invalid_phone_no:
            print(f"Testing invalid phone: {phone_no}")

            self.actions.wait_for_element(self.pg_setup_settings_integration_cashfree_merchant_details_phone_no)
            self.actions.clear_text(self.pg_setup_settings_integration_cashfree_merchant_details_phone_no)
            self.actions.send_keys(
                self.pg_setup_settings_integration_cashfree_merchant_details_phone_no,
                phone_no
            )

            actual_msg = self.actions.get_text(
                self.pg_setup_settings_integration_cashfree_merchant_details_phone_no_invalid_validation
            )

            if self.actions.is_element_present(
                    self.pg_setup_settings_integration_cashfree_merchant_details_phone_no_invalid_validation):

                print(f"Validation displayed for: {phone_no}")

                assert actual_msg == expected_msg, \
                    f"[{phone_no}] Validation mismatch. Expected: '{expected_msg}', Got: '{actual_msg}'"

            else:
                assert False, f"[{phone_no}] Validation NOT displayed for invalid phone number"


    def pgs_settings_integration_cashfree_merchant_details_verify_validation_no_pan(self,payment_gateway_setup_cashfree_test_data):
        self.actions.wait_for_element(self.pg_setup_settings_integration_cashfree_merchant_details_pan)
        self.actions.clear_text(self.pg_setup_settings_integration_cashfree_merchant_details_pan)

        actual_no_pan_validation_msg = self.actions.get_text(self.pg_setup_settings_integration_cashfree_business_details_pan_req_validation)
        expected_no_pan_consent_validation_msg = payment_gateway_setup_cashfree_test_data["blank_pan_validation"]
        if self.actions.is_element_present(self.pg_setup_settings_integration_cashfree_business_details_pan_req_validation):
            print("The validation is displayed")
            assert actual_no_pan_validation_msg == expected_no_pan_consent_validation_msg, f"Validation message mismatch. Expected: '{expected_no_pan_consent_validation_msg}', Got: '{actual_no_pan_validation_msg}'"
        else:
            assert False, "Validation message is NOT displayed when pan field is blank and next is clicked."

    def pgs_settings_integration_cashfree_merchant_details_enter_valid_pan(self,payment_gateway_setup_cashfree_test_data ):
        self.actions.wait_for_element(self.pg_setup_settings_integration_cashfree_business_details_pan)
        self.actions.clear_text(self.pg_setup_settings_integration_cashfree_business_details_pan)
        self.actions.send_keys(self.pg_setup_settings_integration_cashfree_business_details_pan,payment_gateway_setup_cashfree_test_data["valid_pan"])

    def pgs_settings_integration_cashfree_merchant_details_verify_validation_invalid_pan(
            self, payment_gateway_setup_cashfree_test_data):

        invalid_pan = payment_gateway_setup_cashfree_test_data["invalid_pan"]
        expected_msg = payment_gateway_setup_cashfree_test_data["invalid_pan_validation"]

        for pan in invalid_pan:
            print(f"Testing invalid pan: {pan}")

            self.actions.wait_for_element(self.pg_setup_settings_integration_cashfree_business_details_pan)
            self.actions.clear_text(self.pg_setup_settings_integration_cashfree_business_details_pan)
            self.actions.send_keys(
                self.pg_setup_settings_integration_cashfree_business_details_pan,
                pan
            )

            actual_msg = self.actions.get_text(
                self.pg_setup_settings_integration_cashfree_business_details_pan_invalid_validation
            )

            if self.actions.is_element_present(
                    self.pg_setup_settings_integration_cashfree_business_details_pan_invalid_validation):

                print(f"Validation displayed for: {pan}")

                assert actual_msg == expected_msg, \
                    f"[{pan}] Validation mismatch. Expected: '{expected_msg}', Got: '{actual_msg}'"

            else:
                assert False, f"[{pan}] Validation NOT displayed for invalid pan"

    def pgs_settings_integration_cashfree_merchant_details_verify_validation_no_website(self,payment_gateway_setup_cashfree_test_data):
        self.actions.wait_for_element(self.pg_setup_settings_integration_cashfree_merchant_details_website)
        self.actions.clear_text(self.pg_setup_settings_integration_cashfree_merchant_details_website)

        actual_no_website_validation_msg = self.actions.get_text(self.pg_setup_settings_integration_cashfree_merchant_details_website_req_validation)
        expected_no_website_consent_validation_msg = payment_gateway_setup_cashfree_test_data["blank_website_validation"]
        if self.actions.is_element_present(self.pg_setup_settings_integration_cashfree_merchant_details_website_req_validation):
            print("The validation is displayed")
            assert actual_no_website_validation_msg == expected_no_website_consent_validation_msg, f"Validation message mismatch. Expected: '{expected_no_website_consent_validation_msg}', Got: '{actual_no_website_validation_msg}'"
        else:
            assert False, "Validation message is NOT displayed when website field is blank and next is clicked."






























