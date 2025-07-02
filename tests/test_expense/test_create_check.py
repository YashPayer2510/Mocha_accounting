import logging
import os
import time
from pages.expenses.create_check import Create_Check
from tests.conftest import setup, log_file
import allure
from tests.conftest import setup, create_check_test_data, create_invoice_test_data

logger = logging.getLogger(__name__)

def test_ete_create_check(setup, create_check_test_data, create_invoice_test_data):
    driver = setup
    create_check = Create_Check(driver)
    create_check.inv_submod_Sales()
    create_check.inv_submod_invoice()
    create_check.inv_create_invoice()
    create_check.inv_select_customer(create_invoice_test_data)
    create_check.inv_add_items_btn()
    create_check.inv_click_product_service()
    create_check.inv_click_product_x_button()
    create_check.create_c_new()
    logger.info("Clicked on +New")
    create_check.create_c_check()
    logger.info("Clicked on Check")
    create_check.create_c_select_payee(create_check_test_data)
    logger.info("Payee selected")
    create_check.create_c_select_payment_account(create_check_test_data)
    logger.info("Payment account selected")
    create_check.create_c_check_date(create_check_test_data)
    logger.info("Check date selected")
    create_check.create_c_category_add_new_line_btn()
    logger.info("Clicked on Add new line for category details")
    create_check.create_c_add_multiple_category_cao_with_changexpath(create_check_test_data)
    logger.info("Selected the CAO and added amount")
    time.sleep(2)
    create_check.create_c_item_details_add_new_line_btn()
    logger.info("Clicked on Add new line for item details")
    time.sleep(2)
    logger.info("Selected the product")
    create_check.create_c_add_multiple_product_cao_with_changexpath(create_check_test_data)
    logger.info("Category selected and added amount")
    create_check.create_c_memo(create_check_test_data)
    logger.info("Entered memo")
    create_check.create_c_save_and_close()
    logger.info("Clicked Save and Close")
    create_check.create_c_x_button()
    logger.info("Clicked X button on expense list")