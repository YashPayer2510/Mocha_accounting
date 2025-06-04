import logging
import os
import time



from pages.customer_list import CustomerList
from tests.conftest import setup
import allure
from tests.conftest import setup, all_sales_test_data
logger = logging.getLogger(__name__)

def test_assert_invoice_total_count_in_all_sales_with_total_invoice_displayed(setup,all_sales_test_data):
    driver = setup
    customer_list = CustomerList(driver)
    logger.info("Test Cases started")
    customer_list.assert_invoice_total_count_in_all_sales_with_total_invoice_displayed(all_sales_test_data)
    logger.info("Test Cases ended")

def test_assert_over_total_count_in_all_sales_with_total_overdue_displayed(setup,all_sales_test_data):
    driver = setup
    customer_list = CustomerList(driver)
    logger.info("Test Cases started")
    customer_list.assert_overdue_total_count_in_all_sales_with_total_overdue_displayed(all_sales_test_data)
    logger.info("Test Cases ended")

def test_assert_open_total_count_in_all_sales_with_total_open_displayed(setup,all_sales_test_data):
    driver = setup
    customer_list = CustomerList(driver)
    logger.info("Test Cases started")
    customer_list.assert_open_total_count_in_all_sales_with_total_open_displayed(all_sales_test_data)
    logger.info("Test Cases ended")

def test_assert_paid_total_count_in_all_sales_with_total_paid_displayed(setup,all_sales_test_data):
    driver = setup
    customer_list = CustomerList(driver)
    logger.info("Test Cases started")
    customer_list.assert_paid_total_count_in_all_sales_with_total_paid_displayed(all_sales_test_data)
    logger.info("Test Cases ended")

def test_verify_customer_search_bar(setup, customer_list_test_data):
    driver = setup
    customer_list = CustomerList(driver)
    logger.info("Test Cases started")
    customer_list.customer_list_sales_module()
    logger.info("Clicked on Sales module")
    customer_list.customer_list_customer_submodule()
    logger.info("Clicked on customer sub-module")
    customer_list.verify_customer_search_bar(customer_list_test_data)

