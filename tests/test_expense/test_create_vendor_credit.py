import logging
import os
import time
import allure
from pages.expenses.create_vendor_credit import Create_Vendor_Credit
from tests.conftest import setup, log_file, create_vendor_credit_test_data, create_invoice_test_data

logger = logging.getLogger(__name__)


def test_ete_create_vendor_credit(setup, create_vendor_credit_test_data, create_invoice_test_data):
    driver = setup
    create_vc = Create_Vendor_Credit(driver)

    # Setup steps
    create_vc.inv_submod_Sales()
    create_vc.inv_submod_invoice()
    create_vc.inv_create_invoice()
    create_vc.inv_select_customer(create_invoice_test_data)
    create_vc.inv_add_items_btn()
    create_vc.inv_click_product_service()
    create_vc.inv_click_product_x_button()

    # Vendor Credit creation steps
    create_vc.create_vc_new()
    logger.info("Clicked on +New")

    create_vc.create_vc_vendor_credit()
    logger.info("Clicked on Vendor Credit")

    create_vc.create_vc_select_payee(create_vendor_credit_test_data)
    logger.info("Payee selected")

    create_vc.create_vc_vendor_credit_date(create_vendor_credit_test_data)
    logger.info("Vendor Credit date selected")

    create_vc.create_vc_category_add_new_line_btn()
    logger.info("Clicked on Add new line for category details")

    create_vc.create_vc_add_multiple_category_cao_with_changexpath(create_vendor_credit_test_data)
    logger.info("Selected the CAO and added amount")
    time.sleep(2)

    create_vc.create_vc_item_details_add_new_line_btn()
    time.sleep(2)
    logger.info("Selected the product")

    create_vc.create_vc_add_multiple_product_cao_with_changexpath(create_vendor_credit_test_data)
    logger.info("Category selected and added amount")

    create_vc.create_vc_memo(create_vendor_credit_test_data)
    logger.info("Entered memo")

    create_vc.create_vc_save_and_close()
    logger.info("Clicked Save and Close")

    create_vc.create_vc_click_x_button()
    logger.info("Clicked X button on expense list")