import logging
import os
import time



from pages.expenses.create_bill import Create_Bill
from tests.conftest import setup, log_file
import allure
from tests.conftest import setup, create_bill_test_data,create_invoice_test_data
logger = logging.getLogger(__name__)

def test_ete_create_bill(setup, create_bill_test_data, create_invoice_test_data):
    driver = setup
    create_bill = Create_Bill(driver)
    create_bill.inv_submod_Sales()
    create_bill.inv_submod_invoice()
    create_bill.inv_create_invoice()
    create_bill.inv_select_customer(create_invoice_test_data)
    create_bill.inv_add_items_btn()
    create_bill.inv_click_product_service()
    create_bill.inv_click_product_x_button()
    create_bill.create_b_new()
    logger.info("Clicked on +New")
    create_bill.create_b_bill()
    logger.info("Clicked on Bill")
    create_bill.create_b_select_payee(create_bill_test_data)
    logger.info("Payee selected")
    create_bill.create_b_bill_date(create_bill_test_data)
    logger.info("Bill date selected")
    create_bill.create_b_category_add_new_line_btn()
    logger.info("Clicked on Add new line for category details")
    create_bill.create_b_add_multiple_category_cao_with_changexpath(create_bill_test_data)
    logger.info("Selected the CAO and added amount")
    time.sleep(2)
    create_bill.create_b_item_details_add_new_line_btn()
    time.sleep(2)
    logger.info("Selected the product")
    create_bill.create_b_add_multiple_product_cao_with_changexpath(create_bill_test_data)
    logger.info("category selected and added amount")
    create_bill.create_b_memo(create_bill_test_data)
    logger.info("Entered memo")
    create_bill.create_b_save_and_close()
    logger.info("Clicked Save and Close")
    create_bill.create_b_click_x_button()
    logger.info("Clicked X button on expense list")

