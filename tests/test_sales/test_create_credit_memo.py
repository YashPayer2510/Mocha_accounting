import logging
import os
import time

import pytest

from pages.create_credit_memo import CreditMemo
#from dotenv import load_dotenv
import allure
logger = logging.getLogger(__name__)

#verify the ete flow of the credit memo transaction
@pytest.mark.needs_login
def test_ete_create_credit_memo(setup, create_credit_memo_test_data):
    driver = setup
    credit_memo = CreditMemo(driver)
    logger.info("Test Case Started for create credit memo")
    credit_memo.cm_plus_new()
    logger.info("clicked on + New button")
    credit_memo.cm_credit_memo()
    logger.info("clicked on credit memo")
    credit_memo.cm_select_customer(create_credit_memo_test_data)
    logger.info("customer selected")
    credit_memo.cm_credit_memo_date(create_credit_memo_test_data)
    logger.info("credit memo date selected")
    credit_memo.cm_select_transactions(create_credit_memo_test_data)
    logger.info("transaction selected")
    time.sleep(3)
    #credit_memo.cm_add_new_lines()
    #logger.info("clicked on add new line button")
    #credit_memo.cm_select_product_service(create_credit_memo_test_data)
    #logger.info("product/service selected")
    #credit_memo.cm_product_qty(create_credit_memo_test_data)
    #logger.info("qty added")
    credit_memo.cm_save_and_close()
    logger.info("save and close clicked")
    credit_memo.cm_x_button()
    logger.info("x button clicked")
    logger.info("Test case ended")

def test_ete_create_credit_memo_sales_flow(setup, create_credit_memo_test_data,customer_name):
    driver = setup
    credit_memo = CreditMemo(driver)
    logger.info("Test Case Started for create credit memo")
    credit_memo.cm_plus_new()
    logger.info("clicked on + New button")
    credit_memo.cm_credit_memo()
    logger.info("clicked on credit memo")
    credit_memo.cm_select_customer_for_sale_flow(customer_name)
    logger.info("customer selected")
    credit_memo.cm_credit_memo_date(create_credit_memo_test_data)
    logger.info("credit memo date selected")
    credit_memo.cm_select_transactions(create_credit_memo_test_data)
    logger.info("transaction selected")
    time.sleep(3)
    #credit_memo.cm_add_new_lines()
    #logger.info("clicked on add new line button")
    #credit_memo.cm_select_product_service(create_credit_memo_test_data)
    #logger.info("product/service selected")
    #credit_memo.cm_product_qty(create_credit_memo_test_data)
    #logger.info("qty added")
    credit_memo.cm_save_and_close()
    logger.info("save and close clicked")
    credit_memo.cm_x_button()
    logger.info("x button clicked")
    logger.info("Test case ended")
