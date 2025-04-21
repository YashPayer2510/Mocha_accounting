import logging
import time

from pages.create_invoice import Create_Invoice

from tests.conftest import setup, create_invoice_test_data

logger = logging.getLogger(__name__)

def test_create_invoice(setup, create_invoice_test_data):
    driver = setup
    create_invoice = Create_Invoice(driver)


    logger.info("Test case started for create invoice")
    create_invoice.inv_submod_Sales()
    logger.info("Navigated to Sale module")
    create_invoice.inv_submod_invoice()
    logger.info("Navigated to Invoice submodule")
    create_invoice.inv_create_invoice()
    logger.info("clicked on create invoice button")
    time.sleep(3)
    create_invoice.inv_select_customer(create_invoice_test_data)
    logger.info("customer selected")
    time.sleep(2)
    #create_invoice.inv_select_credit_terms(create_invoice_test_data)
    logger.info("credit terms selected")
    #create_invoice.inv_location_of_sale(create_invoice_test_data)
    logger.info("location of sale selected")
    #create_invoice.inv_dd_billing(create_invoice_test_data)
    logger.info("billing address selected")
    #create_invoice.inv_shippingvia(create_invoice_test_data)
    logger.info("shippingvia address selected")
    #create_invoice.inv_shipping_to(create_invoice_test_data)
    logger.info("shippingto address selected")
    create_invoice.inv_invoice_date(create_invoice_test_data)
    logger.info("invoice date selected")
    create_invoice.inv_shipping_date(create_invoice_test_data)
    logger.info("shipping date selected")
    create_invoice.inv_due_date(create_invoice_test_data)
    logger.info("due date selected")
    create_invoice.inv_click_additems()
    logger.info("add items button clicked")
    create_invoice.inv_select_productservice(create_invoice_test_data)
    logger.info("product or service selected")
    create_invoice.inv_inp_quanitiy(create_invoice_test_data)
    logger.info("product or service quantity added")
    create_invoice.inv_inp_rate_per_unit(create_invoice_test_data)
    logger.info("product or service rate added")
    #create_invoice.inv_btn_prod_cancel()
    #logger.info("cancel button click")
    create_invoice.inv_btn_prod_save()
    logger.info("save button click")
    create_invoice.inv_inp_message_on_invoice()
    logger.info("message given for invoice")
    create_invoice.inv_txt_sub_total()
    logger.info("get subtotal")
    create_invoice.inv_txt_tax()
    logger.info("get tax")
    create_invoice.inv_txt_amount_received()
    logger.info("get amount received")
    create_invoice.inv_txt_balance()
    logger.info("get balance")
    create_invoice.inv_btn_save_close()
    logger.info("clicked on Save and Close button")
    logger.info("TC ended")

    time.sleep(5)


