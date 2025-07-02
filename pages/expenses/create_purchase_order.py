import logging
import time

from selenium.common import StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unicodedata import category

from actions.actions import Actions
from tests.conftest import create_purchase_order_test_data
from tests.conftest import create_invoice_test_data
class Create_Purchase_Order:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 50)

    create_purchase_order_plus_new = (By.XPATH, "//button[@class='pe-5 ps-5 btn btn-sm m-3 m-3']")
    create_purchase_order_purchase_order = (By.XPATH, "//a[normalize-space()='Purchase order']")
    create_purchase_order_payee_dd = (By.XPATH, "//label[text()='Vendor *']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    create_purchase_order_options_payee_dd = (By.XPATH, "//div[contains(@class, 'option')]")
    create_purchase_order_payee_email = (By.XPATH,"//input[@name='email']")
    create_purchase_order_mailing_address = (By.XPATH, "//label[contains(text(),'Payee address *')]/following::input[@placeholder='Enter a location']")
    create_purchase_order_options_mailing_address = (By.XPATH, "/html/body/div[2]")
    create_purchase_order_shipping_address = (By.XPATH, "//label[contains(text(),'Location Of Sale *')]/following::input[@placeholder='Enter a location']")
    create_purchase_order_options_shipping_address = (By.XPATH, "/html/body/div[2]")
    create_purchase_order_purchase_order_date = (By.XPATH, "//input[@name='purchase_order_date']")
    create_purchase_order_purchase_order_date_datepicker_current_month_class = (By.CLASS_NAME, "react-datepicker__current-month")
    create_purchase_order_purchase_order_date_next_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--next")
    create_purchase_order_purchase_order_date_prev_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--previous")
    create_purchase_order_purchase_order_no = (By.XPATH, "//input[@name='purchase_order_no']")
    create_purchase_order_category_details_add_new_lines_btn = (By.XPATH, "//div[@class='col-md-12 bg-white']//button[@id='zoom-secondary-outline-btn']")
    create_purchase_order_select_category_cao_dd = (By.XPATH, "//div[@class='row'][1]//table//tr//td[3]//input[contains(@id, 'react')]")
    create_purchase_order_options_category_cao_dd = (By.XPATH, "//div[contains(@class, 'option')]")
    create_purchase_order_category_descriptions = (By.XPATH, "//input[@name='description']")
    create_purchase_order_category_amount = (By.XPATH, "//input[@name='amount']")
    create_purchase_order_category_billable_chkbx = (By.XPATH, "//input[@id='flexCheckDefault1'] [@name='billable']")
    create_purchase_order_category_tax_chkbx = (By.XPATH, "//input[@id='flexCheckDefault1'] [@name='tax']")
    create_purchase_order_select_product_service_dd = (By.XPATH, "//div[@class='row'][2]//table//tr//td[2]")
    create_purchase_order_options_product_service_dd = (By.XPATH, "//div[contains(@class, 'option')]")
    create_purchase_order_item_details_qty = (By.XPATH, "//div[@class='row'][2]//table//tr//td[4]")
    create_purchase_order_item_details_rate = (By.XPATH, "//div[@class='row'][2]//table//tr//td[5]")
    create_purchase_order_item_details_amount = (By.XPATH, "//div[@class='row'][2]//table//tr//td[6]")
    create_purchase_order_item_details_total = (By.XPATH, "//div[@class='row'][2]//table//tr//td[7]")
    create_purchase_order_item_details_add_new_line_btn = (By.XPATH, "//div[@class='col-md-12 bg-white pt-3']//button[@id='zoom-secondary-outline-btn']")
    create_purchase_order_balance_txt = (By.XPATH, "//h5[1]//span[1]")
    create_purchase_order_memo = (By.XPATH, "//textarea[@name='memo']")
    create_purchase_order_btn_save_close = (By.XPATH, "//button[@id='zoom-primary-cancel-btn']")
    create_purchase_order_btn_save_new = (By.XPATH, "//button[normalize-space()='Save and New']")
    create_purchase_order_btn_cancel = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[1]")
    create_purchase_order_btn_clear = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[2]")
    create_purchase_order_btn_x = (By.XPATH, "//div[contains(@class, 'toast') and contains(@class, 'show')]//button[contains(@class, 'btn-close')]")

    # optional
    inv_btn_submod_Sales = (By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
    inv_btn_submod_invoice = (By.XPATH, "//a[@class='nav-link'][normalize-space()='Invoices']")
    inv_btn_create_invoice = (By.XPATH, "//button[normalize-space()='Create Invoice']")
    inv_dd_customer = (By.XPATH, "//*[@id='react-select-2-input']")
    inv_options_customer = By.XPATH, "//div[contains(@class, 'option')]"
    inv_btn_add_items = (By.XPATH, "//button[@class='btn btn-light sc-eqUAAy kJGDIg shadow-none']")
    inv_dd_select_product = (By.XPATH, "//div[contains(@class,'modal-content')]//div[contains(@class,'css-19bb58m')]//input")
    inv_options_select_productservice = (By.XPATH, "//div[contains(@class, 'option')]")
    inv_m_btn_x = (By.XPATH, "//div[@class='modal-header sc-kOHTFB ivaBOY']//button[@aria-label='Close']")

    def create_po_new(self):
        self.actions.wait_for_element(self.create_purchase_order_plus_new)
        self.actions.click(self.create_purchase_order_plus_new)

    def create_po_purchase_order(self):
        self.actions.wait_for_element(self.create_purchase_order_purchase_order)
        self.actions.click(self.create_purchase_order_purchase_order)

    def create_po_select_payee(self, create_purchase_order_test_data):
        self.actions.wait_for_element(self.create_purchase_order_payee_dd)
        self.actions.scroll_to_the_element(self.create_purchase_order_payee_dd)
        self.actions.dropdown_equals(self.create_purchase_order_payee_dd, self.create_purchase_order_options_payee_dd,
                                     create_purchase_order_test_data["purchase_order_payee"])

    def create_po_payee_email(self, create_purchase_order_test_data):
        self.actions.wait_for_element(self.create_purchase_order_payee_email)
        self.actions.scroll_to_the_element(self.create_purchase_order_payee_email)
        self.actions.send_keys(self.create_purchase_order_payee_email,
                               create_purchase_order_test_data[""])



    def create_po_mailing_address(self, create_purchase_order_test_data):
        self.actions.wait_for_element(self.create_purchase_order_mailing_address)
        self.actions.scroll_to_the_element(self.create_purchase_order_mailing_address)
        self.actions.dropdown_contains(self.create_purchase_order_mailing_address,
                                       self.create_purchase_order_options_mailing_address,
                                       create_purchase_order_test_data["purchase_order_mailing_address"])

    def create_po_shipping_address(self, create_purchase_order_test_data):
        self.actions.wait_for_element(self.create_purchase_order_shipping_address)
        self.actions.scroll_to_the_element(self.create_purchase_order_shipping_address)
        self.actions.dropdown_contains(self.create_purchase_order_shipping_address,
                                       self.create_purchase_order_options_shipping_address,
                                       create_purchase_order_test_data["purchase_order_shipping_address"])

    def create_po_purchase_order_date(self, create_purchase_order_test_data):
        self.actions.wait_for_element(self.create_purchase_order_purchase_order_date)
        self.actions.scroll_to_the_element(self.create_purchase_order_purchase_order_date)
        self.actions.select_date(self.create_purchase_order_purchase_order_date,
                                 self.create_purchase_order_purchase_order_date_datepicker_current_month_class,
                                 self.create_purchase_order_purchase_order_date_next_btn_class,
                                 self.create_purchase_order_purchase_order_date_prev_btn_class,
                                 create_purchase_order_test_data["purchase_order_date"])

    def create_po_purchase_order_no(self, create_purchase_order_test_data):
        self.actions.wait_for_element(self.create_purchase_order_purchase_order_no)
        self.actions.scroll_to_the_element(self.create_purchase_order_purchase_order_no)
        self.actions.send_keys(self.create_purchase_order_purchase_order_no,
                               create_purchase_order_test_data["purchase_order_no"])

    def create_po_category_add_new_line_btn(self):
        self.actions.wait_for_element(self.create_purchase_order_category_details_add_new_lines_btn)
        self.actions.scroll_to_the_element(self.create_purchase_order_category_details_add_new_lines_btn)
        self.actions.click(self.create_purchase_order_category_details_add_new_lines_btn)
        time.sleep(2)

    def create_po_category_select_category_cao(self, create_purchase_order_test_data):
        self.actions.wait_for_element(self.create_purchase_order_select_category_cao_dd)
        self.actions.scroll_to_the_element(self.create_purchase_order_select_category_cao_dd)
        self.actions.dropdown_contains(self.create_purchase_order_select_category_cao_dd,
                                       self.create_purchase_order_options_category_cao_dd,
                                       create_purchase_order_test_data["purchase_order_category_CAO"])

    def create_po_category_amount(self, create_purchase_order_test_data):
        self.actions.wait_for_element(self.create_purchase_order_category_amount)
        self.actions.scroll_to_the_element(self.create_purchase_order_category_amount)
        self.actions.send_keys(self.create_purchase_order_category_amount,
                               create_purchase_order_test_data["purchase_order_category_amount"])

    def create_po_category_billable(self, create_purchase_order_test_data):
        self.actions.wait_for_element(self.create_purchase_order_category_billable_chkbx)
        self.actions.scroll_to_the_element(self.create_purchase_order_category_billable_chkbx)
        self.actions.click(self.create_purchase_order_category_billable_chkbx)

    def create_po_category_tax(self, create_purchase_order_test_data):
        self.actions.wait_for_element(self.create_purchase_order_category_tax_chkbx)
        self.actions.scroll_to_the_element(self.create_purchase_order_category_tax_chkbx)
        self.actions.click(self.create_purchase_order_category_tax_chkbx)

    def create_po_item_details_add_new_line_btn(self):
        self.actions.wait_for_element(self.create_purchase_order_item_details_add_new_line_btn)
        self.actions.scroll_to_the_element(self.create_purchase_order_item_details_add_new_line_btn)
        self.actions.click(self.create_purchase_order_item_details_add_new_line_btn)

    def create_po_item_details_select_product_serv(self, create_purchase_order_test_data):
        self.actions.wait_for_element(self.create_purchase_order_select_product_service_dd)
        self.actions.scroll_to_the_element(self.create_purchase_order_select_product_service_dd)
        self.actions.dropdown_contains(self.create_purchase_order_select_product_service_dd,
                                       self.create_purchase_order_options_product_service_dd,
                                       create_purchase_order_test_data["purchase_order_item_details_prod_serv"])

    def create_po_item_details_qty(self, create_purchase_order_test_data):
        self.actions.wait_for_element(self.create_purchase_order_item_details_qty)
        self.actions.scroll_to_the_element(self.create_purchase_order_item_details_qty)
        self.actions.send_keys(self.create_purchase_order_item_details_qty,
                               create_purchase_order_test_data["purchase_order_item_details_qty"])

    def create_po_item_details_rate(self, create_purchase_order_test_data):
        self.actions.wait_for_element(self.create_purchase_order_item_details_rate)
        self.actions.scroll_to_the_element(self.create_purchase_order_item_details_rate)
        self.actions.send_keys(self.create_purchase_order_item_details_rate,
                               create_purchase_order_test_data["purchase_order_item_details_rate"])

    def create_po_item_details_amount(self):
        self.actions.wait_for_element(self.create_purchase_order_item_details_amount)
        self.actions.scroll_to_the_element(self.create_purchase_order_item_details_amount)
        displayed_amount = self.actions.get_text(self.create_purchase_order_item_details_amount)

    def create_po_item_details_total(self):
        self.actions.wait_for_element(self.create_purchase_order_item_details_total)
        self.actions.scroll_to_the_element(self.create_purchase_order_item_details_total)
        displayed_total = self.actions.get_text(self.create_purchase_order_item_details_total)

    def create_po_balance(self):
        self.actions.wait_for_element(self.create_purchase_order_balance_txt)
        self.actions.scroll_to_the_element(self.create_purchase_order_balance_txt)
        displayed_balance = self.actions.get_text(self.create_purchase_order_balance_txt)

    def create_po_memo(self, create_purchase_order_test_data):
        self.actions.wait_for_element(self.create_purchase_order_memo)
        self.actions.scroll_to_the_element(self.create_purchase_order_memo)
        self.actions.send_keys(self.create_purchase_order_memo, create_purchase_order_test_data["purchase_order_memo"])

    def create_po_cancel(self):
        self.actions.wait_for_element(self.create_purchase_order_btn_cancel)
        self.actions.scroll_to_the_element(self.create_purchase_order_btn_cancel)
        self.actions.click(self.create_purchase_order_btn_cancel)

    def create_po_clear(self):
        self.actions.wait_for_element(self.create_purchase_order_btn_clear)
        self.actions.scroll_to_the_element(self.create_purchase_order_btn_clear)
        self.actions.click(self.create_purchase_order_btn_clear)

    def create_po_save_and_close(self):
        self.actions.wait_for_element(self.create_purchase_order_btn_save_close)
        self.actions.scroll_to_the_element(self.create_purchase_order_btn_save_close)
        self.actions.click(self.create_purchase_order_btn_save_close)

    def create_po_save_and_new(self):
        self.actions.wait_for_element(self.create_purchase_order_btn_save_new)
        self.actions.scroll_to_the_element(self.create_purchase_order_btn_save_new)
        self.actions.click(self.create_purchase_order_btn_save_new)

    def create_po_x_button(self):
        self.actions.wait_for_element(self.create_purchase_order_btn_x)
        self.actions.scroll_to_the_element(self.create_purchase_order_btn_x)
        self.actions.click(self.create_purchase_order_btn_x)

    def create_po_add_multiple_category_cao_with_changexpath(self, create_purchase_order_test_data):
        category_coa_list = create_purchase_order_test_data["purchase_order_category_CAO"]
        category_coa_amount = create_purchase_order_test_data["purchase_order_category_amount"]

        for index, (category_cao, amount) in enumerate(zip(category_coa_list, category_coa_amount)):
            row_index = index + 1

            category_dropdown_locator = (
                By.XPATH,
                f"(//div[@class='row']//table//tr[{row_index}]//td[3]//input[contains(@id, 'react')])"
            )

            amount_field_locator = (
                By.XPATH,
                f"(//div[@class='row']//table//tr[{row_index}]//td[5]//input[contains(@name,'amount')])"
            )

            self.actions.wait_for_element_clickable(category_dropdown_locator)
            self.actions.scroll_to_the_element(category_dropdown_locator)
            self.actions.dropdown_contains(
                category_dropdown_locator,
                self.create_purchase_order_options_category_cao_dd,
                category_cao
            )
            time.sleep(1)

            self.actions.wait_for_element(amount_field_locator)
            self.actions.clear_text(amount_field_locator)
            self.actions.send_keys(amount_field_locator, amount)
            time.sleep(1)

            if index < len(category_coa_list) - 1:
                self.actions.click(self.create_purchase_order_category_details_add_new_lines_btn)
                time.sleep(2)

    def create_po_add_multiple_product_cao_with_changexpath(self, create_purchase_order_test_data):
        product_serv_list = create_purchase_order_test_data["purchase_order_item_details_prod_serv"]
        product_serv_qty_list = create_purchase_order_test_data["purchase_order_item_details_qty"]
        product_serv_rate_list = create_purchase_order_test_data["purchase_order_item_details_rate"]

        for index, (product_serv, qty, rate) in enumerate(
                zip(product_serv_list, product_serv_qty_list, product_serv_rate_list)):
            row_index = index + 1

            product_serv_dropdown_locator = (
                By.XPATH,
                f"(//div[contains(@class,'row')]//table//tr[{row_index}]//td[2]//input[contains(@id,'react')])"
            )

            qty_field_locator = (
                By.XPATH,
                f"(//div[contains(@class,'row')]//table//tr[{row_index}]//td[4]//input[contains(@type, 'number')])"
            )

            rate_field_locator = (
                By.XPATH,
                f"(//div[contains(@class,'row')]//table//tr[{row_index}]//td[5]//input[contains(@type, 'number')])"
            )

            self.actions.wait_for_element_clickable(product_serv_dropdown_locator)
            self.actions.scroll_to_the_element(product_serv_dropdown_locator)
            self.actions.click(product_serv_dropdown_locator)
            time.sleep(2)
            self.actions.dropdown_contains(
                product_serv_dropdown_locator,
                self.create_purchase_order_options_product_service_dd,
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
                self.actions.click(self.create_purchase_order_item_details_add_new_line_btn)
                time.sleep(2)

    def create_po_click_x_button(self):
        self.actions.wait_for_element(self.create_purchase_order_btn_x)
        self.actions.click(self.create_purchase_order_btn_x)
        time.sleep(2)

    # optional
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
        self.actions.dropdown_equals(self.inv_dd_customer, self.inv_options_customer,
                                     create_invoice_test_data["customer_name"])

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
