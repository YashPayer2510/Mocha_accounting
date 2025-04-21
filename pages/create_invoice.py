import time

from selenium.webdriver.common.by import By

from actions.actions import Actions
from tests.conftest import create_invoice_test_data

class Create_Invoice:
    def __init__(self, driver):
        #self.expected_name = None
        self.driver = driver
        self.actions = Actions(driver)

    inv_btn_submod_Sales= (By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
    inv_btn_submod_invoice =(By.XPATH,"//a[@class='nav-link'][normalize-space()='Invoices']")
    inv_btn_create_invoice = (By.XPATH,"//button[normalize-space()='Create Invoice']")
    inv_dd_customer= (By.XPATH,"//*[@id='react-select-2-input']")
    inv_options_customer = By.XPATH,"//div[contains(@class, 'option')]"
    inv_dd_credit_terms = (By.ID,"react-select-3-input")
    inv_options_credit_terms =(By.XPATH,"//div[@role='option' and contains(@class, 'css-10wo9uf-option')]")
    inv_dd_location_of_sale =(By.XPATH,"//*[@id='root']/div/div[1]/div[2]/div[2]/div/form/div[4]/div[2]/div/div/input")
    inv_options_location_of_sale = (By.XPATH, "//span[contains(@class, 'pac-item')]")
    inv_dd_billing =(By.XPATH,"//*[@id=root]/div/div[1]/div[2]/div[2]/div/form/div[5]/div[1]/div/div/input")
    inv_options_billing =(By.XPATH,"//span[contains(@class, 'pac-item')]")
    inv_dd_shipvia =(By.XPATH,"//*[@id='root']/div/div[1]/div[2]/div[2]/div/form/div[5]/div[2]/div/div/input")
    inv_options_shipvia= (By.XPATH, "//span[contains(@class, 'pac-item')]")
    inv_dd_shipping_to =(By.XPATH,"//*[@id='root']/div/div[1]/div[2]/div[2]/div/form/div[5]/div[3]/div/div/input")
    inv_options_shipping_to = (By.XPATH, "//span[contains(@class, 'pac-item')]")
    inv_datep_invoice_date =(By.XPATH,"//input[@name='invoice_date']")
    inv_datepicker_month_class = (By.CLASS_NAME,"react-datepicker__current-month")
    inv_next_btn_class = (By.CLASS_NAME,"react-datepicker__navigation--next")
    inv_prev_btn_class = (By.CLASS_NAME,"react-datepicker__navigation--previous")
    inv_datep_shipping_date = (By.XPATH,"//input[@name='shipping_date']")
    inv_datep_due_date = (By.XPATH, "//input[@name='due_date']")
    inv_btn_add_items = (By.XPATH,"//button[@class='btn btn-light sc-eqUAAy kJGDIg shadow-none']")
    inv_dd_select_product = (By.XPATH,"//div[contains(@class,'modal-content')]//div[contains(@class,'css-19bb58m')]//input")
    inv_options_select_productservice =(By.ID,"//div[contains(@class, 'option')]")
    inv_inp_quanitiy = (By.XPATH,"//input[@name='rate']")
    inv_inp_rate_per_unit = (By.XPATH,"//input[@name='rate']")
    inv_btn_prod_save = (By.XPATH,"//button[normalize-space()='Save']")
    inv_btn_prod_cancel = (By.XPATH,"//button[@class='btn btn-outline-primary btn-sm sc-eqUAAy kJGDIg']")
    inv_txt_sub_total = (By.XPATH,"//h5[1]//span[1]")
    inv_txt_tax = (By.XPATH,"//h5[2]//span[1]")
    inv_txt_amount_received = (By.XPATH,"//h5[3]//span[1]")
    inv_txt_balance = (By.XPATH, "//h5[4]//span[1]")
    inv_inp_message_on_invoice = (By.XPATH,"//div[@class='createInvoiceMessageTour']//textarea[@aria-label='With textarea']")
    inv_btn_save_close = (By.XPATH,"//button[@id='zoom-primary-cancel-btn']")
    inv_btn_save_new = (By.XPATH,"//button[normalize-space()='Save and New']")
    inv_btn_cancel = (By.XPATH,"//div[@class='expense-footer-btns']//div[1]//button[1]")
    inv_btn_clear = (By.XPATH,"//div[@class='expense-footer-btns']//div[1]//button[2]")

    #product and service list
    inv_added_productservice_list = (By.XPATH,"//*[@id='root']//table/tbody/tr/td[2]")
    inv_added_productservice_qty =(By.XPATH,"//*[@id='root']//table/tbody/tr/td[3]")
    inv_added_productservice_rate=(By.XPATH,"//*[@id='root']//table/tbody/tr/td[4]")
    inv_added_productservice_amount=(By.XPATH,"//*[@id='root']//table/tbody/tr/td[5]")
    inv_added_productservice_tax=(By.XPATH,"//*[@id='root']//table/tbody/tr/td[6]")
    inv_added_productservice_total=(By.XPATH,"//*[@id='root']//table/tbody/tr/td[7]")

    #if want to access each line items then add number after tr tag e.g tr[1]



    def inv_submod_Sales(self):
        self.actions.wait_for_element(self.inv_btn_submod_Sales)
        self.actions.click(self.inv_btn_submod_Sales)


    def inv_submod_invoice(self):
        self.actions.wait_for_element(self.inv_btn_submod_invoice)
        self.actions.click(self.inv_btn_submod_invoice)
        time.sleep(2)

    def inv_create_invoice(self):
        self.actions.wait_for_element(self.inv_btn_create_invoice)
        self.actions.click(self.inv_btn_create_invoice)
        time.sleep(2)

    def inv_select_customer(self, create_invoice_test_data):
        self.actions.scroll_to_the_element(self.inv_dd_customer)
        self.actions.wait_for_element(self.inv_dd_customer)
        self.actions.dropdown_equals(self.inv_dd_customer, self.inv_options_customer,create_invoice_test_data["customer_name"])

    def inv_select_credit_terms(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_dd_credit_terms)
        self.actions.scroll_to_the_element(self.inv_dd_credit_terms)
        self.actions.dropdown_equals(self.inv_dd_credit_terms, self.inv_options_credit_terms, create_invoice_test_data[""])

    def inv_location_of_sale(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_dd_location_of_sale)
        self.actions.scroll_to_the_element(self.inv_dd_location_of_sale)
        self.actions.dropdown_contains(self.inv_dd_location_of_sale, self.inv_options_location_of_sale, create_invoice_test_data[""])

    def inv_shippingvia(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_dd_shipvia)
        self.actions.scroll_to_the_element(self.inv_dd_shipvia)
        self.actions.dropdown_contains(self.inv_dd_shipvia, self.inv_options_shipvia,create_invoice_test_data[""])

    def inv_shipping_to(self,create_invoice_test_data ):
        self.actions.wait_for_element(self.inv_dd_shipping_to)
        self.actions.scroll_to_the_element(self.inv_dd_shipping_to)
        self.actions.dropdown_contains(self.inv_dd_shipping_to, self.inv_options_shipping_to,create_invoice_test_data[""])

    def inv_invoice_date(self,create_invoice_test_data):
        self.actions.wait_for_element(self.inv_datep_invoice_date)
        self.actions.scroll_to_the_element(self.inv_datep_invoice_date)
        self.actions.select_date(self.inv_datep_invoice_date, self.inv_datepicker_month_class, self.inv_next_btn_class, self.inv_prev_btn_class, create_invoice_test_data["invoice_date"])

    def inv_shipping_date(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_datep_shipping_date)
        self.actions.scroll_to_the_element(self.inv_datep_shipping_date)
        self.actions.select_date(self.inv_datep_shipping_date, self.inv_datepicker_month_class, self.inv_next_btn_class, self.inv_prev_btn_class, create_invoice_test_data["shipping_date"])

    def inv_due_date(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_datep_due_date)
        self.actions.scroll_to_the_element(self.inv_datep_due_date)
        self.actions.select_date(self.inv_datep_due_date, self.inv_datepicker_month_class, self.inv_next_btn_class, self.inv_prev_btn_class, create_invoice_test_data["due_date"])

    def inv_click_additems(self):
        self.actions.wait_for_element(self.inv_btn_add_items)
        self.actions.scroll_to_the_element(self.inv_btn_add_items)
        self.actions.click(self.inv_btn_add_items)

    def inv_select_productservice(self,create_invoice_test_data ):
        self.actions.wait_for_element(self.inv_dd_select_product)
        self.actions.scroll_to_the_element(self.inv_dd_select_product)
        self.actions.dropdown_equals(self.inv_dd_select_product, self.inv_options_select_productservice, create_invoice_test_data["product_service_name"])

    def inv_product_quantity(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_inp_quanitiy)
        self.actions.scroll_to_the_element(self.inv_inp_quanitiy)
        self.actions.send_keys(self.inv_inp_quanitiy, create_invoice_test_data["quantity"])

    def inv_product_rateperunit(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_inp_rate_per_unit)
        self.actions.scroll_to_the_element(self.inv_inp_rate_per_unit)
        self.actions.send_keys(self.inv_inp_rate_per_unit, create_invoice_test_data["rate_per_unit"])

    def inv_selectproduct_cancel(self):
        self.actions.wait_for_element(self.inv_btn_prod_cancel)
        self.actions.scroll_to_the_element(self.inv_btn_prod_cancel)
        self.actions.click(self.inv_btn_prod_cancel)

    def inv_selecproduct_save(self):
        self.actions.wait_for_element(self.inv_btn_prod_save)
        self.actions.scroll_to_the_element(self.inv_btn_prod_save)
        self.actions.click(self.inv_btn_prod_save)

    def inv_message_on_invoice(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_inp_message_on_invoice)
        self.actions.scroll_to_the_element(self.inv_inp_message_on_invoice)
        self.actions.send_keys(self.inv_inp_message_on_invoice, create_invoice_test_data[""])

    def inv_subtotal(self):
        self.actions.wait_for_element(self.inv_txt_sub_total)
        self.actions.scroll_to_the_element(self.inv_txt_sub_total)
        invoice_subtotal = self.actions.get_text(self.inv_txt_sub_total)
        print(f"subtotal: {invoice_subtotal}")

    def inv_tax(self):
        self.actions.wait_for_element(self.inv_txt_tax)
        self.actions.scroll_to_the_element(self.inv_txt_tax)
        invoice_tax = self.actions.get_text(self.inv_txt_tax)

    def inv_amount_received(self):
        self.actions.wait_for_element(self.inv_txt_tax)
        self.actions.scroll_to_the_element(self.inv_txt_tax)
        invoice_amount_received = self.actions.get_text(self.inv_txt_tax)
        print(f"amount received: {invoice_amount_received}")

    def inv_balance(self):
        self.actions.wait_for_element(self.inv_txt_balance)
        self.actions.scroll_to_the_element(self.inv_txt_balance)
        invoice_balance= self.actions.get_text(self.inv_txt_balance)
        print(f"balance: {invoice_balance}")

    def inv_cancel(self):
        self.actions.wait_for_element(self.inv_btn_cancel)
        self.actions.scroll_to_the_element(self.inv_btn_cancel)
        self.actions.click(self.inv_btn_cancel)

    def inv_clear(self):
        self.actions.wait_for_element(self.inv_btn_clear)
        self.actions.scroll_to_the_element(self.inv_btn_clear)
        self.actions.click(self.inv_btn_clear)

    def inv_save_and_close(self):
        self.actions.wait_for_element(self.inv_btn_save_close)
        self.actions.scroll_to_the_element(self.inv_btn_save_close)
        self.actions.click(self.inv_btn_save_close)

    def inv_save_and_new(self):
        self.actions.wait_for_element(self.inv_btn_save_new)
        self.actions.scroll_to_the_element(self.inv_btn_save_new)
        self.actions.click(self.inv_btn_save_new)

