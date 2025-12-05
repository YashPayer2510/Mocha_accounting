import time
from selenium.webdriver.support import expected_conditions as EC
import datetime
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from actions.actions import Actions


class CreateCustomer:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 4)


    btn_submodSales = (By.XPATH,"//img[@src='/svgs/sales.svg']")
    btn_submodCustomer = (By.XPATH,"//a[normalize-space()='Customers']")
    btn_newCustomer = (By.XPATH,"//a[normalize-space()='Create Customer']")
    inptxt_Title = (By.XPATH,"//input[@name='contact_infos.title']")
    inptxt_FirstName = (By.XPATH,"//input[@name='contact_infos.first_name']")
    inptxt_MiddleName = (By.XPATH,"//input[@name='contact_infos.middle_name']")
    inptxt_LastName = (By.XPATH,"//input[@name='contact_infos.last_name']")
    inptxt_CompanyName = (By.XPATH,"//input[@name='additional_infos.company_name']")
    inptxt_DisplayName = (By.XPATH,"//input[@name='contact_infos.display_name']")
    inptxt_Email = (By.XPATH,"//label[normalize-space()='Email']/following-sibling::input")
    dd_PhoneNumCountry = (By.XPATH,"//div[@class='selected-flag']")
    options_PhoneNumCountry = (By.XPATH,"//ul[@class='country-list ']//li//span[@class='country-name']")
    inpnum_PhoneNumber = (By.XPATH,"//input[@placeholder='Enter phone number']")
    inpnum_MobileNumber = (By.XPATH,"//label[normalize-space()='Mobile Number']/following-sibling::input")
    inpnum_Fax = (By.XPATH,"//label[normalize-space()='Fax']/following-sibling::input")
    inp_Other = (By.XPATH,"//input[@label='Other']")
    inp_Website = (By.XPATH,"//input[@label='Website']")
    inptxt_NameToPrintOnChecks = (By.XPATH,"//input[@name='contact_infos.name_on_checks']")
    dd_GSTTreatment = (By.XPATH,"//select[@label='GST treatment']")
    options_GSTTreatment =(By.XPATH,"//select[contains(@label,'GST treatment')]/option")
    inp_GSTnumber =(By.XPATH,"//input[@name='additional_infos.tax_number']")
    #Billing_Address
    btn_Billing_EnterManually = (By.XPATH,"//body//div[@id='root']//div[contains(@class,'body flex-grow-1 px-3 mb-5')]//div[contains(@class,'row')]//div[contains(@class,'row')]//div[contains(@class,'row')]//div[1]//div[1]//div[1]//div[1]//button[1]")
    inp_Billing = (By.XPATH,"//label[normalize-space(text())='Billing']/following-sibling::input[@placeholder='Enter a location']")
    options_billing = (By.XPATH,"/html/body/div[2]")
    dd_BillingCountry = (By.XPATH,"//body//div[@id='root']//div[contains(@class,'body flex-grow-1 px-3 mb-5')]//div[contains(@class,'row')]//div[contains(@class,'row')]//div[contains(@class,'row')]//div[1]//div[1]//div[2]//div[1]//div[1]//select[1]")
    options_billingcountry = (By.XPATH,"//label[contains(text(),'Billing')]/following::select[contains(@label,'Country')]/option")
    dd_BillingState = (By.XPATH,"//body/div[@id='root']/div/div[contains(@class,'layout-container d-flex')]/div[contains(@class,'wrapper d-flex flex-column flex-gorw-1 min-vh-100 full-width')]/div[contains(@class,'body flex-grow-1 px-3 mb-5')]/div[contains(@class,'container-fluid')]/form[contains(@class,'pb-5')]/div[contains(@class,'row')]/div[contains(@class,'row')]/div[contains(@class,'col-md-12 pb-5')]/div[contains(@class,'card sc-iGgWBj djagpQ shadow-none mb-3 addCustomerAddressTour')]/div[contains(@class,'card-body')]/div[contains(@class,'row')]/div[contains(@class,'col-md-6')]/div[contains(@class,'row')]/div[1]/div[1]/div[1]/select[1]")
    options_billingstate = (By.XPATH, "//label[text()='Billing']/following::label[text()='State']/following-sibling::select[1]//option")
    inp_BillingCity = (By.XPATH,"//body/div[@id='root']/div/div[contains(@class,'layout-container d-flex')]/div[contains(@class,'wrapper d-flex flex-column flex-gorw-1 min-vh-100 full-width')]/div[contains(@class,'body flex-grow-1 px-3 mb-5')]/div[contains(@class,'container-fluid')]/form[contains(@class,'pb-5')]/div[contains(@class,'row')]/div[contains(@class,'row')]/div[contains(@class,'col-md-12 pb-5')]/div[contains(@class,'card sc-iGgWBj djagpQ shadow-none mb-3 addCustomerAddressTour')]/div[contains(@class,'card-body')]/div[contains(@class,'row')]/div[contains(@class,'col-md-6')]/div[contains(@class,'row')]/div[2]/div[1]/div[1]/input[1]")
    inp_BillingZip = (By.XPATH,"//label[contains(text(),'Billing')]/following::input[@label='Zip'][1]")
    #Shipping_Address
    checkbx_SameasBilling = (By.XPATH,"//input[@id='bil_checkBox']")
    btn_Shipping_EnterManually = (By.XPATH,"//div[@class='card-body']//div[2]//div[1]//div[1]//div[1]//button[1]")
    inp_Shipping = (By.XPATH,"//label[normalize-space(text())='Shipping']/following-sibling::input[@placeholder='Enter a location']")
    options_shipping =(By.XPATH,"/html/body/div[3]")
    dd_ShippingCountry = (By.XPATH,"//div[@class='card-body']//div[2]//div[1]//div[2]//div[1]//div[1]//select[1]")
    options_shippingcountry= (By.XPATH,"//label[contains(text(),'Shipping')]/following::select[contains(@label,'Country')]/option")
    dd_ShippingState = (By.XPATH,"//div[contains(@class,'col-md-6')]//div//div[contains(@class,'row')]//select[contains(@aria-label,'Large select example')]")
    options_shippingstate = (By.XPATH,"//label[text()='Shipping']/following::label[text()='State']/following-sibling::select[1]//option")
    inp_ShippingCity = (By.XPATH,"//body//div[@id='root']//div[contains(@class,'col-md-6')]//div//div[contains(@class,'row')]//div[2]//div[1]//div[1]//input[1]")
    inp_ShippingZip = (By.XPATH,"//body//div[@id='root']//div[contains(@class,'col-md-6')]//div//div[contains(@class,'row')]//div[3]//div[1]//div[1]//input[1]")
    #Note
    inp_Note = (By.XPATH,"//textarea[contains(@aria-label,'With textarea')]")
    #Additional_Information
    dd_CustomerType = (By.XPATH,"//label[text()='Customer type']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    options_customertype = (By.XPATH,"//div[contains(@id, 'option')]")
    dd_Preferreddeliverymethod = (By.XPATH,"//label[text()='Preferred delivery method']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    options_preferreddeliverymethod = (By.XPATH, "//div[contains(@class, 'option')]")
    dd_PreferredPaymentMethod = (By.XPATH,"//label[text()='Preferred Payment Method']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    options_preferredpaymentmethod = (By.XPATH, "//div[contains(@class, 'option')]")
    dd_CreditTerms = (By.XPATH,"//label[text()='Credit Terms*']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    options_creditterms = (By.XPATH, "//div[contains(@class, 'option')]")
    btn_Cancel = (By.XPATH,"//a[contains(@class,'sc-eeDRCY eMmKiS text-white')]")
    btn_Clear = (By.XPATH,"//div[@class='expense-footer-btns']//div[1]//button[2]")
    btn_SaveandClose = (By.XPATH,"//button[@id='zoom-primary-cancel-btn']")
    btn_SaveandNew = (By.XPATH,"//button[@id='zoom-primary-btn']")
    alert_msg_1_close_X_btn = (By.XPATH,"//div[16]//div[1]//div[1]//button[1]")
    alert_msg_2_close_X_btn = (By.XPATH,"//div[17]//div[1]//div[1]//button[1]")
    alert_msg_3_close_X_btn = (By.XPATH,"//div[18]//div[1]//div[1]//button[1]")



    list_customerlist = (By.XPATH,"//*[@id='root']//table/tbody//a")
    btn_nxt_customerlist = (By.XPATH,"//a[normalize-space()='>']")




    def cust_submodsales(self):
        self.actions.wait_for_element(self.btn_submodSales)
        self.actions.click(self.btn_submodSales)
        time.sleep(2)

    def cust_submodCustomer(self):
        self.actions.wait_for_element(self.btn_submodCustomer)
        self.actions.click(self.btn_submodCustomer)
        time.sleep(2)


    def cust_newCustomer(self):
        self.actions.wait_for_element(self.btn_newCustomer)
        self.actions.click(self.btn_newCustomer)
        time.sleep(2)


    def cust_title(self, customer_data):
        self.actions.wait_for_element(self.inptxt_Title)
        self.actions.send_keys(self.inptxt_Title, customer_data["title"])
        time.sleep(3)


    def cust_firstname(self, customer_data):
        self.actions.wait_for_element(self.inptxt_FirstName)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")  # e.g., 20250709_154500
        self.unique_first_name = f"{customer_data['first_name']}_FN_{timestamp}"
        self.actions.send_keys(self.inptxt_FirstName, self.unique_first_name)
        time.sleep(2)


    def cust_middlename(self, customer_data):
        self.actions.wait_for_element(self.inptxt_MiddleName)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")  # e.g., 20250709_154500
        self.unique_middle_name = f"{customer_data['middle_name']}_MN_{timestamp}"
        self.actions.send_keys(self.inptxt_MiddleName, self.unique_middle_name)
        time.sleep(2)


    def cust_lastname(self, customer_data):
        self.actions.wait_for_element(self.inptxt_LastName)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")  # e.g., 20250709_154500
        self.unique_last_name = f"{customer_data['last_name']}_LN_{timestamp}"
        self.actions.send_keys(self.inptxt_LastName, self.unique_last_name)
        time.sleep(2)


    def cust_companyname(self, customer_data):
        self.actions.wait_for_element(self.inptxt_CompanyName)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")  # e.g., 20250709_154500
        self.unique_company_name = f"{customer_data['company_name']}_CN_{timestamp}"
        self.actions.send_keys(self.inptxt_CompanyName, self.unique_company_name)
        time.sleep(2)


    def cust_displayname(self):
        self.actions.wait_for_element(self.inptxt_DisplayName)
        #self.actions.send_keys(self.inptxt_DisplayName, customer_data['display_name'])
        time.sleep(2)
        self.displayed_display_name = self.actions.get_attribute_value(self.inptxt_DisplayName)
        return self.displayed_display_name




    def cust_email(self, customer_data):
        self.actions.wait_for_element(self.inptxt_Email)
        self.actions.send_keys(self.inptxt_Email, customer_data["email"])
        time.sleep(2)


    def cust_phonenumcountry(self, customer_data):
        self.actions.wait_for_element(self.dd_PhoneNumCountry)
        #self.actions.wait_for_element_visible(self.dd_PhoneNumCountry)
        #self.actions.click(self.dd_PhoneNumCountry)
       # time.sleep(2)
        #self.actions.send_keys(self.dd_PhoneNumCountry, test_data['phone_num_country'])
        #self.actions.dropdown_equals(self.dd_PhoneNumCountry,self.options_PhoneNumCountry, test_data["phone_num_country"] )
        self.actions.dropdown_no_inp(self.dd_PhoneNumCountry,self.options_PhoneNumCountry, customer_data["phone_num_country"])
        time.sleep(2)


    def cust_phonenumber(self, customer_data):
        self.actions.wait_for_element(self.inpnum_PhoneNumber)
        self.actions.send_keys(self.inpnum_PhoneNumber, customer_data["phone_number"])
        time.sleep(2)

    def cust_mobilenumber(self, customer_data):
        self.actions.wait_for_element(self.inpnum_MobileNumber)
        self.actions.send_keys(self.inpnum_MobileNumber, customer_data["mobile_number"])
        time.sleep(2)

    def cust_fax(self, customer_data):
        self.actions.wait_for_element(self.inpnum_Fax)
        self.actions.send_keys(self.inpnum_Fax, customer_data["fax"])
        time.sleep(2)

    def cust_other(self, customer_data):
        self.actions.wait_for_element(self.inp_Other)
        self.actions.send_keys(self.inp_Other, customer_data["other"])
        time.sleep(2)

    def cust_website(self, customer_data):
        self.actions.wait_for_element(self.inp_Website)
        self.actions.send_keys(self.inp_Website, customer_data["website"])
        time.sleep(2)

    def cust_nametoprintoncheck(self, customer_data):
        self.actions.wait_for_element(self.inptxt_NameToPrintOnChecks)
        self.actions.send_keys(self.inptxt_NameToPrintOnChecks, customer_data["name_to_print_on_check"])
        time.sleep(2)

    def cust_gsttreatment(self,customer_data):
        self.actions.wait_for_element(self.dd_GSTTreatment)
        self.actions.dropdown_equals(self.dd_GSTTreatment,self.options_GSTTreatment,customer_data["gst_treatment"] )
        time.sleep(2)

    def cust_gstnumber(self, customer_data):
        self.actions.wait_for_element(self.inp_GSTnumber)
        self.actions.send_keys(self.inp_GSTnumber, customer_data["gst_number"])
        time.sleep(2)

    #BILLING_ADDRESS
    def cust_billingentermanually(self):
        self.actions.wait_for_element(self.btn_Billing_EnterManually)
        self.actions.scroll_to_the_element(self.btn_Billing_EnterManually)
        self.actions.click(self.btn_Billing_EnterManually)
        time.sleep(2)

    def cust_billing(self,customer_data):
        self.actions.scroll_to_the_element(self.inp_Billing)
        self.actions.wait_for_element(self.inp_Billing)
        #self.actions.click_with_retry(self.inp_Billing)
        self.actions.dropdown_contains(self.inp_Billing,self.options_billing, customer_data["billing"] )
        #self.actions.click(self.inp_Billing)
        #self.actions.send_keys(self.inp_Billing, test_data["billing"])
        time.sleep(2)

    def cust_billingcountry(self,customer_data):
        self.actions.scroll_to_the_element(self.dd_BillingCountry)
        self.actions.wait_for_element(self.dd_BillingCountry)
        self.actions.dropdown_equals(self.dd_BillingCountry,self.options_billingcountry, customer_data["billing_country"] )

    def cust_billingstate(self,customer_data):
        self.actions.scroll_to_the_element(self.dd_BillingState)
        self.actions.wait_for_element(self.dd_BillingState)
        self.actions.dropdown_equals(self.dd_BillingState,self.options_billingstate, customer_data["billing_state"] )

    def cust_billingcity(self, customer_data):
        self.actions.scroll_to_the_element(self.inp_BillingCity)
        self.actions.wait_for_element(self.inp_BillingCity)
        self.actions.send_keys(self.inp_BillingCity, customer_data["billing_city"])

    def  cust_billingzip(self, customer_data):
        self.actions.wait_for_element(self.inp_BillingZip)
        self.actions.send_keys(self.inp_BillingZip, customer_data["billing_zip"])

    # SHIPPING_ADDRESS
        self.actions.scroll_to_the_element(self.checkbx_SameasBilling)
        self.actions.wait_for_element(self.checkbx_SameasBilling)
        self.actions.click(self.checkbx_SameasBilling)

    def cust_shippingentermanually(self):
        self.actions.scroll_to_the_element(self.btn_Shipping_EnterManually)
        self.actions.wait_for_element(self.btn_Shipping_EnterManually)
        self.actions.click(self.btn_Shipping_EnterManually)

    def cust_shipping(self, customer_data):
        self.actions.scroll_to_the_element(self.inp_Shipping)
        self.actions.wait_for_element(self.inp_Shipping)
        self.actions.dropdown_contains(self.inp_Shipping, self.options_shipping,customer_data["shipping"])

    def cust_shippingcountry(self, customer_data):
        self.actions.scroll_to_the_element(self.dd_ShippingCountry)
        self.actions.wait_for_element(self.dd_ShippingCountry)
        self.actions.dropdown_equals(self.dd_ShippingCountry, self.options_shippingcountry, customer_data["shipping_country"])

    def cust_shippingstate(self, customer_data):
        self.actions.scroll_to_the_element(self.dd_ShippingState)
        self.actions.wait_for_element(self.dd_ShippingState)
        self.actions.dropdown_equals(self.dd_ShippingState, self.options_shippingstate, customer_data["shipping_state"])

    def cust_shippingcity(self, customer_data):
        self.actions.scroll_to_the_element(self.inp_ShippingCity)
        self.actions.wait_for_element(self.inp_ShippingCity)
        self.actions.send_keys(self.inp_ShippingCity, customer_data["billing_city"])

    def cust_shippingzip(self, customer_data):
        self.actions.scroll_to_the_element(self.inp_ShippingZip)
        self.actions.wait_for_element(self.inp_ShippingZip)
        self.actions.send_keys(self.inp_ShippingZip, customer_data["shipping_zip"])

    def cust_note(self, customer_data):
        self.actions.scroll_to_the_element(self.inp_Note)
        self.actions.wait_for_element(self.inp_Note)
        self.actions.send_keys(self.inp_Note, customer_data["note"])
        time.sleep(2)

    def cust_customertype(self, customer_data):
        self.actions.wait_for_element(self.dd_CustomerType)
        self.actions.scroll_to_the_element(self.dd_CustomerType)
        self.actions.dropdown_equals(self.dd_CustomerType, self.options_customertype, customer_data["customer_type"])

    def cust_preferreddeliverymethod(self,customer_data):
        self.actions.scroll_to_the_element(self.dd_Preferreddeliverymethod)
        self.actions.wait_for_element(self.dd_Preferreddeliverymethod)
        self.actions.dropdown_equals(self.dd_Preferreddeliverymethod, self.options_preferreddeliverymethod, customer_data["preferred_delivery_method"])

    def cust_preferredpaymentmethod(self, customer_data):
        self.actions.wait_for_element(self.dd_PreferredPaymentMethod)
        self.actions.scroll_to_the_element(self.dd_PreferredPaymentMethod)
        self.actions.dropdown_equals(self.dd_PreferredPaymentMethod, self.options_preferredpaymentmethod, customer_data["preferred_payment_method"])

    def cust_creditterms(self, customer_data):
        self.actions.wait_for_element(self.dd_CreditTerms)
        self.actions.scroll_to_the_element(self.dd_CreditTerms)
        self.actions.dropdown_equals(self.dd_CreditTerms, self.options_creditterms, customer_data["credit_terms"])


    def cust_cancel(self,test_data):
        self.actions.wait_for_element(self.btn_Cancel)
        self.actions.scroll_to_the_element(self.btn_Cancel)
        self.actions.click(self.btn_Cancel)

    def cust_clear(self,test_data):
        self.actions.wait_for_element(self.btn_Clear)
        self.actions.scroll_to_the_element(self.btn_Clear)
        self.actions.click(self.btn_Clear)
        time.sleep(4)

    def cust_storedisplayname(self):
        self.actions.wait_for_element(self.inptxt_DisplayName)
        self.expected_name = self.actions.get_attribute_value(self.inptxt_DisplayName)
        print(self.expected_name)
        time.sleep(2)

    def cust_saveandclose(self):
        self.actions.wait_for_element(self.btn_SaveandClose)
        self.actions.scroll_to_the_element(self.btn_SaveandClose)
        self.actions.click(self.btn_SaveandClose)
        time.sleep(3)

    def cust_saveandnew(self,test_data):
        self.actions.scroll_to_the_element(self.btn_SaveandNew)
        self.actions.wait_for_element(self.btn_SaveandNew)
        self.actions.click(self.btn_SaveandNew)
        time.sleep(3)


    def cust_customer_saved_successfully(self):
        expected_status = self.displayed_display_name
        name_found = False

        while True:
            # Wait for the product list to be visible
            self.actions.wait_for_element(self.list_customerlist)
            product_list = self.driver.find_elements(*self.list_customerlist)

            # Loop through product names on current page
            for product in product_list:
                if product.text.strip().lower() == expected_status.strip().lower():
                    print(f"✅ Match found: {expected_status}")
                    name_found = True
                    break

            if name_found:
                break

            # Handle pagination
            try:
                self.actions.scroll_to_the_element(self.btn_nxt_customerlist)
                next_btn = self.driver.find_element(*self.btn_nxt_customerlist)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    print(f"ℹ️ Reached end of pagination. '{next_btn}' not found.")
                    break

                next_btn.click()

                # Wait until new content loads
                self.wait.until(EC.staleness_of(product_list[0]))
                self.wait.until(EC.presence_of_all_elements_located(self.list_customerlist))

            except NoSuchElementException:
                print("✅ No 'Next' button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        if not name_found:
            print(f"❌ Customer '{self.expected_name}' not found.")

    def cust_close_first_3_alert_tax_msg (self) :
        self.actions.wait_for_element(self.alert_msg_1_close_X_btn)
        self.actions.click(self.alert_msg_1_close_X_btn)
        self.actions.click(self.alert_msg_2_close_X_btn)
        self.actions.click(self.alert_msg_3_close_X_btn)


