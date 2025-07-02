import logging
import time

from selenium.common import StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unicodedata import category

from actions.actions import Actions
from tests.conftest import create_expense_test_data
from tests.conftest import create_invoice_test_data

class Create_Expense:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 50)

    create_expense_plus_new = (By.XPATH,"//button[@class='pe-5 ps-5 btn btn-sm m-3 m-3']")
    create_expense_expense= (By.XPATH, "//a[normalize-space()='Expense']")
    create_expense_payee_dd = (By.XPATH,"//label[text()='Payee *']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    create_expense_options_payee_dd = (By.XPATH,"//div[contains(@class, 'option')]")
    create_expense_payment_account_dd =(By.XPATH,"//label[text()='Payment Account *']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    create_expense_options_payment_account_dd = (By.XPATH,"//div[contains(@class, 'option')]")
    create_expense_payment_method_dd = (By.XPATH,"//select[@name='payment_method']")
    create_expense_options_payment_method_dd = (By.XPATH,"//div[contains(@class, 'option')]")
    create_expense_payee_address = (By.XPATH,"//label[contains(text(),'Payee address *')]/following::input[@placeholder='Enter a location']")
    create_expense_options_payee_address = (By.XPATH, "/html/body/div[2]")
    create_expense_location_of_sale = (By.XPATH, "//label[contains(text(),'Location Of Sale *')]/following::input[@placeholder='Enter a location']")
    create_expense_options_location_of_sale = (By.XPATH, "/html/body/div[2]")
    create_expense_expense_date = (By.XPATH, "//input[@name='payment_date']")
    create_expense_expense_date_datepicker_current_month_class = (By.CLASS_NAME,"react-datepicker__current-month")
    create_expense_expensel_date_next_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--next")
    create_expense_expense_date_prev_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--previous")
    create_expense_expense_no = (By.XPATH,"//input[@name='expense_no']")
    create_expense_category_details_add_new_lines_btn = (By.XPATH,"//div[@class='container-fluid']//div[1]//div[2]//table[1]//thead[2]//tr[1]//th[1]//button[1]")
    create_expense_select_category_cao_dd = (By.XPATH,"//div[@class='row'][1]//table//tr//td[3]//input[contains(@id, 'react')]")
    create_expense_options_category_cao_dd = (By.XPATH, "//div[contains(@class, 'option')]")
    create_expense_category_descriptions = (By.XPATH,"//input[@name='description']")
    create_expense_category_amount = (By.XPATH,"//input[@name='amount']")
    create_expense_category_billable_chkbx = (By.XPATH,"//input[@id='flexCheckDefault1'] [@name='billable']")
    create_expense_category_tax_chkbx = (By.XPATH,"//input[@id='flexCheckDefault1'] [@name='tax']")
    create_bill_item_details_add_new_line_btn= (By.XPATH,"//div[@class='body flex-grow-1 px-3 mb-5']//div[2]//div[2]//table[1]//thead[2]//tr[1]//th[1]//button[1]")
    create_expense_select_product_service_dd = (By.XPATH, "//div[@class='row'][2]//table//tr//td[2]")
    create_expense_options_product_service_dd = (By.XPATH, "//div[contains(@class, 'option')]")
    create_expense_item_details_qty = (By.XPATH,"//div[@class='row'][2]//table//tr//td[4]")
    create_expense_item_details_rate = (By.XPATH,"//div[@class='row'][2]//table//tr//td[5]")
    create_expense_item_details_amount = (By.XPATH,"//div[@class='row'][2]//table//tr//td[6]")
    create_expense_item_details_total = (By.XPATH,"//div[@class='row'][2]//table//tr//td[7]")
    create_expense_item_details_add_new_line_btn= (By.XPATH,"//div[@class='body flex-grow-1 px-3 mb-5']//div[2]//div[2]//table[1]//thead[2]//tr[1]//th[1]//button[1]")
    create_expense_balance_txt = (By.XPATH,"//h5[1]//span[1]")
    create_expense_memo= (By.XPATH,"//textarea[@name='memo']")
    create_expense_btn_save_close = (By.XPATH, "//button[@id='zoom-primary-cancel-btn']")
    create_expense_btn_save_new = (By.XPATH, "//button[normalize-space()='Save and New']")
    create_expense_btn_cancel = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[1]")
    create_expense_btn_clear = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[2]")
    create_expense_btn_x = (By.XPATH, "//div[contains(@class, 'toast') and contains(@class, 'show')]//button[contains(@class, 'btn-close')]")

    # optional
    inv_btn_submod_Sales = (By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
    inv_btn_submod_invoice = (By.XPATH, "//a[@class='nav-link'][normalize-space()='Invoices']")
    inv_btn_create_invoice = (By.XPATH, "//button[normalize-space()='Create Invoice']")
    inv_dd_customer = (By.XPATH, "//*[@id='react-select-2-input']")
    inv_options_customer = By.XPATH, "//div[contains(@class, 'option')]"
    inv_btn_add_items = (By.XPATH, "//button[@class='btn btn-light sc-eqUAAy kJGDIg shadow-none']")
    inv_dd_select_product = (By.XPATH, "//div[contains(@class,'modal-content')]//div[contains(@class,'css-19bb58m')]//input")
    inv_options_select_productservice = (By.XPATH, "//div[contains(@class, 'option')]")
    inv_m_btn_x = (By.XPATH, "//div[@class='modal-header sc-kOHTFB ivaBOY']//button[@aria-label='Close']")

    def create_e_new(self):
        self.actions.wait_for_element(self.create_expense_plus_new)
        self.actions.click(self.create_expense_plus_new)

    def create_e_expense(self):
        self.actions.wait_for_element(self.create_expense_expense)
        self.actions.click(self.create_expense_expense)

    def create_e_select_payee(self,create_expense_test_data ):
        self.actions.wait_for_element(self.create_expense_payee_dd)
        self.actions.scroll_to_the_element(self.create_expense_payee_dd)
        self.actions.dropdown_contains(self.create_expense_payee_dd, self.create_expense_options_payee_dd,create_expense_test_data["expense_payee"])

    def create_e_select_payment_account(self,create_expense_test_data ):
        self.actions.wait_for_element(self.create_expense_payment_account_dd)
        self.actions.scroll_to_the_element(self.create_expense_payment_account_dd)
        self.actions.dropdown_contains(self.create_expense_payment_account_dd, self.create_expense_options_payment_account_dd,create_expense_test_data["expense_payment_account"])

    def create_e_expense_date(self, create_expense_test_data):
        self.actions.wait_for_element(self.create_expense_expense_date)
        self.actions.scroll_to_the_element(self.create_expense_expense_date)
        self.actions.select_date(self.create_expense_expense_date, self.create_expense_expense_date_datepicker_current_month_class,self.create_expense_expensel_date_next_btn_class, self.create_expense_expense_date_prev_btn_class,create_expense_test_data["expense_expense_date"])

    def create_e_select_payment_method(self,create_expense_test_data ):
        self.actions.wait_for_element(self.create_expense_payment_method_dd)
        self.actions.scroll_to_the_element(self.create_expense_payment_method_dd)
        self.actions.dropdown_contains(self.create_expense_payment_method_dd, self.create_expense_options_payment_method_dd,create_expense_test_data["expense_payment_method"])

    def create_e_select_payment_2(self,create_expense_test_data):
        self.actions.wait_for_element(self.create_expense_payment_method_dd)
        self.actions.scroll_to_the_element(self.create_expense_payment_method_dd)
        self.actions.dropdown_select(self.create_expense_payment_method_dd,create_expense_test_data["expense_payment_method"])

    def create_e_ref_no(self, create_expense_test_data):
        self.actions.wait_for_element(self.create_expense_expense_no)
        self.actions.scroll_to_the_element(self.create_expense_expense_no)
        self.actions.send_keys(self.create_expense_expense_no, create_expense_test_data["expense_ref_no"])

    def create_e_payee_address(self, create_expense_test_data):
        self.actions.wait_for_element(self.create_expense_payee_address)
        self.actions.scroll_to_the_element(self.create_expense_payee_address)
        self.actions.dropdown_contains(self.create_expense_payee_address, self.create_expense_options_payee_address, create_expense_test_data["expense_payee_address"])

    def create_e_location_of_sale(self, create_expense_test_data):
        self.actions.wait_for_element(self.create_expense_location_of_sale)
        self.actions.scroll_to_the_element(self.create_expense_location_of_sale)
        self.actions.dropdown_contains(self.create_expense_location_of_sale, self.create_expense_options_location_of_sale, create_expense_test_data["expense_location_of_sale"])


    def create_e_category_add_new_line_btn(self):
        self.actions.wait_for_element(self.create_expense_category_details_add_new_lines_btn)
        self.actions.scroll_to_the_element(self.create_expense_category_details_add_new_lines_btn)
        self.actions.click(self.create_expense_category_details_add_new_lines_btn)
        time.sleep(2)

    def create_e_item_details_add_new_line_btn(self):
        self.actions.wait_for_element(self.create_expense_item_details_add_new_line_btn)
        self.actions.scroll_to_the_element(self.create_expense_item_details_add_new_line_btn)
        self.actions.click(self.create_expense_item_details_add_new_line_btn)

    def create_e_item_details_amount(self):
        self.actions.wait_for_element(self.create_expense_item_details_amount)
        self.actions.scroll_to_the_element(self.create_expense_item_details_amount)
        displayed_amount = self.actions.get_text(self.create_expense_item_details_amount)

    def create_e_item_details_total(self):
        self.actions.wait_for_element(self.create_expense_item_details_total)
        self.actions.scroll_to_the_element(self.create_expense_item_details_total)
        displayed_total = self.actions.get_text(self.create_expense_item_details_total)

    def create_e_balance(self):
        self.actions.wait_for_element(self.create_expense_balance_txt)
        self.actions.scroll_to_the_element(self.create_expense_balance_txt)
        displayed_balance = self.actions.get_text(self.create_expense_balance_txt)

    def create_e_memo(self, create_expense_test_data):
        self.actions.wait_for_element(self.create_expense_memo)
        self.actions.scroll_to_the_element(self.create_expense_memo)
        self.actions.send_keys(self.create_expense_memo, create_expense_test_data["expense_memo"])

    def create_e_cancel(self):
        self.actions.wait_for_element(self.create_expense_btn_cancel)
        self.actions.scroll_to_the_element(self.create_expense_btn_cancel)
        self.actions.click(self.create_expense_btn_cancel)

    def create_e_clear(self):
        self.actions.wait_for_element(self.create_expense_btn_clear)
        self.actions.scroll_to_the_element(self.create_expense_btn_clear)
        self.actions.click(self.create_expense_btn_clear)

    def create_e_save_and_close(self):
        self.actions.wait_for_element(self.create_expense_btn_save_close)
        self.actions.scroll_to_the_element(self.create_expense_btn_save_close)
        self.actions.click(self.create_expense_btn_save_close)

    def create_e_save_and_new(self):
        self.actions.wait_for_element(self.create_expense_btn_save_new)
        self.actions.scroll_to_the_element(self.create_expense_btn_save_new)
        self.actions.click(self.create_expense_btn_save_new)

    def create_e_x_button(self):
        self.actions.wait_for_element(self.create_expense_btn_x)
        self.actions.scroll_to_the_element(self.create_expense_btn_x)
        self.actions.click(self.create_expense_btn_x)

    def create_e_add_multiple_category_cao_with_changexpath(self, create_expense_test_data):
        category_coa_list = create_expense_test_data["expense_category_CAO"]
        category_coa_amount = create_expense_test_data["expense_category_amount"]

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
                f"(//div[@class='row'][1]//table//tr[{row_index}]//td[5]//input[contains(@name,'amount')])")
            # 1. Handle Category Dropdown
            self.actions.wait_for_element_clickable(category_dropdown_locator)
            self.actions.scroll_to_the_element(category_dropdown_locator)
            self.actions.dropdown_contains(category_dropdown_locator,self.create_expense_options_category_cao_dd,category_cao)
            time.sleep(1)  # Short pause
            # 2. Enter Amount
            self.actions.wait_for_element(amount_field_locator)
            self.actions.clear_text(amount_field_locator)
            self.actions.send_keys(amount_field_locator, amount)
            time.sleep(1)  # Short pause

            # 3. Add new line if needed
            if index < len(category_coa_list) - 1:
                self.actions.click(self.create_expense_category_details_add_new_lines_btn)
                time.sleep(2)  # Wait for new row to render

    def create_e_add_multiple_product_cao_with_changexpath(self, create_expense_test_data):
        product_serv_list = create_expense_test_data["expense_item_details_prod_serv"]
        product_serv_qty_list = create_expense_test_data["expense_item_details_qty"]
        product_serv_rate_list = create_expense_test_data["expense_item_details_rate"]

        for index, (product_serv, qty, rate) in enumerate(
                zip(product_serv_list, product_serv_qty_list, product_serv_rate_list)):
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
                self.create_expense_options_product_service_dd,
                product_serv
            )
            time.sleep(1)  # Short pause

            # 2. Enter qty
            self.actions.wait_for_element_clickable(qty_field_locator)
            self.actions.clear_text(qty_field_locator)
            self.actions.send_keys(qty_field_locator, qty)
            time.sleep(1)  # Short pause

            # 2. Enter rate
            self.actions.wait_for_element_clickable(rate_field_locator)
            self.actions.clear_text(rate_field_locator)
            self.actions.send_keys(rate_field_locator, rate)
            time.sleep(1)  # Short pause

            # 3. Add new line if needed
            if index < len(product_serv_list) - 1:
                self.actions.click(self.create_expense_item_details_add_new_line_btn)
                time.sleep(2)  # Wait for new row to render

    def create_e_click_x_button(self):
        self.actions.wait_for_element(self.create_expense_btn_x)
        self.actions.click(self.create_expense_btn_x)
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







