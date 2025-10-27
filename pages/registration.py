import logging
import time
import datetime
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.actions import Actions
REGISTRATION_EMAIL = None
class Registration:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 50)

    registration_sign_up_btn = (By.XPATH,"//button[contains(@class,'whitespace-nowrap')][normalize-space()='Sign Up for Free']")
    registration_first_name = (By.XPATH,"//input[@id='first_name']")
    registration_last_name = (By.XPATH, "//input[@id='last_name']")
    registration_email_id = (By.XPATH, "//input[@id='email']")
    registration_dd_PhoneNumCountry = (By.XPATH, "//div[@class='selected-flag']")
    registration_options_PhoneNumCountry = (By.XPATH, "//ul[@class='country-list ']//li//span[@class='country-name']")
    registration_PhoneNumber = (By.XPATH,"//input[@placeholder='Enter phone number']")
    registration_checkbox_agreeToPolicy = (By.XPATH,"//input[@name='agreeToPolicy']")
    registration_submit_btn = (By.XPATH,"//button[@type='submit']")
    registration_otp_input = (By.XPATH, "//input[@id='verification_code']")
    registration_otp_submit_btn = (By.XPATH, "//button[@type='submit']")
    registration_password = (By.XPATH,"//input[@id='password']")
    registration_confirm_password = (By.XPATH, "//input[@id='confirmPassword']")
    registration_next_button = (By.XPATH,"//button[normalize-space(text())='Next']")
    registration_organization_details_org_name = (By.XPATH,"//input[@placeholder='Organization Name']")
    registration_organization_details_org_lgl_name = (By.XPATH,"//input[@placeholder='Organization Legal Name']")
    registration_organization_details_org_email_name = (By.XPATH,"//input[@placeholder='Organization Email']")
    registration_organization_details_btn_address_EnterManually = (By.XPATH,"//div[@type='button']")
    registration_organization_details_inp_address = (By.XPATH, "//input[@placeholder='Enter a Location']")
    registration_organization_details_inp_address_manually = (By.XPATH,"//div[@class='mb-1']//input[@type='text']")
    registration_organization_details_options_address = (By.XPATH, "/html/body/div[2]")
    registration_organization_details_dd_address_Country = (By.XPATH,"//label[normalize-space()='Country : *']/following-sibling::select")
    registration_organization_details_options_address_country = (By.XPATH, "//label[normalize-space()='Country : *']/following-sibling::select//option")
    registration_organization_details_address_State = (By.XPATH,"//label[normalize-space()='State : *']/following-sibling::select")
    registration_organization_details_options_address_state = (By.XPATH, "//label[normalize-space()='State : *']/following-sibling::select//option")
    registration_organization_details_inp_city = (By.XPATH,"//input[contains(@placeholder,'City')]")
    registration_organization_details_inp_zip = (By.XPATH, "//input[@placeholder='Zip']")
    registration_organization_details_inp_website= (By.XPATH,"//input[@placeholder='Website']")
    registration_organization_details_inp_industry= (By.XPATH,"//input[contains(@id,'react-select') and @type='text' and @role='combobox']")
    registration_organization_details_inp_options_industry = (By.XPATH,"//div[contains(@id, 'option')]")
    registration_organization_phone = (By.XPATH,"//input[@placeholder='Organization Phone Number']")
    registration_account_details_base_currency = (By.XPATH,"//input[@placeholder='USD or United...']")
    registration_account_details_options_base_currency = (By.XPATH, "//ul[contains(@role, 'listbox')]//li")
    registration_account_details_first_month_of_financial_year = (By.XPATH,"//select[contains(@name,'month_Of_financial_year')]")
    registration_account_details_option_first_month_of_financial_year = (By.XPATH,"//select[contains(@name,'month_Of_financial_year')]//option")
    registration_account_details_first_month_of_tax_year = (By.XPATH, "//select[@name='first_month_Of_tax_year']")
    registration_account_details_option_first_month_of_tax_year = (By.XPATH, "//select[@name='first_month_Of_tax_year']//option")
    registration_account_details_report_basis = (By.XPATH, "//select[@name='accounting_method']")
    registration_account_details_option_report_basis = (By.XPATH, "//select[@name='accounting_method']//option")
    registration_account_details_date_closing_of_books= (By.XPATH, "//input[@id='closing_date']")
    registration_account_details_datepicker_month_class = (By.CLASS_NAME, "react-datepicker__current-month")
    registration_account_details_next_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--next")
    registration_account_details_prev_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--previous")
    registration_account_details_back_btn = (By.XPATH,"//button[normalize-space()='Back']")
    registration_other_preferences_language_dd = (By.XPATH,"//select[contains(@name,'language')]")
    registration_other_preferences_options_language_dd = (By.XPATH,"//select[contains(@name,'language')]/option")
    registration_other_preferences_date_format_dd = (By.XPATH,"//select[@name='op_date_formate']")
    registration_other_preferences_options_date_format_dd = (By.XPATH,"//select[@name='op_date_formate']/option")
    registration_other_preferences_currency_format_dd = (By.XPATH,"//select[@name='currency_format']")
    registration_other_preferences_options_currency_format_dd = (By.XPATH,"//select[@name='currency_format']/option")
    registration_other_preferences_time_zone_dd = (By.XPATH, "//select[@name='time_zone']")
    registration_other_preferences_options_time_zone_dd = (By.XPATH, "//select[@name='time_zone']/option")
    registration_other_preferences_time_format_dd = (By.XPATH, "//select[contains(@name,'time_format')]")
    registration_other_preferences_options_time_format_dd = (By.XPATH, "//select[@name='time_format']/option")
    registration_tax_legal_organization_id = (By.XPATH,"//input[@name='businessId']")
    registration_tax_legal_tax_form_dd = (By.XPATH,"//label[text()='Tax Form :']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    registration_tax_legal_options_tax_form_dd = (By.XPATH,"//div[contains(@class, 'option')]")
    registration_tax_legal_gst_treatment_dd = (By.XPATH,"/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/input")
    registration_tax_legal_options_gst_treatment_dd = (By.XPATH, "//div[contains(@class, 'option')]")
    registration_tax_legal_tax_no = (By.XPATH,"//input[@name='gstin']")
    registration_tax_legal_submit_btn = (By.XPATH,"//button[normalize-space()='Submit']")
    registration_org_name_txt = (By.XPATH,"//p[@class='bg-white text-dark d-none d-md-flex m-0 p-2']")
    mobile_app_popup_x_btn = (By.XPATH, "//div[@title='Close' and text()='×']")
    registration_choose_mocha_product_accounting_btn = (By.XPATH,"//img[@src='images/logos/mocha-accounting.svg']")
    registration_choose_mocha_product_manage_btn = (By.XPATH,"//img[@src='images/logos/mocha-manage.svg']")
    registration_kickstart_your_journey_popup_setup_btn = (By.XPATH,"//button[@class= 'swal2-confirm swal2-styled']")
    registration_kickstart_your_journey_popup_later_btn = (By.XPATH,"//button[@class= 'swal2-cancel swal2-styled']")
    registration_tax_legal_einssn_dd = (By.XPATH,"//input[@name='einSsn[0]']")
    registration_tax_legal_add_more_tax_id = (By.XPATH,"//span[normalize-space()='+ Add more Tax ID']")


    def registration_signup_sign_up_btn(self):
        self.actions.wait_for_element(self.registration_sign_up_btn)
        self.actions.click(self.registration_sign_up_btn)

    def registration_signup_first_name(self, registration_test_data):
        self.actions.wait_for_element(self.registration_first_name)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")  # e.g., 20250709_154500
        unique_first_name = f"{registration_test_data['registration_first_name']}_FN_{timestamp}"
        self.actions.send_keys(self.registration_first_name, unique_first_name)
        logging.info(f"Entered First Name: {unique_first_name}")
        time.sleep(2)

    def registration_signup_last_name(self, registration_test_data):
        self.actions.wait_for_element(self.registration_last_name)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_last_name = f"{registration_test_data['registration_last_name']}_LN_{timestamp}"
        self.actions.send_keys(self.registration_last_name, unique_last_name)
        logging.info(f"Entered Last Name: {unique_last_name}")
        time.sleep(2)

    def registration_signup_email(self, registration_test_data):
        self.actions.wait_for_element(self.registration_email_id)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.unique_email_id = f"{registration_test_data['registration_email_id']}+{timestamp}@gmail.com"
        self.actions.send_keys(self.registration_email_id, self.unique_email_id)
        time.sleep(2)
        return self.unique_email_id

    def registration_signup_phone_number_country(self, registration_test_data):
        self.actions.wait_for_element(self.registration_dd_PhoneNumCountry)
        self.actions.dropdown_no_inp(self.registration_dd_PhoneNumCountry, self.registration_options_PhoneNumCountry, registration_test_data["registration_phone_number_country"])

    def registration_signup_phone_number(self, registration_test_data):
        self.actions.wait_for_element(self.registration_dd_PhoneNumCountry)
        base_number = str(registration_test_data["registration_phone_number"])
        suffix = datetime.datetime.now().strftime("%H%M%S")[-4:]  # e.g., "1545"
        unique_number = f"{base_number}{suffix}"
        self.actions.send_keys(self.registration_PhoneNumber,unique_number)

    def registration_signup_agreed_to_policy_chkbx(self, registration_test_data):
        self.actions.wait_for_element(self.registration_checkbox_agreeToPolicy)
        self.actions.click(self.registration_checkbox_agreeToPolicy)

    def registration_signup_submit_btn(self, registration_test_data):
        self.actions.wait_for_element(self.registration_submit_btn)
        self.actions.click(self.registration_submit_btn)

    def registration_enter_otp(self, otp):
        """
           Enter the OTP into the registration page and submit.
           :param otp: The 6-digit OTP string to be entered.
           """
        logging.info(f"Using OTP: {otp}")
        self.actions.wait_for_element(self.registration_otp_input)
        self.actions.send_keys(self.registration_otp_input, otp)

        self.actions.wait_for_element(self.registration_otp_submit_btn)
        self.actions.click(self.registration_otp_submit_btn)
        logging.info("OTP submitted successfully.")

    def registration_enter_password(self, registration_test_data):
        self.actions.wait_for_element(self.registration_password)
        self.actions.send_keys(self.registration_password,registration_test_data["registration_password"])
        self.actions.wait_for_element(self.registration_confirm_password)
        self.actions.send_keys(self.registration_confirm_password, registration_test_data["registration_confirm_password"])

    def registration_next_btn(self):
        self.actions.wait_for_element(self.registration_next_button)
        self.actions.click(self.registration_next_button)

    def registration_organization_details_enter_org_name(self, registration_test_data):
        self.actions.wait_for_element(self.registration_organization_details_org_name)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.unique_org_name = f"{registration_test_data['organization_name']}_{timestamp} pvt. ltd."
        self.actions.send_keys(self.registration_organization_details_org_name,self.unique_org_name)

    def registration_organization_details_enter_org_lgl_name(self, registration_test_data):
        self.actions.wait_for_element(self.registration_organization_details_org_lgl_name)
        self.actions.send_keys(self.registration_organization_details_org_lgl_name, registration_test_data["organization_legal_name"])

    def registration_organization_org_email(self, registration_test_data):
        self.actions.wait_for_element(self.registration_organization_details_org_email_name)
        self.actions.send_keys(self.registration_organization_details_org_email_name, self.unique_email_id )

    def registration_organization_address_entermanually(self):
        self.actions.wait_for_element(self.registration_organization_details_btn_address_EnterManually)
        self.actions.scroll_to_the_element(self.registration_organization_details_btn_address_EnterManually)
        self.actions.click(self.registration_organization_details_btn_address_EnterManually)
        time.sleep(2)

    def registration_organization_address_inp(self,registration_test_data):
        self.actions.scroll_to_the_element(self.registration_organization_details_inp_address)
        self.actions.wait_for_element(self.registration_organization_details_inp_address)
        #self.actions.click_with_retry(self.inp_Billing)
        self.actions.dropdown_contains(self.registration_organization_details_inp_address,self.registration_organization_details_options_address, registration_test_data["organization_address"] )
        #self.actions.click(self.inp_Billing)
        #self.actions.send_keys(self.inp_Billing, test_data["billing"])
        time.sleep(2)

    def registration_organization_address_inp_manually(self, registration_test_data):
        self.actions.scroll_to_the_element(self.registration_organization_details_inp_address_manually)
        self.actions.wait_for_element(self.registration_organization_details_inp_address_manually)
        self.actions.send_keys(self.registration_organization_details_inp_address_manually, registration_test_data["organization_address"])


    def registration_organization_address_country(self,registration_test_data):
        self.actions.scroll_to_the_element(self.registration_organization_details_dd_address_Country)
        self.actions.wait_for_element(self.registration_organization_details_dd_address_Country)
        self.actions.dropdown_contains(self.registration_organization_details_dd_address_Country,self.registration_organization_details_options_address_country, registration_test_data["organization_address_country"])

    def registration_organization_address_state(self,registration_test_data):
        self.actions.scroll_to_the_element(self.registration_organization_details_address_State)
        self.actions.wait_for_element(self.registration_organization_details_address_State)
        self.actions.dropdown_equals(self.registration_organization_details_address_State,self.registration_organization_details_options_address_state, registration_test_data["organization_address_state"] )

    def registration_organization_address_city(self, registration_test_data):
        self.actions.scroll_to_the_element(self.registration_organization_details_inp_city)
        self.actions.wait_for_element(self.registration_organization_details_inp_city)
        self.actions.send_keys(self.registration_organization_details_inp_city, registration_test_data["organization_address_city"])

    def  registration_organization_address_zip(self, registration_test_data):
        self.actions.wait_for_element(self.registration_organization_details_inp_zip)
        self.actions.send_keys(self.registration_organization_details_inp_zip, registration_test_data["organization_address_zip"])

    def registration_organization_website(self, registration_test_data):
        self.actions.wait_for_element(self.registration_organization_details_inp_website)
        self.actions.send_keys(self.registration_organization_details_inp_website,
                               registration_test_data["organization_website"])

    def registration_organization_industry(self, registration_test_data):
        self.actions.scroll_to_the_element(self.registration_organization_details_inp_industry)
        self.actions.wait_for_element(self.registration_organization_details_inp_industry)
        self.actions.dropdown_equals(self.registration_organization_details_inp_industry,self.registration_organization_details_inp_options_industry, registration_test_data["organization_industry"])

    def registration_organization_phone_no(self, registration_test_data):
        self.actions.wait_for_element(self.registration_organization_phone)
        self.actions.send_keys(self.registration_organization_phone,
                               registration_test_data["organization_phone"])


    def registration_organization_accounting_details_base_currency(self, registration_test_data):
        self.actions.scroll_to_the_element(self.registration_account_details_base_currency)
        self.actions.wait_for_element(self.registration_account_details_base_currency)
        self.actions.clear_text(self.registration_account_details_base_currency)
        self.actions.dropdown_contains(self.registration_account_details_base_currency,self.registration_account_details_options_base_currency,registration_test_data["organization_base_currency"])

    def registration_organization_accounting_details_first_month_of_financial_year(self, registration_test_data):
        self.actions.scroll_to_the_element(self.registration_account_details_first_month_of_financial_year)
        self.actions.wait_for_element(self.registration_account_details_first_month_of_financial_year)
        self.actions.dropdown_equals(self.registration_account_details_first_month_of_financial_year,self.registration_account_details_option_first_month_of_financial_year,registration_test_data["organization_first_month_of_financial_year"])

    def registration_organization_accounting_details_first_month_of_tax_year(self, registration_test_data):
        self.actions.scroll_to_the_element(self.registration_account_details_first_month_of_tax_year)
        self.actions.wait_for_element(self.registration_account_details_first_month_of_tax_year)
        self.actions.dropdown_equals(self.registration_account_details_first_month_of_tax_year,self.registration_account_details_option_first_month_of_tax_year,registration_test_data["organization_first_month_of_tax_year"])

    def registration_organization_accounting_details_report_basis(self, registration_test_data):
        self.actions.scroll_to_the_element(self.registration_account_details_report_basis)
        self.actions.wait_for_element(self.registration_account_details_report_basis)
        self.actions.dropdown_equals(self.registration_account_details_report_basis,self.registration_account_details_option_report_basis,registration_test_data["organization_report_basis"])


    def registration_organization_accounting_details_closing_of_books(self,registration_test_data):
        self.actions.scroll_to_the_element(self.registration_account_details_date_closing_of_books)
        self.actions.wait_for_element(self.registration_account_details_date_closing_of_books)
        self.actions.select_date(self.registration_account_details_date_closing_of_books, self.registration_account_details_datepicker_month_class, self.registration_account_details_next_btn_class, self.registration_account_details_prev_btn_class, registration_test_data["receive_payment_date"])


    def registration_organization_accounting_details_back_btn(self):
        self.actions.wait_for_element(self.registration_account_details_back_btn)
        self.actions.scroll_to_the_element(self.registration_account_details_back_btn)
        self.actions.click(self.registration_account_details_back_btn)
        time.sleep(2)

    def registration_organization_other_preference_language_dd(self, registration_test_data):
        self.actions.scroll_to_the_element(self.registration_other_preferences_language_dd)
        self.actions.wait_for_element(self.registration_other_preferences_language_dd)
        self.actions.dropdown_equals(self.registration_other_preferences_language_dd,self.registration_other_preferences_options_language_dd,registration_test_data["organization_language"])

    def registration_organization_other_preference_date_format_dd(self, registration_test_data):
        self.actions.scroll_to_the_element(self.registration_other_preferences_date_format_dd)
        self.actions.wait_for_element(self.registration_other_preferences_date_format_dd)
        self.actions.dropdown_contains(self.registration_other_preferences_date_format_dd,self.registration_other_preferences_options_date_format_dd,registration_test_data["organization_date_format"])

    def registration_organization_other_preference_currency_format_dd(self, registration_test_data):
        self.actions.scroll_to_the_element(self.registration_other_preferences_currency_format_dd)
        self.actions.wait_for_element(self.registration_other_preferences_currency_format_dd)
        self.actions.dropdown_contains(self.registration_other_preferences_currency_format_dd,self.registration_other_preferences_options_currency_format_dd,registration_test_data["organization_currency_format"])

    def registration_organization_other_preference_time_zone_dd(self, registration_test_data):
        self.actions.scroll_to_the_element(self.registration_other_preferences_time_zone_dd)
        self.actions.wait_for_element(self.registration_other_preferences_time_zone_dd)
        self.actions.dropdown_contains(self.registration_other_preferences_time_zone_dd,self.registration_other_preferences_options_time_zone_dd,registration_test_data["organization_time_zone"])

    def registration_organization_other_preference_time_format_dd(self, registration_test_data):
        self.actions.scroll_to_the_element(self.registration_other_preferences_time_format_dd)
        self.actions.wait_for_element(self.registration_other_preferences_time_format_dd)
        self.actions.dropdown_contains(self.registration_other_preferences_time_format_dd,self.registration_other_preferences_options_time_format_dd,registration_test_data["organization_time_format"])

    def registration_organization_tax_legal_organization_id(self,registration_test_data):
        self.actions.scroll_to_the_element(self.registration_tax_legal_organization_id)
        self.actions.wait_for_element(self.registration_tax_legal_organization_id)
        self.actions.send_keys(self.registration_tax_legal_organization_id,registration_test_data["organization_organization_id"])

    def registration_organization_tax_legal_tax_form_dd(self, registration_test_data):
        self.actions.scroll_to_the_element(self.registration_tax_legal_tax_form_dd)
        self.actions.wait_for_element(self.registration_tax_legal_tax_form_dd)
        self.actions.dropdown_contains(self.registration_tax_legal_tax_form_dd, self.registration_tax_legal_options_tax_form_dd, registration_test_data["organization_tax_form"] )

    def registration_organization_tax_legal_gst_treatment_dd(self, registration_test_data):
        self.actions.scroll_to_the_element(self.registration_tax_legal_gst_treatment_dd)
        self.actions.wait_for_element(self.registration_tax_legal_gst_treatment_dd)
        self.actions.dropdown_equals(self.registration_tax_legal_gst_treatment_dd,self.registration_tax_legal_options_gst_treatment_dd, registration_test_data["organization_gst_treatment"])

    def registration_organization_tax_legal_tax_no(self,registration_test_data):
        self.actions.scroll_to_the_element(self.registration_tax_legal_tax_no)
        self.actions.wait_for_element(self.registration_tax_legal_tax_no)
        self.actions.send_keys(self.registration_tax_legal_tax_no, registration_test_data["organization_tax_no"])

    def registration_organization_tax_legal_submit_btn(self):
        self.actions.wait_for_element(self.registration_tax_legal_submit_btn)
        self.actions.scroll_to_the_element(self.registration_tax_legal_submit_btn)
        self.actions.click(self.registration_tax_legal_submit_btn)

    def registration_organization_close_ads_popup(self):
        self.actions.wait_for_element(self.mobile_app_popup_x_btn)
        self.actions.click(self.mobile_app_popup_x_btn)

    def registration_asset_given_org_name_and_displayed_org_name(self):
        self.actions.wait_for_element(self.registration_org_name_txt)
        displayed_org_name = self.actions.get_text(self.registration_org_name_txt)
        print(f"Displayed Organization: {displayed_org_name}")
        assert displayed_org_name == self.unique_org_name, f"Mismatch in given organization name with displayed organization name"

    def registration_organization_choose_mocha_product_accounting(self):
        self.actions.wait_for_element(self.registration_choose_mocha_product_accounting_btn)
        self.actions.click(self.registration_choose_mocha_product_accounting_btn)

    def registration_organization_choose_mocha_product_manage(self):
        self.actions.wait_for_element(self.registration_choose_mocha_product_manage_btn)
        self.actions.click(self.registration_choose_mocha_product_manage_btn)

    def registration_organization_kickstart_your_journey_popup_setup_btn(self):
        self.actions.wait_for_element(self.registration_kickstart_your_journey_popup_setup_btn)
        self.actions.click(self.registration_kickstart_your_journey_popup_setup_btn)

    def registration_organization_kickstart_your_journey_popup_later_btn(self):
        self.actions.wait_for_element(self.registration_kickstart_your_journey_popup_later_btn)
        self.actions.click(self.registration_kickstart_your_journey_popup_later_btn)

    def registration_organization_tax_legal_einssn (self,registration_test_data):
        self.actions.scroll_to_the_element(self.registration_tax_legal_einssn_dd)
        self.actions.wait_for_element(self.registration_tax_legal_einssn_dd)
        self.actions.send_keys(self.registration_tax_legal_einssn_dd, registration_test_data["organization_einssn_no"])





























