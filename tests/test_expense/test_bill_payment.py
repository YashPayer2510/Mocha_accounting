import logging
import os
import time

import pytest

from pages.expenses.bill_payment import BillPayment
from pages.expenses.create_check import Create_Check
import allure


logger = logging.getLogger(__name__)
@pytest.mark.needs_login
def test_ete_bill_payment(expense_setup, bill_payment_test_data):
    driver = expense_setup
    bill_payment = BillPayment(driver)
    bill_payment.bill_b_exp_mod()
    logger.info("Clicked on Expense module")
    bill_payment.bill_b_exp_list_submod()
    logger.info("Clicked on Expense list submodule")
    bill_payment.bill_p_mark_as_paid_click(bill_payment_test_data)
    logger.info("clicked on mark as paid")
    bill_payment.bill_p_dd_payment_account(bill_payment_test_data)
    logger.info("Payment account selected")
    bill_payment.bill_p_payment_date(bill_payment_test_data)
    logger.info("Payment date selected")
    bill_payment.bill_p_outstanding_transactions_check_and_enter_amount(bill_payment_test_data)
    logger.info("Bill checked and amount added")
    bill_payment.bill_p_credits_check_and_enter_amount(bill_payment_test_data)
    logger.info("Credits checked and amount added")
    bill_payment.bill_p_click_x_button()
    logger.info("Clicked X button on expense list")