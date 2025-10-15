import time
import datetime

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.actions import Actions

class CreateCOA:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 4)

    create_coa_accounting_module = (By.XPATH,"//img[@src='/svgs/accounting.svg']")
    create_coa_sub_module = (By.XPATH,"//a[normalize-space()='Charts of Accounts']")
    create_coa_new_btn = (By.XPATH,"//div[@id='coa-header-btns']//button[normalize-space(text())='New']")
    create_coa_select_accounting_type_dd = (By.XPATH,"//select[@name='account_type_id']")
    create_coa_options_select_accounting_type = (By.XPATH,"//select[@name='account_type_id']//option")
    create_coa_select_detail_typ_dd = (By.XPATH,"//select[@name='account_type_child_id']")
    create_coa_options_select_detail_type = (By.XPATH,"//select[@name='account_type_child_id']//option")
    create_coa_account_name = (By.XPATH,"//input[@name='name']")
    create_coa_account_number = (By.XPATH,"//input[@name='account_number']")
    create_coa_checkbox_subaccount = (By.XPATH,"//input[@id='flexCheckDefault']")
    create_coa_select_parent_account_dd = (By.XPATH,"//select[@name='sub_account_id']")
    create_coa_options_select_parent_account_dd  = (By.XPATH, "//select[@name='sub_account_id']//option")
    create_coa_opening_balance = (By.XPATH,"//input[@name='openning_balance']")
    create_coa_as_of_date = (By.XPATH, "//input[@name='started_tracking_since_date']")
    create_coa_datepicker_current_month_class = (By.CLASS_NAME, "react-datepicker__current-month")
    create_coa_next_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--next")
    create_coa_prev_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--previous")
    create_coa_description = (By.XPATH,"//input[@name='description']")
    create_coa_save_btn = (By.XPATH,"//button[normalize-space(text())='Save']")
    create_coa_cancel_btn = (By.XPATH,"//button[normalize-space(text())='Cancel']")
    create_coa_x_btn = (By.XPATH,"//div[@class='modal-header sc-kOHTFB ivaBOY']//button[@aria-label='Close']")

    def create_coa_accounting_modul_click(self):
        self.actions.wait_for_element(self.create_coa_accounting_module)
        self.actions.click(self.create_coa_accounting_module)

    def create_coa_submodule_click(self):
        self.actions.wait_for_element(self.create_coa_sub_module)
        self.actions.click(self.create_coa_sub_module)

    def create_coa_new_btn_click(self):
        self.actions.wait_for_element(self.create_coa_new_btn)
        self.actions.click(self.create_coa_new_btn)

    def create_coa_detail_type_dd(self, create_coa_test_data):
        self.actions.wait_for_element(self.create_coa_select_detail_typ_dd)
        self.actions.scroll_to_the_element(self.create_coa_select_detail_typ_dd)
        self.actions.dropdown_equals(self.create_coa_select_detail_typ_dd, self.create_coa_options_select_detail_type, create_coa_test_data["coa_detailed_type"])

    def create_coa_account_type_dd(self, create_coa_test_data):
        self.actions.wait_for_element(self.create_coa_select_accounting_type_dd)
        self.actions.scroll_to_the_element(self.create_coa_select_accounting_type_dd)
        self.actions.dropdown_equals(self.create_coa_select_accounting_type_dd, self.create_coa_options_select_accounting_type, create_coa_test_data["coa_account_type"])


    def create_coa_enter_account_name(self, create_coa_test_data):
        self.actions.wait_for_element(self.create_coa_account_name)
        self.actions.scroll_to_the_element(self.create_coa_account_name)
        cao_name = create_coa_test_data["cao_account_name"]
        self.actions.send_keys(self.create_coa_account_name, cao_name)
        return cao_name

    def create_coa_enter_account_number(self, create_coa_test_data):
        self.actions.wait_for_element(self.create_coa_account_number)
        self.actions.scroll_to_the_element(self.create_coa_account_number)
        self.actions.send_keys(self.create_coa_account_number,create_coa_test_data["cao_account_number"])


    def create_coa_check_box(self):
        self.actions.wait_for_element(self.create_coa_checkbox_subaccount)
        self.actions.scroll_to_the_element(self.create_coa_checkbox_subaccount)
        self.actions.click(self.create_coa_checkbox_subaccount)

    def create_coa_select_parent_account(self, create_coa_test_data):
        self.actions.wait_for_element(self.create_coa_select_parent_account_dd)
        self.actions.scroll_to_the_element(self.create_coa_select_parent_account_dd)
        self.actions.dropdown_equals(self.create_coa_select_parent_account_dd, self.create_coa_options_select_parent_account_dd, create_coa_test_data["coa_parent_account"])

    def create_coa_enter_opening_balance(self, create_coa_test_data):
        self.actions.wait_for_element(self.create_coa_opening_balance)
        self.actions.scroll_to_the_element(self.create_coa_opening_balance)
        self.actions.send_keys(self.create_coa_opening_balance, create_coa_test_data["cao_opening_balance"])

    def create_coa_select_as_of_date(self, create_coa_test_data):
        self.actions.wait_for_element(self.create_coa_as_of_date)
        self.actions.scroll_to_the_element(self.create_coa_as_of_date)
        self.actions.select_date(self.create_coa_as_of_date, self.create_coa_datepicker_current_month_class, self.create_coa_next_btn_class, self.create_coa_prev_btn_class,create_coa_test_data["coa_as_of_date"] )

    def create_coa_enter_description(self, create_coa_test_data):
        self.actions.wait_for_element(self.create_coa_description)
        self.actions.scroll_to_the_element(self.create_coa_description)
        self.actions.send_keys(self.create_coa_description, create_coa_test_data["cao_description"])

    def create_coa_click_save_btn(self):
        self.actions.wait_for_element(self.create_coa_save_btn)
        self.actions.scroll_to_the_element(self.create_coa_save_btn)
        self.actions.click(self.create_coa_save_btn)

    def page_refresh(self):
        self.driver.refresh()

    def create_coa_click_cancel_btn(self):
        self.actions.wait_for_element(self.create_coa_cancel_btn)
        self.actions.scroll_to_the_element(self.create_coa_cancel_btn)
        self.actions.click(self.create_coa_cancel_btn)

















