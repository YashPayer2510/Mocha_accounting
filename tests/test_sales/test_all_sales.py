import logging
import os
import pytest
import sys
from pathlib import Path
sys.path.insert(0, r'C:\Users\Taurus13\PycharmProjects\PythonProject\tests')


from pages.all_sales_page import AllSales

logger = logging.getLogger(__name__)
@pytest.mark.needs_login
def test_all_sales_verify_transaction_type_filter(setup,all_sales_test_data):
    driver = setup
    all_sales = AllSales(driver)
    logger.info("Test Cases started")
    all_sales.all_sales_list_sales_module()
    logger.info("Clicked on Sales module")
    all_sales.all_sales_list_all_sales_submodule()
    logger.info("Clicked on Invoice sub-module")
    all_sales.all_sales_verify_transaction_type_filter(all_sales_test_data)
    logger.info("Transaction type selected and list is located according to selected transaction")

@pytest.mark.needs_login
def test_all_sales_verify_transaction_open_status_filter(setup,all_sales_test_data):
    driver = setup
    all_sales = AllSales(driver)
    logger.info("Test Cases started")
    all_sales.all_sales_list_sales_module()
    logger.info("Clicked on Sales module")
    all_sales.all_sales_list_all_sales_submodule()
    logger.info("Clicked on Invoice sub-module")
    all_sales.all_sales_verify_transaction_open_status_filter(all_sales_test_data)
    logger.info("open status selected and list is located according to selected status")

@pytest.mark.needs_login
def test_all_sales_verify_transaction_paid_status_filter(setup,all_sales_test_data):
    driver = setup
    all_sales = AllSales(driver)
    logger.info("Test Cases started")
    all_sales.all_sales_list_sales_module()
    logger.info("Clicked on Sales module")
    all_sales.all_sales_list_all_sales_submodule()
    logger.info("Clicked on Invoice sub-module")
    all_sales.all_sales_verify_transaction_paid_status_filter(all_sales_test_data)
    logger.info("paid status selected and list is located according to selected status")

@pytest.mark.needs_login
def test_all_sales_verify_transaction_deposited_status_filter(setup,all_sales_test_data):
    driver = setup
    all_sales = AllSales(driver)
    logger.info("Test Cases started")
    all_sales.all_sales_list_sales_module()
    logger.info("Clicked on Sales module")
    all_sales.all_sales_list_all_sales_submodule()
    logger.info("Clicked on Invoice sub-module")
    all_sales.all_sales_verify_transaction_deposited_status_filter(all_sales_test_data)
    logger.info("deposited status selected and list is located according to selected status")


@pytest.mark.needs_login
def test_all_sales_verify_transaction_closed_status_filter(setup,all_sales_test_data):
    driver = setup
    all_sales = AllSales(driver)
    logger.info("Test Cases started")
    all_sales.all_sales_list_sales_module()
    logger.info("Clicked on Sales module")
    all_sales.all_sales_list_all_sales_submodule()
    logger.info("Clicked on Invoice sub-module")
    all_sales.all_sales_verify_transaction_closed_status_filter(all_sales_test_data)
    logger.info("closed status selected and list is located according to selected status")


def test_all_sales_verify_transaction_applied_status_filter(setup,all_sales_test_data):
    driver = setup
    all_sales = AllSales(driver)
    logger.info("Test Cases started")
    all_sales.all_sales_list_sales_module()
    logger.info("Clicked on Sales module")
    all_sales.all_sales_list_all_sales_submodule()
    logger.info("Clicked on Invoice sub-module")
    all_sales.all_sales_verify_transaction_applied_status_filter(all_sales_test_data)
    logger.info("applied status selected and list is located according to selected status")


@pytest.mark.needs_login
def test_all_sales_verify_transaction_unapplied_status_filter(setup,all_sales_test_data):
    driver = setup
    all_sales = AllSales(driver)
    logger.info("Test Cases started")
    all_sales.all_sales_list_sales_module()
    logger.info("Clicked on Sales module")
    all_sales.all_sales_list_all_sales_submodule()
    logger.info("Clicked on Invoice sub-module")
    all_sales.all_sales_verify_transaction_unapplied_status_filter(all_sales_test_data)
    logger.info("unapplied status selected and list is located according to selected status")

@pytest.mark.needs_login
def test_all_sales_verify_transaction_partially_paid_status_filter(setup,all_sales_test_data):
    driver = setup
    all_sales = AllSales(driver)
    logger.info("Test Cases started")
    all_sales.all_sales_list_sales_module()
    logger.info("Clicked on Sales module")
    all_sales.all_sales_list_all_sales_submodule()
    logger.info("Clicked on Invoice sub-module")
    all_sales.all_sales_verify_transaction_partially_paid_status_filter(all_sales_test_data)
    logger.info("partially paid status selected and list is located according to selected status")

@pytest.mark.needs_login
def test_all_sales_verify_transaction_overdue_status_filter(setup,all_sales_test_data):
    driver = setup
    all_sales = AllSales(driver)
    logger.info("Test Cases started")
    all_sales.all_sales_list_sales_module()
    logger.info("Clicked on Sales module")
    all_sales.all_sales_list_all_sales_submodule()
    logger.info("Clicked on Invoice sub-module")
    all_sales.all_sales_verify_transaction_overdue_status_filter(all_sales_test_data)
    logger.info("overdue status selected and list is located according to selected status")

def test_all_sales_verify_transaction_void_status_filter(setup,all_sales_test_data):
    driver = setup
    all_sales = AllSales(driver)
    logger.info("Test Cases started")
    all_sales.all_sales_list_sales_module()
    logger.info("Clicked on Sales module")
    all_sales.all_sales_list_all_sales_submodule()
    logger.info("Clicked on Invoice sub-module")
    all_sales.all_sales_verify_transaction_void_status_filter(all_sales_test_data)
    logger.info("void status selected and list is located according to selected status")


@pytest.mark.needs_login
def test_all_sales_verify_transaction_type_status_filter(setup,all_sales_test_data):
    driver = setup
    all_sales = AllSales(driver)
    logger.info("Test Cases started")
    all_sales.all_sales_list_sales_module()
    logger.info("Clicked on Sales module")
    all_sales.all_sales_list_all_sales_submodule()
    logger.info("Clicked on Invoice sub-module")
    all_sales.all_sales_verify_transaction_type_status_filter(all_sales_test_data)
    logger.info("selected type, status and list is located according to selected status")

@pytest.mark.needs_login
def test_all_sales_verify_transaction_type_status_customer_filter(setup, all_sales_test_data):
    driver= setup
    all_sales = AllSales(driver)
    logger.info("Test Cases started")
    all_sales.all_sales_list_sales_module()
    logger.info("Clicked on Sales module")
    all_sales.all_sales_list_all_sales_submodule()
    logger.info("Clicked on Invoice sub-module")
    all_sales.all_sales_verify_transaction_type_status_customer_filter(all_sales_test_data)
    logger.info("selected type, status, customer and list is located according to selected status")
