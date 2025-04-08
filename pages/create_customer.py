import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.core import driver
from selenium.webdriver.chrome.webdriver import WebDriver

from tests.conftest import setup, test_data

from actions.actions import Actions


class CreateCustomer:
    def __init__(self, driver):
        #self.expected_name = None
        self.driver = driver
        self.actions = Actions(driver)


    btn_submodSales = (By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
    btn_submodCustomer = (By.XPATH,"//a[normalize-space()='Customers']")
    btn_newCustomer = (By.XPATH,"//a[normalize-space()='Create Customer']")
    inptxt_Title = (By.XPATH,"//input[@name='contact_infos.title']")
    inptxt_FirstName = (By.XPATH,"//input[@name='contact_infos.first_name']")
    inptxt_MiddleName = (By.XPATH,"//input[@name='contact_infos.middle_name']")
    inptxt_LastName = (By.XPATH,"//input[@name='contact_infos.last_name']")
    inptxt_CompanyName = (By.XPATH,"//input[@name='additional_infos.company_name']")
    inptxt_DisplayName = (By.XPATH,"//input[@name='contact_infos.display_name']")
    inptxt_Email = (By.XPATH,"//input[@label='Email']")
    dd_PhoneNumCountry = (By.XPATH,"//*[@id='root']/div/div[1]/div[2]/div[2]/div/form/div/div[2]/div[8]/div/div")
    options_PhoneNumCountry = (By.XPATH,"//select[@name='phone_numberCountry']/option")
    inpnum_PhoneNumber = (By.XPATH,"//input[@placeholder='Enter phone number']")
    inpnum_MobileNumber = (By.XPATH,"//input[@label='Mobile Number']")
    inpnum_Fax = (By.XPATH,"//input[@label='Fax']")
    inp_Other = (By.XPATH,"//input[@label='Other']")
    inp_Website = (By.XPATH,"//input[@label='Website']")
    inptxt_NameToPrintOnChecks = (By.XPATH,"//input[@name='contact_infos.name_on_checks']")
    dd_GSTTreatment = (By.XPATH,"//select[@label='GST treatment']")
    options_GSTTreatment =(By.XPATH,"//select[contains(@label,'GST treatment')]/option")
    inp_GSTnumber =(By.XPATH,"//*[@id='root']/div/div[1]/div[2]/div[2]/div/form/div/div[2]/div[15]/div/div/input")
    #Billing_Address
    btn_Billing_EnterManually = (By.XPATH,"//body//div[@id='root']//div[contains(@class,'body flex-grow-1 px-3 mb-5')]//div[contains(@class,'row')]//div[contains(@class,'row')]//div[contains(@class,'row')]//div[1]//div[1]//div[1]//div[1]//button[1]")
    inp_Billing = (By.XPATH,"//label[contains(text(),'Billing')]/following::input[@placeholder='Enter a location']")
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
    inp_Shipping = (By.XPATH,"//label[contains(text(),'Shipping')]/following::input[@placeholder='Enter a location']")
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
    dd_CustomerType = (By.ID,"react-select-2-input")
    options_customertype = (By.XPATH,"//div[contains(@id, 'option')]")
    dd_Preferreddeliverymethod = (By.ID,"react-select-3-input")
    options_preferreddeliverymethod = (By.XPATH, "//div[contains(@class, 'option')]")
    dd_PreferredPaymentMethod = (By.ID,"react-select-4-input")
    options_preferredpaymentmethod = (By.XPATH, "//div[contains(@class, 'option')]")
    dd_CreditTerms = (By.ID,"react-select-5-input")
    options_creditterms = (By.XPATH, "//div[contains(@class, 'option')]")
    btn_Cancel = (By.XPATH,"//a[contains(@class,'sc-eeDRCY eMmKiS text-white')]")
    btn_Clear = (By.XPATH,"//div[@class='expense-footer-btns']//div[1]//button[2]")
    btn_SaveandClose = (By.XPATH,"//button[@id='zoom-primary-cancel-btn']")
    btn_SaveandNew = (By.XPATH,"//button[@id='zoom-primary-btn']")

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


    def cust_title(self, test_data):
        self.actions.wait_for_element(self.inptxt_Title)
        self.actions.send_keys(self.inptxt_Title, test_data["title"])
        time.sleep(3)


    def cust_firstname(self, test_data):
        self.actions.wait_for_element(self.inptxt_FirstName)
        self.actions.send_keys(self.inptxt_FirstName, test_data["first_name"])
        time.sleep(2)


    def cust_middlename(self, test_data):
        self.actions.wait_for_element(self.inptxt_MiddleName)
        self.actions.send_keys(self.inptxt_MiddleName, test_data["middle_name"])
        time.sleep(2)


    def cust_lastname(self, test_data):
        self.actions.wait_for_element(self.inptxt_LastName)
        self.actions.send_keys(self.inptxt_LastName, test_data["last_name"])
        time.sleep(2)


    def cust_companyname(self, test_data):
        self.actions.wait_for_element(self.inptxt_CompanyName)
        self.actions.send_keys(self.inptxt_CompanyName, test_data["company_name"])
        time.sleep(2)


    def cust_displayname(self, test_data):
        self.actions.wait_for_element(self.inptxt_DisplayName)
        self.actions.send_keys(self.inptxt_DisplayName, test_data["display_name"])
        time.sleep(2)


    def cust_email(self, test_data):
        self.actions.wait_for_element(self.inptxt_Email)
        self.actions.send_keys(self.inptxt_Email, test_data["email"])
        time.sleep(2)


    def cust_phonenumcountry(self, test_data):
        self.actions.wait_for_element(self.dd_PhoneNumCountry)
        #self.actions.wait_for_element_visible(self.dd_PhoneNumCountry)
        #self.actions.click(self.dd_PhoneNumCountry)
       # time.sleep(2)
        #self.actions.send_keys(self.dd_PhoneNumCountry, test_data['phone_num_country'])
        #self.actions.dropdown_equals(self.dd_PhoneNumCountry,self.options_PhoneNumCountry, test_data["phone_num_country"] )
        self.actions.dropdown_no_inp(self.dd_PhoneNumCountry,self.options_PhoneNumCountry, test_data["phone_num_country"])
        time.sleep(2)


    def cust_phonenumber(self, test_data):
        self.actions.wait_for_element(self.inpnum_PhoneNumber)
        self.actions.send_keys(self.inpnum_PhoneNumber, test_data["phone_number"])
        time.sleep(2)

    def cust_mobilenumber(self, test_data):
        self.actions.wait_for_element(self.inpnum_MobileNumber)
        self.actions.send_keys(self.inpnum_MobileNumber, test_data["mobile_number"])
        time.sleep(2)

    def cust_fax(self, test_data):
        self.actions.wait_for_element(self.inpnum_Fax)
        self.actions.send_keys(self.inpnum_Fax, test_data["fax"])
        time.sleep(2)

    def cust_other(self, test_data):
        self.actions.wait_for_element(self.inp_Other)
        self.actions.send_keys(self.inp_Other, test_data["other"])
        time.sleep(2)

    def cust_website(self, test_data):
        self.actions.wait_for_element(self.inp_Website)
        self.actions.send_keys(self.inp_Website, test_data["website"])
        time.sleep(2)

    def cust_nametoprintoncheck(self, test_data):
        self.actions.wait_for_element(self.inptxt_NameToPrintOnChecks)
        self.actions.send_keys(self.inptxt_NameToPrintOnChecks, test_data["name_to_print_on_check"])
        time.sleep(2)

    def cust_gsttreatment(self,test_data):
        self.actions.wait_for_element(self.dd_GSTTreatment)
        self.actions.dropdown_equals(self.dd_GSTTreatment,self.options_GSTTreatment, test_data["gst_treatment"] )
        time.sleep(2)

    def cust_gstnumber(self, test_data):
        self.actions.wait_for_element(self.inp_GSTnumber)
        self.actions.send_keys(self.inp_GSTnumber, test_data["gst_number"])
        time.sleep(2)

    #BILLING_ADDRESS
    def cust_billingentermanually(self,test_data):
        self.actions.wait_for_element(self.btn_Billing_EnterManually)
        self.actions.scroll_to_the_element(self.btn_Billing_EnterManually)
        self.actions.click(self.btn_Billing_EnterManually)
        time.sleep(2)

    def cust_billing(self,test_data):
        self.actions.scroll_to_the_element(self.inp_Billing)
        self.actions.wait_for_element(self.inp_Billing)
        #self.actions.click_with_retry(self.inp_Billing)
        self.actions.dropdown_contains(self.inp_Billing,self.options_billing, test_data["billing"] )
        #self.actions.click(self.inp_Billing)
        #self.actions.send_keys(self.inp_Billing, test_data["billing"])
        time.sleep(2)

    def cust_billingcountry(self,test_data):
        self.actions.scroll_to_the_element(self.dd_BillingCountry)
        self.actions.wait_for_element(self.dd_BillingCountry)
        self.actions.dropdown_equals(self.dd_BillingCountry,self.options_billingcountry, test_data["billing_country"] )

    def cust_billingstate(self,test_data):
        self.actions.scroll_to_the_element(self.dd_BillingState)
        self.actions.wait_for_element(self.dd_BillingState)
        self.actions.dropdown_equals(self.dd_BillingState,self.options_billingstate, test_data["billing_state"] )

    def cust_billingcity(self, test_data):
        self.actions.scroll_to_the_element(self.inp_BillingCity)
        self.actions.wait_for_element(self.inp_BillingCity)
        self.actions.send_keys(self.inp_BillingCity, test_data["billing_city"])

    def  cust_billingzip(self, test_data):
        self.actions.wait_for_element(self.inp_BillingZip)
        self.actions.send_keys(self.inp_BillingZip, test_data["billing_zip"])

    # SHIPPING_ADDRESS
    def cust_sameasbilling(self,test_data):
        self.actions.scroll_to_the_element(self.checkbx_SameasBilling)
        self.actions.wait_for_element(self.checkbx_SameasBilling)
        self.actions.click(self.checkbx_SameasBilling)

    def cust_shippingentermanually(self, test_data):
        self.actions.scroll_to_the_element(self.btn_Shipping_EnterManually)
        self.actions.wait_for_element(self.btn_Shipping_EnterManually)
        self.actions.click(self.btn_Shipping_EnterManually)

    def cust_shipping(self, test_data):
        self.actions.scroll_to_the_element(self.inp_Shipping)
        self.actions.wait_for_element(self.inp_Shipping)
        self.actions.dropdown_contains(self.inp_Shipping, self.options_shipping, test_data["shipping"])

    def cust_shippingcountry(self, test_data):
        self.actions.scroll_to_the_element(self.dd_ShippingCountry)
        self.actions.wait_for_element(self.dd_ShippingCountry)
        self.actions.dropdown_equals(self.dd_ShippingCountry, self.options_shippingcountry, test_data["shipping_country"])

    def cust_shippingstate(self, test_data):
        self.actions.scroll_to_the_element(self.dd_ShippingState)
        self.actions.wait_for_element(self.dd_ShippingState)
        self.actions.dropdown_equals(self.dd_ShippingState, self.options_shippingstate, test_data["shipping_state"])

    def cust_shippingcity(self, test_data):
        self.actions.scroll_to_the_element(self.inp_ShippingCity)
        self.actions.wait_for_element(self.inp_ShippingCity)
        self.actions.send_keys(self.inp_ShippingCity, test_data["billing_city"])

    def cust_shippingzip(self, test_data):
        self.actions.scroll_to_the_element(self.inp_ShippingZip)
        self.actions.wait_for_element(self.inp_ShippingZip)
        self.actions.send_keys(self.inp_ShippingZip, test_data["shipping_zip"])

    def cust_note(self, test_data):
        self.actions.scroll_to_the_element(self.inp_Note)
        self.actions.wait_for_element(self.inp_Note)
        self.actions.send_keys(self.inp_Note, test_data["note"])

    def cust_customertype(self, test_data):
        self.actions.scroll_to_the_element(self.dd_CustomerType)
        self.actions.wait_for_element(self.dd_CustomerType)
        self.actions.dropdown_equals(self.dd_CustomerType, self.options_customertype, test_data["customer_type"])

    def cust_preferreddeliverymethod(self, test_data):
        self.actions.scroll_to_the_element(self.dd_Preferreddeliverymethod)
        self.actions.wait_for_element(self.dd_Preferreddeliverymethod)
        self.actions.dropdown_equals(self.dd_Preferreddeliverymethod, self.options_preferreddeliverymethod, test_data["preferred_delivery_method"])

    def cust_preferredpaymentmethod(self, test_data):
        self.actions.scroll_to_the_element(self.dd_PreferredPaymentMethod)
        self.actions.wait_for_element(self.dd_PreferredPaymentMethod)
        self.actions.dropdown_equals(self.dd_PreferredPaymentMethod, self.options_preferredpaymentmethod, test_data["preferred_payment_method"])

    def cust_creditterms(self, test_data):
        self.actions.scroll_to_the_element(self.dd_CreditTerms)
        self.actions.wait_for_element(self.dd_CreditTerms)
        self.actions.dropdown_equals(self.dd_CreditTerms, self.options_creditterms, test_data["credit_terms"])


    def cust_cancel(self,test_data):
        self.actions.scroll_to_the_element(self.btn_Cancel)
        self.actions.wait_for_element(self.btn_Cancel)
        self.actions.click(self.btn_Cancel)

    def cust_clear(self,test_data):
        self.actions.scroll_to_the_element(self.btn_Clear)
        self.actions.wait_for_element(self.btn_Clear)
        self.actions.click(self.btn_Clear)
        time.sleep(4)

    def cust_storedisplayname(self):
        self.actions.wait_for_element(self.inptxt_DisplayName)
        self.expected_name = self.actions.get_attribute(self.inptxt_DisplayName)
        print(self.expected_name)
        time.sleep(2)

    def cust_saveandclose(self):
        self.actions.scroll_to_the_element(self.btn_SaveandClose)
        self.actions.wait_for_element(self.btn_SaveandClose)
        self.actions.click(self.btn_SaveandClose)
        time.sleep(3)

    def cust_saveandnew(self,test_data):
        self.actions.scroll_to_the_element(self.btn_SaveandNew)
        self.actions.wait_for_element(self.btn_SaveandNew)
        self.actions.click(self.btn_SaveandNew)
        time.sleep(3)


    def cust_customer_saved_successfully(self, driver:WebDriver ):
       #wait = WebDriverWait(driver, timeout)
        name_found = False

        while True:
            # Wait until the customer list is visible
            #wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']//table/tbody//a")))
            self.actions.wait_for_element(self.list_customerlist)
            # Get list of customer elements
            customer_list = self.driver.find_elements(*self.list_customerlist)

            # Scroll to each customer entry
            for customer in customer_list:
                #scroll_to_element(driver, customer)
                if customer.text.strip().lower() == self.expected_name.strip().lower():
                    print(f"Match found: {self.expected_name}")
                    name_found = True
                    break

            if name_found:
                break

            # Try to find the Next button
            #wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='>']")))
            self.actions.wait_for_element(self.btn_nxt_customerlist)
            next_buttons = self.driver.find_elements(*self.btn_nxt_customerlist)

            if next_buttons:
                #scroll_to_element(driver, next_buttons[0])
                next_buttons[0].click()
                time.sleep(2)  # Give time for next page to load
            else:
                print("Name not found in any pages.")
                break
