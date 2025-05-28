import logging
import time

import pytest
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.core import driver
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.conftest import create_refund_receipt_test_data

from actions.actions import Actions


class RefundReceipt:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)

    refund_r_plus_new = (By.XPATH, "//button[@class='pe-5 ps-5 btn btn-sm m-3 m-3']")
    refund_r_refund_receipt = (By.XPATH, "//a[normalize-space()='Refund Receipt']")
    refund_r_select_customer = (By.ID, "react-select-2-input")
    refund_r_options_customer = (By.XPATH, "//div[contains(@class, 'option')]")
    refund_r_cust_email = (By.XPATH, "//input[@label='Customer Email']")
    refund_r_billing_address = (By.XPATH, "//label[contains(text(),'Billing')]/following::input[@placeholder='Enter a location']")
    refund_r_options_billing = (By.XPATH, "/html/body/div[3]/div")
    refund_r_shipping_address = (By.XPATH, "//label[contains(text(),'Shipping')]/following::input[@placeholder='Enter a location']")
    refund_r_options_shipping = (By.XPATH, "/html/body/div[4]/div")
    refund_r_location_of_sale = (By.XPATH, "//label[contains(text(),'Location Of Sale')]/following::input[@placeholder='Enter a location']")
    refund_r_options_location_of_sale = (By.XPATH, "/html/body/div[5]/div")
    refund_r_refund_receipt_date = (By.XPATH, "//input[@name='refund_receipt_date']")
    refund_r_current_month = (By.CLASS_NAME, "react-datepicker__current-month")
    refund_r_dt_next_btn_class = (By.XPATH, "react-datepicker__navigation--next")
    refund_r_dt_prev_btn_class = (By.XPATH, "react-datepicker__navigation--previous")
    refund_r_refund_receipt_no = (By.XPATH, "//input[@name='refund_receipt_no']")
    refund_r_payment_method = (By.ID,"react-select-3-input")
    refund_r_options_payment_method = (By.XPATH,"//div[contains(@class, 'option')]")
    refund_r_refund_from = (By.ID, "react-select-5-input")
    refund_r_options_refund_from = (By.XPATH, "//div[contains(@class, 'option')]")
    refund_r_select_transactions = (By.ID, "react-select-10-input")
    refund_r_options_transactions = (By.XPATH, "//div[contains(@class, 'option')]")
    refund_r_add_new_lines = (By.XPATH, "//button[@id='zoom-secondary-outline-btn']")
    refund_r_select_product_service = (By.ID, "react-select-10-input")
    refund_r_options_product_service = (By.XPATH, "//div[contains(@class, 'option')]")
    refund_r_product_qty = (By.XPATH, "//table//tbody//td[4]//input")
    refund_r_product_rate = (By.XPATH, "//table//tbody//td[5]//input")
    refund_r_product_amount = (By.XPATH, "//table//tbody//td[6]//input")
    refund_r_product_tax = (By.XPATH, "//table//tbody//td[7]//input")
    refund_r_product_total = (By.XPATH, "//table//tbody//td[7]//input")
    refund_r_txt_sub_total = (By.XPATH, "//h5[1]//span[1]")
    refund_r_txt_total_tax = (By.XPATH, "//div[@class='col-md-6']//h5[2]//span[1]")
    refund_r_balance = (By.XPATH, "//h5[3]//span[1]")
    refund_r_memo = (By.XPATH, "//textarea[@name='memo']")
    refund_r_btn_save_close = (By.XPATH, "//button[@id='zoom-primary-cancel-btn']")
    refund_r_btn_save_new = (By.XPATH, "//button[normalize-space()='Save and New']")
    refund_r_btn_cancel = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[1]")
    refund_r_btn_clear = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[2]")
    refund_r_btn_x = (By.XPATH, "//div[contains(@class, 'toast') and contains(@class, 'show')]//button[contains(@class, 'btn-close')]")

    def rr_plus_new(self):
        self.actions.wait_for_element(self.refund_r_plus_new)
        self.actions.click(self.refund_r_plus_new)

    def rr_refund_receipt(self):
        self.actions.wait_for_element(self.refund_r_refund_receipt )
        self.actions.click(self.refund_r_refund_receipt)

    def rr_select_customer(self, create_refund_receipt_test_data):
        self.actions.wait_for_element(self.refund_r_select_customer)
        self.actions.scroll_to_the_element(self.refund_r_select_customer)
        self.actions.dropdown_equals(self.refund_r_select_customer, self.refund_r_options_customer,create_refund_receipt_test_data["rr_customer"])

    def rr_email(self, create_refund_receipt_test_data):
        self.actions.wait_for_element(self.refund_r_cust_email)
        self.actions.scroll_to_the_element(self.refund_r_cust_email)
        self.actions.send_keys(self.refund_r_cust_email, create_refund_receipt_test_data[""])

    def rr_shipping_address(self, create_refund_receipt_test_data):
        self.actions.wait_for_element(self.refund_r_shipping_address)
        self.actions.scroll_to_the_element(self.refund_r_shipping_address)
        self.actions.dropdown_contains(self.refund_r_shipping_address, self.refund_r_options_shipping,
                                       create_refund_receipt_test_data[""])

    def rr_billing_address(self, create_refund_receipt_test_data):
        self.actions.wait_for_element(self.refund_r_billing_address)
        self.actions.scroll_to_the_element(self.refund_r_billing_address)
        self.actions.dropdown_contains(self.refund_r_billing_address, self.refund_r_options_billing,
                                       create_refund_receipt_test_data[""])

    def rr_location_of_sale(self, create_refund_receipt_test_data):
        self.actions.wait_for_element(self.refund_r_location_of_sale)
        self.actions.scroll_to_the_element(self.refund_r_location_of_sale)
        self.actions.dropdown_contains(self.refund_r_location_of_sale, self.refund_r_options_location_of_sale,
                                       create_refund_receipt_test_data[""])

    def rr_payment_method(self, create_refund_receipt_test_data):
        self.actions.wait_for_element(self.refund_r_payment_method)
        self.actions.scroll_to_the_element(self.refund_r_payment_method)
        self.actions.dropdown_contains(self.refund_r_payment_method, self.refund_r_options_payment_method,
                                       create_refund_receipt_test_data["rr_payment_method"])

    def rr_refund_receipt_date(self, create_refund_receipt_test_data):
        self.actions.wait_for_element(self.refund_r_refund_receipt_date)
        self.actions.scroll_to_the_element(self.refund_r_refund_receipt_date)
        self.actions.select_date(self.refund_r_refund_receipt_date, self.refund_r_current_month,
                                 self.refund_r_dt_next_btn_class, self.refund_r_dt_prev_btn_class,
                                 create_refund_receipt_test_data["refund_receipt_date"])

    def rr_refund_receipt_no(self):
        self.actions.wait_for_element(self.refund_r_refund_receipt_no)
        self.actions.scroll_to_the_element(self.refund_r_refund_receipt_no)
        self.actions.get_attribute(self.refund_r_refund_receipt_no)

    def rr_refund_from(self, create_refund_receipt_test_data):
        self.actions.wait_for_element(self.refund_r_refund_from)
        self.actions.scroll_to_the_element(self.refund_r_refund_from)
        self.actions.dropdown_contains(self.refund_r_refund_from, self.refund_r_options_refund_from,create_refund_receipt_test_data["rr_refund_from"])

    def rr_select_transactions(self, create_refund_receipt_test_data):
        self.actions.wait_for_element(self.refund_r_select_transactions)
        self.actions.scroll_to_the_element(self.refund_r_select_transactions)
        self.actions.dropdown_equals(self.refund_r_select_transactions, self.refund_r_options_transactions, create_refund_receipt_test_data["rr_select_transaction"])

    def rr_add_new_lines(self):
        self.actions.wait_for_element(self.refund_r_add_new_lines)
        self.actions.click(self.refund_r_add_new_lines)

    def rr_select_product_service(self, create_refund_receipt_test_data):
        self.actions.wait_for_element(self.refund_r_select_product_service)
        self.actions.scroll_to_the_element(self.refund_r_select_product_service)
        self.actions.dropdown_contains(self.refund_r_select_product_service, self.refund_r_options_product_service ,create_refund_receipt_test_data["rr_product_service"])

    def rr_product_qty(self, create_refund_receipt_test_data):
        self.actions.wait_for_element(self.refund_r_product_qty)
        self.actions.scroll_to_the_element(self.refund_r_product_qty)
        self.actions.clear_text(self.refund_r_product_qty)
        self.actions.send_keys(self.refund_r_product_qty, create_refund_receipt_test_data["rr_quantity"])

    def rr_product_rate(self, create_refund_receipt_test_data):
        self.actions.wait_for_element(self.refund_r_product_rate)
        self.actions.scroll_to_the_element(self.refund_r_product_rate)
        self.actions.send_keys(self.refund_r_product_rate, create_refund_receipt_test_data["rr_rate_per_unit"])

    def rr_product_amount(self):
        self.actions.wait_for_element(self.refund_r_product_amount)
        self.actions.scroll_to_the_element(self.refund_r_product_amount)
        self.actions.get_attribute(self.refund_r_product_amount)

    def rr_product_tax(self):
        self.actions.wait_for_element(self.refund_r_product_tax)
        self.actions.scroll_to_the_element(self.refund_r_product_tax)
        self.actions.get_attribute(self.refund_r_product_tax)

    def sr_product_total(self):
        self.actions.wait_for_element(self.refund_r_product_total)
        self.actions.scroll_to_the_element(self.refund_r_product_total)
        self.actions.get_attribute(self.refund_r_product_total)

    def sr_memo(self, create_refund_receipt_test_data):
        self.actions.wait_for_element(self.refund_r_memo)
        self.actions.scroll_to_the_element(self.refund_r_memo)
        self.actions.send_keys(self.refund_r_memo, create_refund_receipt_test_data["rr_memo"])

    def rr_cancel(self):
        self.actions.wait_for_element(self.refund_r_btn_cancel)
        self.actions.scroll_to_the_element(self.refund_r_btn_cancel)
        self.actions.click(self.refund_r_btn_cancel)

    def rr_clear(self):
        self.actions.wait_for_element(self.refund_r_btn_clear)
        self.actions.scroll_to_the_element(self.refund_r_btn_clear)
        self.actions.click(self.refund_r_btn_clear)

    def rr_save_and_close(self):
        self.actions.wait_for_element(self.refund_r_btn_save_close)
        self.actions.scroll_to_the_element(self.refund_r_btn_save_close)
        self.actions.click(self.refund_r_btn_save_close)

    def rr_save_and_new(self):
        self.actions.wait_for_element(self.refund_r_btn_save_new)
        self.actions.scroll_to_the_element(self.refund_r_btn_save_new)
        self.actions.click(self.refund_r_btn_save_new)

    def rr_x_button(self):
        self.actions.wait_for_element(self.refund_r_btn_x)
        self.actions.scroll_to_the_element(self.refund_r_btn_x)
        self.actions.click(self.refund_r_btn_x)
