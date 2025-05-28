import logging
import os
import time

from pages.receive_payment import ReceivePayment
#from dotenv import load_dotenv
from tests.conftest import setup, createcustomer_test_data
import allure
logger = logging.getLogger(__name__)

#verify the ete flow of the receive payment transaction
def test_ete_receive_payment(setup, receive_payment_test_data):
    driver = setup
    receive_payment = ReceivePayment(driver)

    logger.info("Test case started for create invoice")
    receive_payment.recpay_mod_sales()
    #receive_payment.rp_submod_invoice()
    receive_payment.rp_submod_recpay()
    receive_payment.rp_dd_select_customer(receive_payment_test_data)
    receive_payment.rp_payment_date(receive_payment_test_data)
    receive_payment.rp_reference_no()
    receive_payment.rp_dd_payment_method(receive_payment_test_data)
    receive_payment.rp_dd_deposit_to(receive_payment_test_data)
    time.sleep(3)
    receive_payment.rp_outstanding_transactions_check_and_enter_amount(receive_payment_test_data)
    receive_payment.rp_credits_check_and_enter_amount(receive_payment_test_data)
    receive_payment.rp_total_outstanding_transactions()
    receive_payment.rp_total_credits_transactions()
    receive_payment.rp_amount_received()
    receive_payment.rp_memo(receive_payment_test_data)
    receive_payment.rp_save_and_close()

#Verify that total amount received amount should be total of outstanding amount - total credits
def test_validate_total_amount_received_balance(setup, receive_payment_test_data):
    driver = setup
    receive_payment = ReceivePayment(driver)

    logger.info("Test case started for create invoice")
    receive_payment.recpay_mod_sales()
    #receive_payment.rp_submod_invoice()
    receive_payment.rp_submod_recpay()
    receive_payment.rp_dd_select_customer(receive_payment_test_data)
    receive_payment.rp_payment_date(receive_payment_test_data)
    receive_payment.rp_reference_no()
    receive_payment.rp_dd_payment_method(receive_payment_test_data)
    receive_payment.rp_dd_deposit_to(receive_payment_test_data)
    time.sleep(3)
    receive_payment.rp_outstanding_transactions_check_and_enter_amount(receive_payment_test_data)
    receive_payment.rp_credits_check_and_enter_amount(receive_payment_test_data)
    receive_payment.rp_validate_total_amount_received_balance()

#Verify that total outstanding transactions amount should be total of outstanding transactions payment amount
def test_validate_total_outstanding_transactions_balance(setup, receive_payment_test_data):
    driver = setup
    receive_payment = ReceivePayment(driver)

    logger.info("Test case started for create invoice")
    receive_payment.recpay_mod_sales()
    #receive_payment.rp_submod_invoice()
    receive_payment.rp_submod_recpay()
    receive_payment.rp_dd_select_customer(receive_payment_test_data)
    receive_payment.rp_payment_date(receive_payment_test_data)
    receive_payment.rp_reference_no()
    receive_payment.rp_dd_payment_method(receive_payment_test_data)
    receive_payment.rp_dd_deposit_to(receive_payment_test_data)
    time.sleep(3)
    receive_payment.rp_outstanding_transactions_check_and_enter_amount(receive_payment_test_data)
    receive_payment.rp_validate_total_outstanding_transaction_balance()

#Verify that total credits amount should be total of credits payment amount
def test_validate_total_credits_balance(setup, receive_payment_test_data):
    driver = setup
    receive_payment = ReceivePayment(driver)

    logger.info("Test case started for create invoice")
    receive_payment.recpay_mod_sales()
    #receive_payment.rp_submod_invoice()
    receive_payment.rp_submod_recpay()
    receive_payment.rp_dd_select_customer(receive_payment_test_data)
    receive_payment.rp_payment_date(receive_payment_test_data)
    receive_payment.rp_reference_no()
    receive_payment.rp_dd_payment_method(receive_payment_test_data)
    receive_payment.rp_dd_deposit_to(receive_payment_test_data)
    time.sleep(3)
    receive_payment.rp_outstanding_transactions_check_and_enter_amount(receive_payment_test_data)
    receive_payment.rp_validate_total_credits_balance()
