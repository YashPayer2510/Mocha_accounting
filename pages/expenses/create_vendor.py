import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.actions import Actions


class Create_Vendor:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 50)

    create_vendor_expense_mod = (By.XPATH,"//img[@src='/svgs/expense.svg']")
    create_vendor_vendor_sub_mod = (By.XPATH,"//a[normalize-space()='Vendors']")
    create_vendor_new_vendor_btn = (By.XPATH,"//a[@class='shadow-none me-3 btn btn-primary sc-dkPtRN cLEBPX']")
    create_vendor_inptxt_Title = (By.XPATH, "//input[@name='contact_infos.title']")
    create_vendor_inptxt_FirstName = (By.XPATH, "//input[@name='contact_infos.first_name']")
    create_vendor_inptxt_MiddleName = (By.XPATH, "//input[@name='contact_infos.middle_name']")
    create_vendor_inptxt_LastName = (By.XPATH, "//input[@name='contact_infos.last_name']")
    create_vendor_inptxt_CompanyName = (By.XPATH,"//input[@name='additional_infos.company_name']")
    create_vendor_inptxt_DisplayName = (By.XPATH, "//input[@name='contact_infos.display_name']")
    create_vendor_inptxt_Email = (By.XPATH,"//input[@label='Email']")
    create_vendor_inptxt_PhoneNumCountry = (By.XPATH, "//input[@label='Phone number']")
    create_vendor_dd_MobileNumber = (By.XPATH, "//div[@class='selected-flag']")
    create_vendor_options_MobileNumber = (By.XPATH, "//ul[@class='country-list ']//li//span[@class='country-name']")
    create_vendor_inpnum_MobileNumber = (By.XPATH,"//input[@placeholder='Enter phone number']")
    create_vendor_inpnum_Fax = (By.XPATH, "//input[@label='Fax']")
    create_vendor_inp_Other = (By.XPATH, "//input[@label='Other']")
    create_vendor_inp_Website = (By.XPATH,"//input[@label='Website']")
    create_vendor_inptxt_NameToPrintOnChecks = (By.XPATH, "//input[@name='contact_infos.name_on_checks']")
    create_vendor_dd_GSTTreatment = (By.XPATH,"//select[@label='GST treatment']")
    create_vendor_options_GSTTreatment =(By.XPATH,"//select[contains(@label,'GST treatment')]/option")
    create_vendor_inp_GSTnumber =(By.XPATH,"//input[@name='additional_infos.tax_number']")
    # Address
    create_vendor_btn_address_EnterManually = (By.XPATH,"//button[normalize-space()='Enter manually']")
    create_vendor_inp_address = (By.XPATH,"//label[contains(text(),'Address')]/following::input[@placeholder='Enter a location']")
    create_vendor_options_address = (By.XPATH, "/html/body/div[2]")
    create_vendor_dd_address_country = (By.XPATH,"//select[@label='Country']")
    create_vendor_options_country = (By.XPATH, "//label[contains(text(),'Country')]/following::select[contains(@label,'Country')]/option")
    create_vendor_dd_State = (By.XPATH,"//label[text()='State']/following-sibling::select//option")
    create_venddor_options_state = (By.XPATH,"//label[text()='State']/following-sibling::select[1]//option")
    create_vendor_inp_City = (By.XPATH, "//input[@label='City']")
    create_vendor_inp_Zip = (By.XPATH, "//input[@label='Zip']")
    create_vendor_inp_Note = (By.XPATH,"//textarea[@placeholder='Notes']")
    create_vendor_dd_CreditTerms = (By.XPATH, "//label[text()='Credit Terms*']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    create_vendor_options_creditterms = (By.XPATH, "//div[contains(@class, 'option')]")
    create_vendor_accounts = (By.XPATH,"//input[@label='Account no.']")
    create_vendor_dd_default_exp_acc = (By.ID,"//label[text()='Default expense account']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    create_vendor_options_default_exp_acc = (By.XPATH,"//div[contains(@class, 'option')]")
    create_vendor_btn_Cancel = (By.XPATH, "//a[contains(@class,'sc-eeDRCY eMmKiS text-white')]")
    create_vendor_btn_Clear = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[2]")
    create_vendor_btn_SaveandClose = (By.XPATH, "//button[@id='zoom-primary-cancel-btn']")
    create_vendor_btn_SaveandNew = (By.XPATH, "//button[@id='zoom-primary-btn']")

    create_vendor_dd_list_vendorlist = (By.XPATH, "//table//tr//td[1]")
    create_vendor_dd_btn_nxt_vendorlist = (By.XPATH, "//a[normalize-space()='>']")


    def create_vendor_mod_expense(self):
        self.actions.wait_for_element(self.create_vendor_expense_mod)
        self.actions.click(self.create_vendor_expense_mod)
        time.sleep(2)

    def create_vendor_submod_vendor(self):
        self.actions.wait_for_element(self.create_vendor_vendor_sub_mod)
        self.actions.click(self.create_vendor_vendor_sub_mod)
        time.sleep(2)


    def create_vendor_new_vendor(self):
        self.actions.wait_for_element(self.create_vendor_new_vendor_btn)
        self.actions.click(self.create_vendor_new_vendor_btn)
        time.sleep(2)


    def create_vendor_title(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_inptxt_Title)
        self.actions.send_keys(self.create_vendor_inptxt_Title, create_vendor_test_data["vendor_title"])
        time.sleep(3)


    def create_vendor_firstname(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_inptxt_FirstName)
        self.actions.send_keys(self.create_vendor_inptxt_FirstName, create_vendor_test_data["vendor_first_name"])
        time.sleep(2)


    def create_vendor_middlename(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_inptxt_MiddleName)
        self.actions.send_keys(self.create_vendor_inptxt_MiddleName, create_vendor_test_data["vendor_middle_name"])
        time.sleep(2)


    def create_vendor_lastname(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_inptxt_LastName)
        self.actions.send_keys(self.create_vendor_inptxt_LastName, create_vendor_test_data["vendor_last_name"])
        time.sleep(2)


    def create_vendor_companyname(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_inptxt_CompanyName)
        self.actions.send_keys(self.create_vendor_inptxt_CompanyName, create_vendor_test_data["vendor_company_name"])
        time.sleep(2)


    def create_vendor_displayname(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_inptxt_DisplayName)
        self.actions.send_keys(self.create_vendor_inptxt_DisplayName, create_vendor_test_data["vendor_display_name"])
        time.sleep(2)


    def create_vendor_email(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_inptxt_Email)
        self.actions.send_keys(self.create_vendor_inptxt_Email, create_vendor_test_data["vendor_email"])
        time.sleep(2)

    def create_vendor_phonenumber(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_inptxt_PhoneNumCountry)
        self.actions.scroll_to_the_element(self.create_vendor_inptxt_PhoneNumCountry)
        self.actions.send_keys(self.create_vendor_inptxt_PhoneNumCountry, create_vendor_test_data["vendor_phone_number"])
        time.sleep(2)

    def create_vendor_mobile_numcountry(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_dd_MobileNumber)
        self.actions.dropdown_no_inp(self.create_vendor_dd_MobileNumber, self.create_vendor_options_MobileNumber, create_vendor_test_data["vendor_mobile_num_country"])
        time.sleep(2)

    def create_vendor_mobile_number(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_inpnum_MobileNumber)
        self.actions.send_keys(self.create_vendor_inpnum_MobileNumber, create_vendor_test_data["vendor_mobile_number"])
        time.sleep(2)

    def create_vendor_fax(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_inpnum_Fax)
        self.actions.send_keys(self.create_vendor_inpnum_Fax, create_vendor_test_data["vendor_fax"])
        time.sleep(2)

    def create_vendor_other(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_inp_Other)
        self.actions.send_keys(self.create_vendor_inp_Other, create_vendor_test_data["vendor_other"])
        time.sleep(2)

    def create_vendor_website(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_inp_Website)
        self.actions.send_keys(self.create_vendor_inp_Website, create_vendor_test_data["vendor_website"])
        time.sleep(2)

    def create_vendor_nametoprintoncheck(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_inptxt_NameToPrintOnChecks)
        self.actions.send_keys(self.create_vendor_inptxt_NameToPrintOnChecks, create_vendor_test_data["vendor_name_to_print_on_check"])
        time.sleep(2)

    def create_vendor_gsttreatment(self,create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_dd_GSTTreatment)
        self.actions.dropdown_equals(self.create_vendor_dd_GSTTreatment,self.create_vendor_options_GSTTreatment,create_vendor_test_data["vendor_gst_treatment"] )
        time.sleep(2)

    def create_vendor_gstnumber(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_inp_GSTnumber)
        self.actions.send_keys(self.create_vendor_inp_GSTnumber, create_vendor_test_data["vendor_gst_number"])
        time.sleep(2)

    def create_vendor_address_entermanually(self):
        self.actions.wait_for_element(self.create_vendor_btn_address_EnterManually)
        self.actions.scroll_to_the_element(self.create_vendor_btn_address_EnterManually)
        self.actions.click(self.create_vendor_btn_address_EnterManually)
        time.sleep(2)

    def create_vendor_address(self,create_vendor_test_data):
        self.actions.scroll_to_the_element(self.create_vendor_inp_address)
        self.actions.wait_for_element(self.create_vendor_inp_address)
        #self.actions.click_with_retry(self.inp_Billing)
        self.actions.dropdown_contains(self.create_vendor_inp_address,self.create_vendor_options_address, create_vendor_test_data["vendor_address"] )
        #self.actions.click(self.inp_Billing)
        #self.actions.send_keys(self.inp_Billing, test_data["billing"])
        time.sleep(2)

    def create_vendor_addresscountry(self,create_vendor_test_data):
        self.actions.scroll_to_the_element(self.create_vendor_dd_address_country)
        self.actions.wait_for_element(self.create_vendor_dd_address_country)
        self.actions.dropdown_equals(self.create_vendor_dd_address_country,self.create_vendor_options_country, create_vendor_test_data["vendor_country"] )

    def create_vendor_addressstate(self,create_vendor_test_data):
        self.actions.scroll_to_the_element(self.create_vendor_dd_State)
        self.actions.wait_for_element(self.create_vendor_dd_State)
        self.actions.dropdown_equals(self.create_vendor_dd_State,self.create_venddor_options_state, create_vendor_test_data["vendor_state"] )

    def create_vendor_addresscity(self, create_vendor_test_data):
        self.actions.scroll_to_the_element(self.create_vendor_inp_City)
        self.actions.wait_for_element(self.create_vendor_inp_City)
        self.actions.send_keys(self.create_vendor_inp_City, create_vendor_test_data["vendor_city"])

    def create_vendor_addresszip(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_inp_Zip)
        self.actions.send_keys(self.create_vendor_inp_Zip, create_vendor_test_data["vendor_zip"])

    def create_vendor_note(self, create_vendor_test_data):
        self.actions.scroll_to_the_element(self.create_vendor_inp_Note)
        self.actions.wait_for_element(self.create_vendor_inp_Note)
        self.actions.send_keys(self.create_vendor_inp_Note, create_vendor_test_data["vendor_note"])

    def create_vendor_creditterms(self, create_vendor_test_data):
        self.actions.scroll_to_the_element(self.create_vendor_dd_CreditTerms)
        self.actions.wait_for_element(self.create_vendor_dd_CreditTerms)
        self.actions.dropdown_equals(self.create_vendor_dd_CreditTerms, self.create_vendor_options_creditterms, create_vendor_test_data["vendor_credit_terms"])

    def create_vendor_account(self, create_vendor_test_data):
        self.actions.wait_for_element(self.create_vendor_accounts)
        self.actions.send_keys(self.create_vendor_accounts, create_vendor_test_data["vendor_account"])

    def create_vendor_default_account(self, create_vendor_test_data):
        self.actions.scroll_to_the_element(self.create_vendor_dd_default_exp_acc)
        self.actions.wait_for_element(self.create_vendor_dd_default_exp_acc)
        self.actions.dropdown_equals(self.create_vendor_dd_default_exp_acc, self.create_vendor_options_default_exp_acc, create_vendor_test_data["vendor_default_expense_account"])

    def create_vendor_cancel(self):
        self.actions.scroll_to_the_element(self.create_vendor_btn_Cancel)
        self.actions.wait_for_element(self.create_vendor_btn_Cancel)
        self.actions.click(self.create_vendor_btn_Cancel)

    def create_vendor_clear(self, test_data):
        self.actions.scroll_to_the_element(self.create_vendor_btn_Clear)
        self.actions.wait_for_element(self.create_vendor_btn_Clear)
        self.actions.click(self.create_vendor_btn_Clear)
        time.sleep(4)

    def create_vendor_saveandclose(self):
        self.actions.scroll_to_the_element(self.create_vendor_btn_SaveandClose)
        self.actions.wait_for_element(self.create_vendor_btn_SaveandClose)
        self.actions.click(self.create_vendor_btn_SaveandClose)
        time.sleep(3)

    def create_vendor_saveandnew(self,test_data):
        self.actions.scroll_to_the_element(self.create_vendor_btn_SaveandNew)
        self.actions.wait_for_element(self.create_vendor_btn_SaveandNew)
        self.actions.click(self.create_vendor_btn_SaveandNew)
        time.sleep(3)


    def create_vendor_saved_successfully(self, create_vendor_test_data):
        expected_vendor = create_vendor_test_data["vendor_display_name"]
        name_found = False

        while True:
            # Wait for the product list to be visible
            self.actions.wait_for_element(self.create_vendor_dd_list_vendorlist)
            product_list = self.driver.find_elements(*self.create_vendor_dd_list_vendorlist)

            # Loop through product names on current page
            for product in product_list:
                if product.text.strip().lower() == expected_vendor.strip().lower():
                    print(f"✅ Match found: {expected_vendor}")
                    name_found = True
                    break

            if name_found:
                break

            # Handle pagination
            try:
                self.actions.scroll_to_the_element(self.create_vendor_dd_btn_nxt_vendorlist)
                next_btn = self.driver.find_element(*self.create_vendor_dd_btn_nxt_vendorlist)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    print(f"ℹ️ Reached end of pagination. '{next_btn}' not found.")
                    break

                next_btn.click()

                # Wait until new content loads
                self.wait.until(EC.staleness_of(product_list[0]))
                self.wait.until(EC.presence_of_all_elements_located(self.create_vendor_dd_list_vendorlist))

            except NoSuchElementException:
                print("✅ No 'Next' button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        if not name_found:
            print(f"❌ Customer '{expected_vendor}' not found.")
