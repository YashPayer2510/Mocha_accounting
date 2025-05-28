import logging
import os
import time

from pages.create_sales_receipt import SalesReceipt
#from dotenv import load_dotenv
from tests.conftest import setup, create_sales_receipt_test_data
import allure
logger = logging.getLogger(__name__)

#verify the ete flow of the refund receipt transaction
def test_ete_create_sales_receipt(setup, create_sales_receipt_test_data):
    driver = setup
    sales_receipt = SalesReceipt(driver)
    logger.info("Test Case Started for create sales receipt")
    sales_receipt.sr_plus_new()
    logger.info("clicked on + New button")
    sales_receipt.sr_sales_receipt()
    logger.info("clicked on Sales Receipt")
    sales_receipt.sr_select_customer(create_sales_receipt_test_data)
    logger.info("customer selected")
    sales_receipt.sr_sales_receipt_date(create_sales_receipt_test_data)
    logger.info("sales receipt date selected")
    sales_receipt.sr_sales_receipt_no()
    logger.info("get the sale receipt no")
    sales_receipt.sr_payment_method(create_sales_receipt_test_data)
    logger.info("selected the payment method")
    sales_receipt.sr_deposit_to(create_sales_receipt_test_data)
    logger.info("selected the deposit to account")
    sales_receipt.cm_add_new_lines()
    logger.info("Clicked on add new line button.")
    time.sleep(3)
    sales_receipt.sr_select_product_service(create_sales_receipt_test_data)
    logger.info("product/service selected")
    time.sleep(3)
    sales_receipt.sr_product_qty(create_sales_receipt_test_data)
    logger.info("qty added")
    time.sleep(3)
    sales_receipt.sr_save_and_close()
    logger.info("save and close click")
    sales_receipt.sr_x_button()
    logger.info("x button click")
    logger.info("Test cases ended")