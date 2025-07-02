import logging
import time

from selenium.common import StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unicodedata import category

from actions.actions import Actions
from tests.conftest import create_check_test_data
from tests.conftest import create_invoice_test_data

class Create_Check:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 50)

    create_check_plus_new = (By.XPATH, "//button[@class='pe-5 ps-5 btn btn-sm m-3 m-3']")
    create_check_check = (By.XPATH, "//a[normalize-space()='Check']")
    create_check_payee_dd = (By.XPATH, "//label[text()='Payee']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    create_check_options_payee_dd = (By.XPATH, "//div[contains(@class, 'option')]")
    create_check_payment_account_dd = (By.XPATH,"//label[text()='Payment Account *']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    create_check_options_payment_account_dd = (By.XPATH, "//div[contains(@class, 'option')]")
    create_check_payment_method_dd = (By.XPATH, "//select[@name='payment_method']")
    create_check_options_payment_method_dd = (By.XPATH, "//div[contains(@class, 'option')]")
    create_check_payee_address = (By.XPATH, "//label[contains(text(),'Mailing Address')]/following::input[@placeholder='Enter a location']")
    create_check_options_payee_address = (By.XPATH, "/html/body/div[2]")
    create_check_location_of_sale = (By.XPATH, "//label[contains(text(),'Location Of Sale *')]/following::input[@placeholder='Enter a location']")
    create_check_options_location_of_sale = (By.XPATH, "/html/body/div[2]")
    create_check_check_date = (By.XPATH, "//input[@name='payment_date']")
    create_check_check_date_datepicker_current_month_class = (By.CLASS_NAME, "react-datepicker__current-month")
    create_check_check_date_next_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--next")
    create_check_check_date_prev_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--previous")
    create_check_check_no = (By.XPATH, "//input[@name='bill_no']")
    create_check_category_details_add_new_lines_btn = (By.XPATH, "//div[@class='col-md-12 bg-white']//button[@id='zoom-secondary-outline-btn']")
    create_check_select_category_cao_dd = (By.XPATH, "//div[@class='row'][1]//table//tr//td[3]//input[contains(@id, 'react')]")
    create_check_options_category_cao_dd = (By.XPATH, "//div[contains(@class, 'option')]")
    create_check_category_descriptions = (By.XPATH, "//input[@name='description']")
    create_check_category_amount = (By.XPATH, "//input[@name='amount']")
    create_check_category_billable_chkbx = (By.XPATH, "//input[@id='flexCheckDefault1'] [@name='billable']")
    create_check_category_tax_chkbx = (By.XPATH, "//input[@id='flexCheckDefault1'] [@name='tax']")
    create_check_select_product_service_dd = (By.XPATH, "//div[@class='row'][2]//table//tr//td[2]")
    create_check_options_product_service_dd = (By.XPATH, "//div[contains(@class, 'option')]")
    create_check_item_details_qty = (By.XPATH, "//div[@class='row'][2]//table//tr//td[4]")
    create_check_item_details_rate = (By.XPATH, "//div[@class='row'][2]//table//tr//td[5]")
    create_check_item_details_amount = (By.XPATH, "//div[@class='row'][2]//table//tr//td[6]")
    create_check_item_details_total = (By.XPATH, "//div[@class='row'][2]//table//tr//td[7]")
    create_check_item_details_add_new_line_btn = (By.XPATH,"//div[@class='col-md-12 bg-white pt-3']//button[@id='zoom-secondary-outline-btn']")
    create_check_balance_txt = (By.XPATH, "//h5[1]//span[1]")
    create_check_memo = (By.XPATH, "//textarea[@name='memo']")
    create_check_btn_save_close = (By.XPATH, "//button[@id='zoom-primary-cancel-btn']")
    create_check_btn_save_new = (By.XPATH, "//button[normalize-space()='Save and New']")
    create_check_btn_cancel = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[1]")
    create_check_btn_clear = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[2]")
    create_check_btn_x = (By.XPATH,"//div[contains(@class, 'toast') and contains(@class, 'show')]//button[contains(@class, 'btn-close')]")

    # optional
    inv_btn_submod_Sales = (By.CSS_SELECTOR,
                            "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
    inv_btn_submod_invoice = (By.XPATH, "//a[@class='nav-link'][normalize-space()='Invoices']")
    inv_btn_create_invoice = (By.XPATH, "//button[normalize-space()='Create Invoice']")
    inv_dd_customer = (By.XPATH, "//*[@id='react-select-2-input']")
    inv_options_customer = By.XPATH, "//div[contains(@class, 'option')]"
    inv_btn_add_items = (By.XPATH, "//button[@class='btn btn-light sc-eqUAAy kJGDIg shadow-none']")
    inv_dd_select_product = (
        By.XPATH, "//div[contains(@class,'modal-content')]//div[contains(@class,'css-19bb58m')]//input")
    inv_options_select_productservice = (By.XPATH, "//div[contains(@class, 'option')]")
    inv_m_btn_x = (By.XPATH, "//div[@class='modal-header sc-kOHTFB ivaBOY']//button[@aria-label='Close']")

    def create_c_new(self):
        self.actions.wait_for_element(self.create_check_plus_new)
        self.actions.click(self.create_check_plus_new)

    def create_c_check(self):
        self.actions.wait_for_element(self.create_check_check)
        self.actions.click(self.create_check_check)

    def create_c_select_payee(self, create_check_test_data):
        self.actions.wait_for_element(self.create_check_payee_dd)
        self.actions.scroll_to_the_element(self.create_check_payee_dd)
        self.actions.dropdown_contains(self.create_check_payee_dd, self.create_check_options_payee_dd,
                                       create_check_test_data["check_payee"])

    def create_c_select_payment_account(self, create_check_test_data):
        self.actions.wait_for_element(self.create_check_payment_account_dd)
        self.actions.scroll_to_the_element(self.create_check_payment_account_dd)
        self.actions.dropdown_contains(self.create_check_payment_account_dd,
                                       self.create_check_options_payment_account_dd,
                                       create_check_test_data["check_payment_account"])

    def create_c_check_date(self, create_check_test_data):
        self.actions.wait_for_element(self.create_check_check_date)
        self.actions.scroll_to_the_element(self.create_check_check_date)
        self.actions.select_date(self.create_check_check_date,
                                 self.create_check_check_date_datepicker_current_month_class,
                                 self.create_check_check_date_next_btn_class,
                                 self.create_check_check_date_prev_btn_class,
                                 create_check_test_data["check_check_date"])

    def create_c_select_payment_method(self, create_check_test_data):
        self.actions.wait_for_element(self.create_check_payment_method_dd)
        self.actions.scroll_to_the_element(self.create_check_payment_method_dd)
        self.actions.dropdown_contains(self.create_check_payment_method_dd, self.create_check_options_payment_method_dd,
                                       create_check_test_data["check_payment_method"])

    def create_c_select_payment_2(self, create_check_test_data):
        self.actions.wait_for_element(self.create_check_payment_method_dd)
        self.actions.scroll_to_the_element(self.create_check_payment_method_dd)
        self.actions.dropdown_select(self.create_check_payment_method_dd,
                                     create_check_test_data["check_payment_method"])

    def create_c_check_no(self, create_check_test_data):
        self.actions.wait_for_element(self.create_check_check_no)
        self.actions.scroll_to_the_element(self.create_check_check_no)
        self.actions.send_keys(self.create_check_check_no, create_check_test_data["check_check_no"])

    def create_c_payee_address(self, create_check_test_data):
        self.actions.wait_for_element(self.create_check_payee_address)
        self.actions.scroll_to_the_element(self.create_check_payee_address)
        self.actions.dropdown_contains(self.create_check_payee_address, self.create_check_options_payee_address,
                                       create_check_test_data["check_payee_address"])

    def create_c_location_of_sale(self, create_check_test_data):
        self.actions.wait_for_element(self.create_check_location_of_sale)
        self.actions.scroll_to_the_element(self.create_check_location_of_sale)
        self.actions.dropdown_contains(self.create_check_location_of_sale, self.create_check_options_location_of_sale,
                                       create_check_test_data["check_location_of_sale"])

    def create_c_category_add_new_line_btn(self):
        self.actions.wait_for_element(self.create_check_category_details_add_new_lines_btn)
        self.actions.scroll_to_the_element(self.create_check_category_details_add_new_lines_btn)
        self.actions.click(self.create_check_category_details_add_new_lines_btn)
        time.sleep(2)

    def create_c_item_details_add_new_line_btn(self):
        self.actions.wait_for_element(self.create_check_item_details_add_new_line_btn)
        self.actions.scroll_to_the_element(self.create_check_item_details_add_new_line_btn)
        self.actions.click(self.create_check_item_details_add_new_line_btn)

    def create_c_item_details_amount(self):
        self.actions.wait_for_element(self.create_check_item_details_amount)
        self.actions.scroll_to_the_element(self.create_check_item_details_amount)
        displayed_amount = self.actions.get_text(self.create_check_item_details_amount)

    def create_c_item_details_total(self):
        self.actions.wait_for_element(self.create_check_item_details_total)
        self.actions.scroll_to_the_element(self.create_check_item_details_total)
        displayed_total = self.actions.get_text(self.create_check_item_details_total)

    def create_c_balance(self):
        self.actions.wait_for_element(self.create_check_balance_txt)
        self.actions.scroll_to_the_element(self.create_check_balance_txt)
        displayed_balance = self.actions.get_text(self.create_check_balance_txt)

    def create_c_memo(self, create_check_test_data):
        self.actions.wait_for_element(self.create_check_memo)
        self.actions.scroll_to_the_element(self.create_check_memo)
        self.actions.send_keys(self.create_check_memo, create_check_test_data["check_memo"])

    def create_c_cancel(self):
        self.actions.wait_for_element(self.create_check_btn_cancel)
        self.actions.scroll_to_the_element(self.create_check_btn_cancel)
        self.actions.click(self.create_check_btn_cancel)

    def create_c_clear(self):
        self.actions.wait_for_element(self.create_check_btn_clear)
        self.actions.scroll_to_the_element(self.create_check_btn_clear)
        self.actions.click(self.create_check_btn_clear)

    def create_c_save_and_close(self):
        self.actions.wait_for_element(self.create_check_btn_save_close)
        self.actions.scroll_to_the_element(self.create_check_btn_save_close)
        self.actions.click(self.create_check_btn_save_close)

    def create_c_save_and_new(self):
        self.actions.wait_for_element(self.create_check_btn_save_new)
        self.actions.scroll_to_the_element(self.create_check_btn_save_new)
        self.actions.click(self.create_check_btn_save_new)

    def create_c_x_button(self):
        self.actions.wait_for_element(self.create_check_btn_x)
        self.actions.scroll_to_the_element(self.create_check_btn_x)
        self.actions.click(self.create_check_btn_x)

    def create_c_add_multiple_category_cao_with_changexpath(self, create_check_test_data):
        category_coa_list = create_check_test_data["check_category_CAO"]
        category_coa_amount = create_check_test_data["check_category_amount"]

        for index, (category_cao, amount) in enumerate(zip(category_coa_list, category_coa_amount)):
            row_index = index + 1
            category_dropdown_locator = (
                By.XPATH,
                f"(//div[@class='row']//table//tr[{row_index}]//td[3]//input[contains(@id, 'react')])"
            )
            amount_field_locator = (
                By.XPATH,
                f"(//div[@class='row']//table//tr[{row_index}]//td[5]//input[contains(@name,'amount')])")

            self.actions.wait_for_element_clickable(category_dropdown_locator)
            self.actions.scroll_to_the_element(category_dropdown_locator)
            self.actions.dropdown_contains(category_dropdown_locator, self.create_check_options_category_cao_dd,
                                           category_cao)
            time.sleep(1)

            self.actions.wait_for_element(amount_field_locator)
            self.actions.clear_text(amount_field_locator)
            self.actions.send_keys(amount_field_locator, amount)
            time.sleep(1)

            if index < len(category_coa_list) - 1:
                self.actions.click(self.create_check_category_details_add_new_lines_btn)
                time.sleep(2)

    def create_c_add_multiple_product_cao_with_changexpath(self, create_check_test_data):
        product_serv_list = create_check_test_data["check_item_details_prod_serv"]
        product_serv_qty_list = create_check_test_data["check_item_details_qty"]
        product_serv_rate_list = create_check_test_data["check_item_details_rate"]

        for index, (product_serv, qty, rate) in enumerate(
                zip(product_serv_list, product_serv_qty_list, product_serv_rate_list)):
            row_index = index + 1
            product_serv_dropdown_locator = (
                By.XPATH,
                f"(//div[@class='row']//table//tr[{row_index}]//td[2]//input[contains(@id,'react')])"
            )
            qty_field_locator = (
                By.XPATH,
                f"(//div[@class='row']//table//tr[{row_index}]//td[4]//input[contains(@type, 'number')])"
            )
            rate_field_locator = (
                By.XPATH,
                f"(//div[@class='row'][5]//table//tr[{row_index}]//td[5]//input[contains(@type, 'number')])"
            )

            self.actions.wait_for_element_clickable(product_serv_dropdown_locator)
            self.actions.scroll_to_the_element(product_serv_dropdown_locator)
            self.actions.click(product_serv_dropdown_locator)
            time.sleep(2)
            self.actions.dropdown_contains(
                product_serv_dropdown_locator,
                self.create_check_options_product_service_dd,
                product_serv
            )
            time.sleep(1)

            self.actions.wait_for_element_clickable(qty_field_locator)
            self.actions.clear_text(qty_field_locator)
            self.actions.send_keys(qty_field_locator, qty)
            time.sleep(1)

            self.actions.wait_for_element_clickable(rate_field_locator)
            self.actions.clear_text(rate_field_locator)
            self.actions.send_keys(rate_field_locator, rate)
            time.sleep(1)

            if index < len(product_serv_list) - 1:
                self.actions.click(self.create_check_item_details_add_new_line_btn)
                time.sleep(2)

    def create_c_click_x_button(self):
        self.actions.wait_for_element(self.create_check_btn_x)
        self.actions.click(self.create_check_btn_x)
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
