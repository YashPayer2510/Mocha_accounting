import logging
import time

import pytest
from self import driver

from pages.chart_of_accounts.create_chart_of_accounts import CreateCOA
#from dotenv import load_dotenv
import allure
logger = logging.getLogger(__name__)

@pytest.mark.needs_login
def test_ete_create_chart_of_account(cao_setup,create_coa_test_data ):
    driver = cao_setup
    create_coa = CreateCOA(driver)

    create_coa.create_coa_accounting_modul_click()
    logger.info("clicked on Accounting module")
    create_coa.create_coa_submodule_click()
    logger.info("clicked on Chart of account sub-module")
    time.sleep(2)
    create_coa.page_refresh()
    create_coa.create_coa_new_btn_click()
    logger.info("clicked on new button")
    create_coa.create_coa_account_type_dd(create_coa_test_data)
    logger.info("selected Account type")
    create_coa.create_coa_detail_type_dd(create_coa_test_data)
    logger.info("selected Detailed type")
    chart_of_account_name = create_coa.create_coa_enter_account_name(create_coa_test_data)
    logger.info("Account name entered")
    create_coa.create_coa_enter_account_number(create_coa_test_data)
    logger.info("Account number entered")
    create_coa.create_coa_enter_opening_balance(create_coa_test_data)
    logger.info("Opening balance entered")
    create_coa.create_coa_select_as_of_date(create_coa_test_data)
    logger.info("As of date selected")
    create_coa.create_coa_click_save_btn()
    logger.info("Clicked on save button")
    return chart_of_account_name

