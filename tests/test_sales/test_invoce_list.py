import logging
import os
import time

import pytest

from pages.invoices_list import InvoicesList

import allure
logger = logging.getLogger(__name__)

@pytest.mark.needs_login
def test_inv_list_verify_overdue_amount(setup):
    driver=setup
    invoice_list= InvoicesList(driver)
    logger.info("Test Cases started")
    invoice_list.inv_list_sales_module()
    logger.info("Clicked on Sales module")
    invoice_list.inv_list_invoice_submodule()
    logger.info("Clicked on Invoice sub-module")
    invoice_list.inv_list_verify_overdue_amount()

@pytest.mark.needs_login
def test_inv_list_verify_not_due_yet_amount(setup):
    driver=setup
    invoice_list= InvoicesList(driver)
    logger.info("Test Cases started")
    invoice_list.inv_list_sales_module()
    logger.info("Clicked on Sales module")
    invoice_list.inv_list_invoice_submodule()
    logger.info("Clicked on Invoice sub-module")
    invoice_list.inv_list_verify_not_due_yet_amount()

@pytest.mark.needs_login
def test_inv_list_verify_not_deposited_amount(setup):
    driver = setup
    invoice_list = InvoicesList(driver)
    logger.info("Test Cases started")
    invoice_list.inv_list_sales_module()
    logger.info("Clicked on Sales module")
    invoice_list.inv_list_invoice_submodule()
    logger.info("Clicked on Invoice sub-module")
    invoice_list.inv_list_verify_not_deposited_amount()

@pytest.mark.needs_login
def test_inv_list_verify_deposited_amount(setup):
    driver = setup
    invoice_list = InvoicesList(driver)
    logger.info("Test Cases started")
    invoice_list.inv_list_sales_module()
    logger.info("Clicked on Sales module")
    invoice_list.inv_list_invoice_submodule()
    logger.info("Clicked on Invoice sub-module")
    invoice_list.inv_list_verify_deposited2_amount()

@pytest.mark.needs_login
def test_inv_list_verify_overdue_dd_filter(setup):
    driver = setup
    invoice_list = InvoicesList(driver)
    logger.info("Test Cases started")
    invoice_list.inv_list_sales_module()
    logger.info("Clicked on Sales module")
    invoice_list.inv_list_invoice_submodule()
    logger.info("Clicked on Invoice sub-module")
    invoice_list.inv_list_verify_overdue_filter()

@pytest.mark.needs_login
def test_inv_list_verify_not_due_yet_dd_filter(setup):
    driver = setup
    invoice_list = InvoicesList(driver)
    logger.info("Test Cases started")
    invoice_list.inv_list_sales_module()
    logger.info("Clicked on Sales module")
    invoice_list.inv_list_invoice_submodule()
    logger.info("Clicked on Invoice sub-module")
    invoice_list.inv_list_verify_not_due_yet_filter()

@pytest.mark.needs_login
def test_inv_list_verify_not_deposit_dd_filter(setup):
    driver = setup
    invoice_list = InvoicesList(driver)
    logger.info("Test Cases started")
    invoice_list.inv_list_sales_module()
    logger.info("Clicked on Sales module")
    invoice_list.inv_list_invoice_submodule()
    logger.info("Clicked on Invoice sub-module")
    invoice_list.inv_list_verify_not_deposited_filter()

@pytest.mark.needs_login
def test_inv_list_verify_deposited_dd_filter(setup):
    driver = setup
    invoice_list = InvoicesList(driver)
    logger.info("Test Cases started")
    invoice_list.inv_list_sales_module()
    logger.info("Clicked on Sales module")
    invoice_list.inv_list_invoice_submodule()
    logger.info("Clicked on Invoice sub-module")
    invoice_list.inv_list_verify_deposited_filter()
