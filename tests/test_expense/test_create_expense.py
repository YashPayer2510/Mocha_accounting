import logging
import time

import pytest

from pages.expenses.create_expense import Create_Expense


logger = logging.getLogger(__name__)

@pytest.mark.needs_login
def test_ete_create_expense(expense_setup, create_expense_test_data, create_invoice_test_data):
    driver = expense_setup
    create_expense = Create_Expense(driver)
    create_expense.inv_submod_Sales()
    create_expense.inv_submod_invoice()
    create_expense.inv_create_invoice()
    create_expense.inv_select_customer(create_invoice_test_data)
    create_expense.inv_add_items_btn()
    create_expense.inv_click_product_service()
    create_expense.inv_click_product_x_button()
    create_expense.create_e_new()
    logger.info("Clicked on +New")
    create_expense.create_e_expense()
    logger.info("Clicked on Expense")
    create_expense.create_e_select_payee(create_expense_test_data)
    logger.info("Payee selected")
    create_expense.create_e_select_payment_account(create_expense_test_data)
    logger.info("Payment account selected")
    create_expense.create_e_expense_date(create_expense_test_data)
    logger.info("Expense date selected")
    create_expense.create_e_select_payment_2(create_expense_test_data)
    logger.info("Payment method selected")
    create_expense.create_e_category_add_new_line_btn()
    logger.info("Clicked on Add new line for category details")
    create_expense.create_e_add_multiple_category_cao_with_changexpath(create_expense_test_data)
    logger.info("Selected the CAO and added amount")
    time.sleep(2)
    create_expense.create_e_item_details_add_new_line_btn()
    time.sleep(2)
    logger.info("Selected the product")
    create_expense.create_e_add_multiple_product_cao_with_changexpath(create_expense_test_data)
    logger.info("Category selected and added amount")
    create_expense.create_e_memo(create_expense_test_data)
    logger.info("Entered memo")
    create_expense.create_e_save_and_close()
    logger.info("Clicked Save and Close")
    create_expense.create_e_click_x_button()
    logger.info("Clicked X button on expense list")