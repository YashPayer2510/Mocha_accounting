import logging
import time

import pytest

from pages.expenses.expense_list import  ExpenseList


logger = logging.getLogger(__name__)
@pytest.mark.needs_login
def test_expense_list_verify_transaction_type_filter(expense_setup, expense_list_test_data):
    driver = expense_setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expenses sub-module")
    time.sleep(5)
    expense_list.expense_verify_transaction_type_filter(expense_list_test_data)
    logger.info("Transaction type selected and list is located according to selected transaction")

@pytest.mark.needs_login
def test_expense_select_date_range(setup, expense_list_test_data):
    driver = setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expense sub-module")
    time.sleep(5)
    expense_list.expense_list_filter_btn_submodule()
    logger.info("Clicked on filter button ")
    expense_list.select_date_range(expense_list_test_data)
    logger.info("Date range selected")
    time.sleep(5)
    expense_list.verify_expense_dates_within_range(expense_list_test_data)
    logger.info("verify weather the transactions displayed is according to given dat range")

@pytest.mark.needs_login
def test_expense_list_verify_transaction_unpaid_status_filter(setup, expense_list_test_data):
    driver = setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expense sub-module")
    time.sleep(5)
    expense_list.expense_list_filter_btn_submodule()
    logger.info("Clicked on filter button ")
    expense_list.expense_list_verify_transaction_unpaid_status_filter(expense_list_test_data)
    logger.info("verify weather the transactions displayed is according to selected type")

@pytest.mark.needs_login
def test_expense_list_verify_transaction_paid_status_filter(setup, expense_list_test_data):
    driver = setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expense sub-module")
    time.sleep(5)
    expense_list.expense_list_filter_btn_submodule()
    logger.info("Clicked on filter button ")
    expense_list.expense_list_verify_transaction_paid_status_filter(expense_list_test_data)
    logger.info("verify weather the transactions displayed is according to selected type")


@pytest.mark.needs_login
def test_expense_list_verify_transaction_partially_paid_status_filter(setup, expense_list_test_data):
    driver = setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expense sub-module")
    time.sleep(5)
    expense_list.expense_list_filter_btn_submodule()
    logger.info("Clicked on filter button ")
    expense_list.expense_list_verify_transaction_partially_paid_status_filter(expense_list_test_data)
    logger.info("verify weather the transactions displayed is according to selected type")


@pytest.mark.needs_login
def test_expense_list_verify_transaction_deposited_status_filter(setup, expense_list_test_data):
    driver = setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expense sub-module")
    time.sleep(5)
    expense_list.expense_list_filter_btn_submodule()
    logger.info("Clicked on filter button ")
    expense_list.expense_list_verify_transaction_deposited_status_filter(expense_list_test_data)
    logger.info("verify weather the transactions displayed is according to selected type")


@pytest.mark.needs_login
def test_expense_list_verify_transaction_applied_status_filter(setup, expense_list_test_data):
    driver = setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expense sub-module")
    time.sleep(5)
    expense_list.expense_list_filter_btn_submodule()
    logger.info("Clicked on filter button ")
    expense_list.expense_list_verify_transaction_applied_status_filter(expense_list_test_data)
    logger.info("verify weather the transactions displayed is according to selected type")

@pytest.mark.needs_login
def test_expense_list_verify_transaction_unapplied_status_filter(setup, expense_list_test_data):
    driver = setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expense sub-module")
    time.sleep(5)
    expense_list.expense_list_filter_btn_submodule()
    logger.info("Clicked on filter button ")
    expense_list.expense_list_verify_transaction_unapplied_status_filter(expense_list_test_data)
    logger.info("verify weather the transactions displayed is according to selected type")


@pytest.mark.needs_login
def test_expense_list_verify_transaction_overdue_status_filter(setup, expense_list_test_data):
    driver = setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expense sub-module")
    time.sleep(5)
    expense_list.expense_list_filter_btn_submodule()
    logger.info("Clicked on filter button ")
    expense_list.expense_list_verify_transaction_overdue_status_filter(expense_list_test_data)
    logger.info("verify weather the transactions displayed is according to selected type")

@pytest.mark.needs_login
def test_expense_list_verify_transaction_void_status_filter(setup, expense_list_test_data):
    driver = setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expense sub-module")
    time.sleep(5)
    expense_list.expense_list_filter_btn_submodule()
    logger.info("Clicked on filter button ")
    expense_list.expense_list_verify_transaction_void_status_filter(expense_list_test_data)
    logger.info("verify weather the transactions displayed is according to selected type")


@pytest.mark.needs_login
def test_all_sales_verify_transaction_type_status_filter(setup, expense_list_test_data):
    driver = setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expense sub-module")
    time.sleep(5)
    expense_list.expense_list_verify_transaction_type_status_filter(expense_list_test_data)
    logger.info("The transaction list loaded according to selected type and status filter")

@pytest.mark.needs_login
def test_all_sales_verify_transaction_type_status_customer_filter(setup, expense_list_test_data):
    driver = setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expense sub-module")
    time.sleep(5)
    expense_list.expense_list_verify_transaction_type_status_customer_filter(expense_list_test_data)
    logger.info("The transaction list loaded according to selected type,status and customer filter")


@pytest.mark.needs_login
def test_verify_date_range_dropdown_filter(setup, expense_list_test_data):
    driver = setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expense sub-module")
    time.sleep(5)
    expense_list.verify_date_range_dropdown_filter(expense_list_test_data)
    logger.info("The transaction list loaded according to selected period filter")

@pytest.mark.needs_login
def test_verify_category_dropdown_filter(setup, expense_list_test_data):
    driver = setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expense sub-module")
    time.sleep(5)
    expense_list.verify_category_dropdown_filter(expense_list_test_data)
    logger.info("The transaction list loaded according to selected category filter")


@pytest.mark.needs_login
def test_expense_list_verify_transaction_category_type_status_customer_date_range_filter(setup, expense_list_test_data):
    driver = setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expense sub-module")
    time.sleep(5)
    expense_list.expense_list_verify_transaction_category_type_status_customer_date_range_filter(expense_list_test_data)
    logger.info("The transaction list loaded according to selected category, date range, type,status and customer filters")


@pytest.mark.needs_login
def test_expense_list_verify_transaction_category_type_status_customer_selecte_date_range_filter(setup, expense_list_test_data):
    driver = setup
    expense_list = ExpenseList(driver)
    logger.info("Test Cases started")
    expense_list.expense_list_expense_module()
    logger.info("Clicked on Expense module")
    expense_list.expense_list_expense_list_submodule()
    logger.info("Clicked on Expense sub-module")
    time.sleep(5)
    expense_list.expense_list_verify_transaction_category_type_status_customer_selecte_date_range_filter( expense_list_test_data)
    logger.info("The transaction list loaded according to selected category, date range, type,status and customer filters")


