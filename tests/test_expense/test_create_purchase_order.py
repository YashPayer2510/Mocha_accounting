import logging
import time

import pytest

from pages.expenses.create_purchase_order import Create_Purchase_Order
from tests.test_expense.conftest import expense_setup

logger = logging.getLogger(__name__)

@pytest.mark.needs_login
def test_ete_create_purchase_order(expense_setup, create_purchase_order_test_data, create_invoice_test_data):
    driver = expense_setup
    create_po = Create_Purchase_Order(driver)

    # Setup steps
    create_po.inv_submod_Sales()
    create_po.inv_submod_invoice()
    create_po.inv_create_invoice()
    create_po.inv_select_customer(create_invoice_test_data)
    create_po.inv_add_items_btn()
    create_po.inv_click_product_service()
    create_po.inv_click_product_x_button()

    # Purchase Order creation steps
    create_po.create_po_new()
    logger.info("Clicked on +New")

    create_po.create_po_purchase_order()
    logger.info("Clicked on Purchase Order")

    create_po.create_po_select_payee(create_purchase_order_test_data)
    logger.info("Payee selected")

    create_po.create_po_purchase_order_date(create_purchase_order_test_data)
    logger.info("Purchase Order date selected")

    create_po.create_po_category_add_new_line_btn()
    logger.info("Clicked on Add new line for category details")

    create_po.create_po_add_multiple_category_cao_with_changexpath(create_purchase_order_test_data)
    logger.info("Selected the CAO and added amount")
    time.sleep(2)

    create_po.create_po_item_details_add_new_line_btn()
    time.sleep(2)
    logger.info("Selected the product")

    create_po.create_po_add_multiple_product_cao_with_changexpath(create_purchase_order_test_data)
    logger.info("Category selected and added amount")

    create_po.create_po_memo(create_purchase_order_test_data)
    logger.info("Entered memo")

    create_po.create_po_save_and_close()
    logger.info("Clicked Save and Close")

    create_po.create_po_click_x_button()
    logger.info("Clicked X button on expense list")

