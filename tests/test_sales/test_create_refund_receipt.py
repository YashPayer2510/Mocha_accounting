import logging
import os
import time

import pytest

from pages.create_refund_receipt import RefundReceipt
#from dotenv import load_dotenv
import allure
logger = logging.getLogger(__name__)

#verify the ete flow of the credit memo transaction
@pytest.mark.needs_login
def test_ete_refund_receipt_memo(setup, create_refund_receipt_test_data):
    driver = setup
    refund_receipt = RefundReceipt(driver)
    logger.info("Test Case Started for create credit memo")
    refund_receipt.rr_plus_new()
    logger.info("clicked on + New button")
    refund_receipt.rr_refund_receipt()
    logger.info("clicked on credit memo")
    refund_receipt.rr_select_customer(create_refund_receipt_test_data)
    logger.info("customer selected")
    refund_receipt.rr_payment_method(create_refund_receipt_test_data)
    logger.info("payment method selected")
    refund_receipt.rr_refund_receipt_date(create_refund_receipt_test_data)
    logger.info("refund receipt date selected")
    refund_receipt.rr_refund_from(create_refund_receipt_test_data)
    logger.info("refund from selected")
    refund_receipt.rr_select_transactions(create_refund_receipt_test_data)
    logger.info("transaction selected")
    time.sleep(3)
    #refund_receipt.rr_add_new_lines()
    #logger.info("clicked on add new line button")
    #refund_receipt.rr_select_product_service(create_refund_receipt_test_data)
    #logger.info("product/service selected")
    #refund_receipt.rr_product_qty(create_refund_receipt_test_data)
    #logger.info("qty added")
    refund_receipt.rr_save_and_close()
    logger.info("save and closed clicked")
    refund_receipt.rr_x_button()
    logger.info("x button clicked")
    logger.info("Test case ended")



