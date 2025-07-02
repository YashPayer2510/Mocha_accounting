import logging
import time

from selenium.common import StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unicodedata import category

from actions.actions import Actions
from tests.conftest import create_bill_test_data
from tests.conftest import create_invoice_test_data
class Create_Bill:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 50)

    create_bill_plus_new = (By.XPATH,"//button[@class='pe-5 ps-5 btn btn-sm m-3 m-3']")
    create_bill_bill= (By.XPATH, "//a[normalize-space()='Bill']")
    create_bill_payee_dd = (By.XPATH,"//label[text()='Payee *']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    create_bill_options_payee_dd = (By.XPATH,"//div[contains(@class, 'option')]")
    create_bill_credit_terms_dd =(By.XPATH,"//label[text()='Credit Terms *']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    create_bill_options_credit_terms_dd = (By.XPATH,"//div[contains(@class, 'option')]")
    create_bill_payee_address = (By.XPATH,"//label[contains(text(),'Payee address *')]/following::input[@placeholder='Enter a location']")
    create_bill_options_payee_address = (By.XPATH, "/html/body/div[2]")
    create_bill_location_of_sale = (By.XPATH, "//label[contains(text(),'Location Of Sale *')]/following::input[@placeholder='Enter a location']")
    create_bill_options_location_of_sale = (By.XPATH, "/html/body/div[2]")
    create_bill_bill_date = (By.XPATH, "//input[@name='bill_date']")
    create_bill_bill_date_datepicker_current_month_class = (By.CLASS_NAME,"react-datepicker__current-month")
    create_bill_bill_date_next_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--next")
    create_bill_bill_date_prev_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--previous")
    create_bill_due_date = (By.XPATH, "//input[@name='due_date']")
    create_bill_due_date_datepicker_current_month_class = (By.CLASS_NAME, "react-datepicker__current-month")
    create_bill_due_date_next_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--next")
    create_bill_due_date_prev_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--previous")
    create_bill_bill_no = (By.XPATH,"//input[@name='bill_no']")
    create_bill_category_details_add_new_lines_btn = (By.XPATH,"//div[@class='container-fluid']//div[1]//div[2]//table[1]//thead[2]//tr[1]//th[1]//button[1]")
    create_bill_select_category_cao_dd = (By.XPATH,"//div[@class='row'][1]//table//tr//td[3]//input[contains(@id, 'react')]")
    create_bill_options_category_cao_dd = (By.XPATH, "//div[contains(@class, 'option')]")
    create_bill_category_descriptions = (By.XPATH,"//input[@name='description']")
    create_bill_category_amount = (By.XPATH,"//input[@name='amount']")
    create_bill_category_billable_chkbx = (By.XPATH,"//input[@id='flexCheckDefault1'] [@name='billable']")
    create_bill_category_tax_chkbx = (By.XPATH,"//input[@id='flexCheckDefault1'] [@name='tax']")
    create_bill_select_product_service_dd = (By.XPATH, "//div[@class='row'][2]//table//tr//td[2]")
    create_bill_options_product_service_dd = (By.XPATH, "//div[contains(@class, 'option')]")
    create_bill_item_details_qty = (By.XPATH,"//div[@class='row'][2]//table//tr//td[4]")
    create_bill_item_details_rate = (By.XPATH,"//div[@class='row'][2]//table//tr//td[5]")
    create_bill_item_details_amount = (By.XPATH,"//div[@class='row'][2]//table//tr//td[6]")
    create_bill_item_details_total = (By.XPATH,"//div[@class='row'][2]//table//tr//td[7]")
    create_bill_item_details_add_new_line_btn= (By.XPATH,"//div[@class='body flex-grow-1 px-3 mb-5']//div[2]//div[2]//table[1]//thead[2]//tr[1]//th[1]//button[1]")
    create_bill_balance_txt = (By.XPATH,"//h5[1]//span[1]")
    create_bill_memo= (By.XPATH,"//textarea[@name='memo']")
    create_bill_btn_save_close = (By.XPATH, "//button[@id='zoom-primary-cancel-btn']")
    create_bill_btn_save_new = (By.XPATH, "//button[normalize-space()='Save and New']")
    create_bill_btn_cancel = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[1]")
    create_bill_btn_clear = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[2]")
    create_bill_btn_x = (By.XPATH, "//div[contains(@class, 'toast') and contains(@class, 'show')]//button[contains(@class, 'btn-close')]")

    # optional
    inv_btn_submod_Sales = (By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
    inv_btn_submod_invoice = (By.XPATH, "//a[@class='nav-link'][normalize-space()='Invoices']")
    inv_btn_create_invoice = (By.XPATH, "//button[normalize-space()='Create Invoice']")
    inv_dd_customer = (By.XPATH, "//*[@id='react-select-2-input']")
    inv_options_customer = By.XPATH, "//div[contains(@class, 'option')]"
    inv_btn_add_items = (By.XPATH, "//button[@class='btn btn-light sc-eqUAAy kJGDIg shadow-none']")
    inv_dd_select_product = (By.XPATH, "//div[contains(@class,'modal-content')]//div[contains(@class,'css-19bb58m')]//input")
    inv_options_select_productservice = (By.XPATH, "//div[contains(@class, 'option')]")
    inv_m_btn_x = (By.XPATH,"//div[@class='modal-header sc-kOHTFB ivaBOY']//button[@aria-label='Close']")

    def create_b_new(self):
        self.actions.wait_for_element(self.create_bill_plus_new)
        self.actions.click(self.create_bill_plus_new)

    def create_b_bill(self):
        self.actions.wait_for_element(self.create_bill_bill)
        self.actions.click(self.create_bill_bill)

    def create_b_select_payee(self,create_bill_test_data ):
        self.actions.wait_for_element(self.create_bill_payee_dd)
        self.actions.scroll_to_the_element(self.create_bill_payee_dd)
        self.actions.dropdown_equals(self.create_bill_payee_dd, self.create_bill_options_payee_dd,create_bill_test_data["bill_payee"])

    def create_b_select_credit_terms(self, create_bill_test_data):
        self.actions.wait_for_element(self.create_bill_credit_terms_dd)
        self.actions.scroll_to_the_element(self.create_bill_credit_terms_dd)
        self.actions.dropdown_equals(self.create_bill_credit_terms_dd, self.create_bill_options_credit_terms_dd,create_bill_test_data["bill_credit_memo"])

    def create_b_payee_address(self, create_bill_test_data):
        self.actions.wait_for_element(self.create_bill_payee_address)
        self.actions.scroll_to_the_element(self.create_bill_payee_address)
        self.actions.dropdown_contains(self.create_bill_payee_address, self.create_bill_options_payee_address, create_bill_test_data["bill_payee_address"])

    def create_b_location_of_sale(self, create_bill_test_data):
        self.actions.wait_for_element(self.create_bill_location_of_sale)
        self.actions.scroll_to_the_element(self.create_bill_location_of_sale)
        self.actions.dropdown_contains(self.create_bill_location_of_sale, self.create_bill_options_location_of_sale, create_bill_test_data["bill_location_of_sale"])

    def create_b_bill_date(self, create_bill_test_data):
        self.actions.wait_for_element(self.create_bill_bill_date)
        self.actions.scroll_to_the_element(self.create_bill_bill_date)
        self.actions.select_date(self.create_bill_bill_date, self.create_bill_bill_date_datepicker_current_month_class,self.create_bill_bill_date_next_btn_class, self.create_bill_bill_date_prev_btn_class,create_bill_test_data["bill_bill_date"])

    def create_b_due_date(self, create_bill_test_data):
        self.actions.wait_for_element(self.create_bill_due_date)
        self.actions.scroll_to_the_element(self.create_bill_due_date)
        self.actions.select_date(self.create_bill_due_date, self.create_bill_due_date_datepicker_current_month_class,self.create_bill_due_date_next_btn_class, self.create_bill_due_date_prev_btn_class,create_bill_test_data["bill_due_date"])

    def create_b_bill_no(self, create_bill_test_data):
        self.actions.wait_for_element(self.create_bill_bill_no)
        self.actions.scroll_to_the_element(self.create_bill_bill_no)
        self.actions.send_keys(self.create_bill_bill_no, create_bill_test_data["bill_bill_no"])

    def create_b_category_add_new_line_btn(self):
        self.actions.wait_for_element(self.create_bill_category_details_add_new_lines_btn)
        self.actions.scroll_to_the_element(self.create_bill_category_details_add_new_lines_btn)
        self.actions.click(self.create_bill_category_details_add_new_lines_btn)
        time.sleep(2)

    def create_b_category_select_category_cao(self, create_bill_test_data):
        self.actions.wait_for_element(self.create_bill_select_category_cao_dd)
        self.actions.scroll_to_the_element(self.create_bill_select_category_cao_dd)
        self.actions.dropdown_contains(self.create_bill_select_category_cao_dd,self.create_bill_options_category_cao_dd, create_bill_test_data["bill_category_CAO"])

    def create_b_category_amount(self, create_bill_test_data):
        self.actions.wait_for_element(self.create_bill_category_amount)
        self.actions.scroll_to_the_element(self.create_bill_category_amount)
        self.actions.send_keys(self.create_bill_category_amount, create_bill_test_data["bill_category_amount"])

    def create_b_category_billable(self,create_bill_test_data):
        self.actions.wait_for_element(self.create_bill_category_billable_chkbx)
        self.actions.scroll_to_the_element(self.create_bill_category_billable_chkbx)
        self.actions.click(self.create_bill_category_billable_chkbx)

    def create_b_category_tax(self,create_bill_test_data):
        self.actions.wait_for_element(self.create_bill_category_tax_chkbx)
        self.actions.scroll_to_the_element(self.create_bill_category_tax_chkbx)
        self.actions.click(self.create_bill_category_tax_chkbx)

    def create_b_item_details_add_new_line_btn(self):
        self.actions.wait_for_element(self.create_bill_item_details_add_new_line_btn)
        self.actions.scroll_to_the_element(self.create_bill_item_details_add_new_line_btn)
        self.actions.click(self.create_bill_item_details_add_new_line_btn)

    def create_b_item_details_select_product_serv(self, create_bill_test_data):
        self.actions.wait_for_element(self.create_bill_select_product_service_dd)
        self.actions.scroll_to_the_element(self.create_bill_select_product_service_dd)
        self.actions.dropdown_contains(self.create_bill_select_product_service_dd, self.create_bill_options_product_service_dd, create_bill_test_data["bill_item_details_prod_serv"])

    def create_b_item_details_qty(self, create_bill_test_data):
        self.actions.wait_for_element(self.create_bill_item_details_qty)
        self.actions.scroll_to_the_element(self.create_bill_item_details_qty)
        self.actions.send_keys(self.create_bill_item_details_qty, create_bill_test_data["bill_item_details_qty"])

    def create_b_item_details_rate(self, create_bill_test_data):
        self.actions.wait_for_element(self.create_bill_item_details_rate)
        self.actions.scroll_to_the_element(self.create_bill_item_details_rate)
        self.actions.send_keys(self.create_bill_item_details_rate, create_bill_test_data["bill_item_details_rate"])

    def create_b_item_details_amount(self):
        self.actions.wait_for_element(self.create_bill_item_details_amount)
        self.actions.scroll_to_the_element(self.create_bill_item_details_amount)
        displayed_amount = self.actions.get_text(self.create_bill_item_details_amount)

    def create_b_item_details_total(self):
        self.actions.wait_for_element(self.create_bill_item_details_total)
        self.actions.scroll_to_the_element(self.create_bill_item_details_total)
        displayed_total = self.actions.get_text(self.create_bill_item_details_total)

    def create_b_balance(self):
        self.actions.wait_for_element(self.create_bill_balance_txt)
        self.actions.scroll_to_the_element(self.create_bill_balance_txt)
        displayed_balance = self.actions.get_text(self.create_bill_balance_txt)

    def create_b_memo(self, create_bill_test_data):
        self.actions.wait_for_element(self.create_bill_memo)
        self.actions.scroll_to_the_element(self.create_bill_memo)
        self.actions.send_keys(self.create_bill_memo, create_bill_test_data["bill_memo"])

    def create_b_cancel(self):
        self.actions.wait_for_element(self.create_bill_btn_cancel)
        self.actions.scroll_to_the_element(self.create_bill_btn_cancel)
        self.actions.click(self.create_bill_btn_cancel)

    def create_b_clear(self):
        self.actions.wait_for_element(self.create_bill_btn_clear)
        self.actions.scroll_to_the_element(self.create_bill_btn_clear)
        self.actions.click(self.create_bill_btn_clear)

    def create_b_save_and_close(self):
        self.actions.wait_for_element(self.create_bill_btn_save_close)
        self.actions.scroll_to_the_element(self.create_bill_btn_save_close)
        self.actions.click(self.create_bill_btn_save_close)

    def create_b_save_and_new(self):
        self.actions.wait_for_element(self.create_bill_btn_save_new)
        self.actions.scroll_to_the_element(self.create_bill_btn_save_new)
        self.actions.click(self.create_bill_btn_save_new)

    def create_b_x_button(self):
        self.actions.wait_for_element(self.create_bill_btn_x)
        self.actions.scroll_to_the_element(self.create_bill_btn_x)
        self.actions.click(self.create_bill_btn_x)

    def create_b_add_multiple_category_cao_with_changexpath(self, create_bill_test_data):
        category_coa_list = create_bill_test_data["bill_category_CAO"]
        category_coa_amount = create_bill_test_data["bill_category_amount"]

        for index, (category_cao, amount) in enumerate(zip(category_coa_list, category_coa_amount)):
            # Get fresh references to elements for each new row
            row_index = index + 1  # XPath indexes are 1-based

            # Dynamic locators for each row
            category_dropdown_locator = (
                By.XPATH,
                f"(//div[@class='row'][1]//table//tr[{row_index}]//td[3]//input[contains(@id, 'react')])"
            )

            # For amount field (assuming it's in the 3rd column)
            amount_field_locator = (
                By.XPATH,
                f"(//div[@class='row'][1]//table//tr[{row_index}]//td[5]//input[contains(@name,'amount')])"
            )
            # 1. Handle Category Dropdown
            self.actions.wait_for_element_clickable(category_dropdown_locator)
            self.actions.scroll_to_the_element(category_dropdown_locator)
            self.actions.dropdown_contains(
                category_dropdown_locator,
                self.create_bill_options_category_cao_dd,
                category_cao
            )
            time.sleep(1)  # Short pause

            # 2. Enter Amount
            self.actions.wait_for_element(amount_field_locator)
            self.actions.clear_text(amount_field_locator)
            self.actions.send_keys(amount_field_locator,amount)
            time.sleep(1)  # Short pause

            # 3. Add new line if needed
            if index < len(category_coa_list) - 1:
                self.actions.click(self.create_bill_category_details_add_new_lines_btn)
                time.sleep(2)  # Wait for new row to render


    def create_b_add_multiple_product_cao_with_changexpath(self, create_bill_test_data):
        product_serv_list = create_bill_test_data["bill_item_details_prod_serv"]
        product_serv_qty_list = create_bill_test_data["bill_item_details_qty"]
        product_serv_rate_list = create_bill_test_data["bill_item_details_rate"]



        for index, (product_serv, qty, rate) in enumerate(zip(product_serv_list, product_serv_qty_list, product_serv_rate_list)):
            # Get fresh references to elements for each new row
            row_index = index + 1  # XPath indexes are 1-based

            # Dynamic locators for each row
            product_serv_dropdown_locator = (
                By.XPATH,
                f"(//div[@class='row'][2]//table//tr[{row_index}]//td[2]//input[contains(@id,'react')])"
            )

            qty_field_locator = (
                By.XPATH,
                f"(//div[@class='row'][2]//table//tr[{row_index}]//td[4]//input[contains(@type, 'number')])"
            )

            rate_field_locator = (
                By.XPATH,
                f"(//div[@class='row'][2]//table//tr[{row_index}]//td[5]//input[contains(@type, 'number')])"
            )
            # 1. Handle product/service Dropdown
            self.actions.wait_for_element_clickable(product_serv_dropdown_locator)
            self.actions.scroll_to_the_element(product_serv_dropdown_locator)
            self.actions.click(product_serv_dropdown_locator)
            time.sleep(2)
            self.actions.dropdown_contains(
                product_serv_dropdown_locator,
                self.create_bill_options_product_service_dd,
                product_serv
            )
            time.sleep(1)  # Short pause

            # 2. Enter qty
            self.actions.wait_for_element_clickable(qty_field_locator)
            self.actions.clear_text(qty_field_locator)
            self.actions.send_keys(qty_field_locator,qty)
            time.sleep(1)  # Short pause

            # 2. Enter rate
            self.actions.wait_for_element_clickable(rate_field_locator)
            self.actions.clear_text(rate_field_locator)
            self.actions.send_keys(rate_field_locator, rate)
            time.sleep(1)  # Short pause

            # 3. Add new line if needed
            if index < len(product_serv_list) - 1:
                self.actions.click(self.create_bill_item_details_add_new_line_btn)
                time.sleep(2)  # Wait for new row to render

    def create_b_click_x_button(self):
        self.actions.wait_for_element(self.create_bill_btn_x)
        self.actions.click(self.create_bill_btn_x)
        time.sleep(2)

    #optional
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

    def inv_add_items_btn(self):
        self.actions.wait_for_element(self.inv_btn_add_items)
        self.actions.click(self.inv_btn_add_items)
        time.sleep(2)

    def inv_click_product_service(self):
        self.actions.wait_for_element(self.inv_dd_select_product)
        self.actions.click(self.inv_dd_select_product)
        time.sleep(2)

    def inv_click_product_x_button(self):
        self.actions.wait_for_element(self.inv_m_btn_x)
        self.actions.click(self.inv_m_btn_x)
        time.sleep(2)
















