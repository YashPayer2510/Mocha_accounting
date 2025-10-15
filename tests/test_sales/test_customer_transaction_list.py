import logging
import os
import time

import pytest

from pages.customer_list import CustomerList
from pages.customer_transaction_list import CustomerTransactionList


logger = logging.getLogger(__name__)

@pytest.mark.needs_login
def test_customer_transaction_list_verify_customer_clickable_navigation(setup, customer_transaction_list_test_data  ):
    driver = setup
    customer_transaction_list = CustomerTransactionList(driver)
    logger.info("Test Cases started")
    customer_transaction_list.customer_transaction_list_verify_customer_clickable_navigation(customer_transaction_list_test_data)

@pytest.mark.needs_login
def test_customer_transaction_verify_open_balance_with_transaction_list(setup, customer_transaction_list_test_data  ):
    driver = setup
    customer_transaction_list = CustomerTransactionList(driver)
    logger.info("Test Cases started")
    customer_transaction_list.customer_transaction_verify_open_balance_with_transaction_list(customer_transaction_list_test_data)

@pytest.mark.needs_login
def test_customer_transaction_list_verify_open_balance_with_sum_transactions(setup, customer_transaction_list_test_data  ):
    driver = setup
    customer_transaction_list = CustomerTransactionList(driver)
    logger.info("Test Cases started")
    customer_transaction_list.customer_transaction_list_sales_module()
    logger.info("Clicked on Sales module")
    customer_transaction_list.customer_transaction_list_all_sales_submodule()
    logger.info("Clicked on All Sales sub-module")
    customer_transaction_list.customer_transaction_list_verify_open_balance_with_sum_transactions(customer_transaction_list_test_data)

@pytest.mark.needs_login
def test_customer_transaction_list_verify_overdue_amount_with_overdue_transactions_sum(setup, customer_list_test_data, customer_transaction_list_test_data  ):
    driver = setup
    customer_transaction_list = CustomerTransactionList(driver)
    logger.info("Test Cases started")
    customer_transaction_list.customer_transaction_list_sales_module()
    logger.info("Clicked on Sales module")
    customer_transaction_list.customer_transaction_list_all_sales_submodule()
    logger.info("Clicked on All Sales sub-module")
    customer_transaction_list.customer_transaction_list_verify_overdue_amount_with_overdue_transactions_sum(customer_transaction_list_test_data)