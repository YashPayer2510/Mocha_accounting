import logging
import re
import time

import pytest
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.actions import Actions


class AllSales:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)

all_sales_type_dd =(By.XPATH,"//div[@style='display: flex; gap: 10px; flex-direction: column;'][1]//select")
all_sales_options_type_dd = (By.XPATH,"//div[@style='display: flex; gap: 10px; flex-direction: column;'][1]//select//option")
all_sales_status_dd = (By.XPATH,"//div[@style='display: flex; gap: 10px; flex-direction: column;'][2]//select")
all_sales_options_status_dd = (By.XPATH,"//div[@style='display: flex; gap: 10px; flex-direction: column;'][2]//select//option")
all_sales_search_customer=(By.XPATH,"//input[@name='searchBar' or @label='Customer']")
all_sales_new_transaction_dd= (By.XPATH,"//button[normalize-space()='New Transaction']")
all_sales_new_transaction_dd_invoices= (By.XPATH,"//a[@class='dropdown-item sc-eDPEul inWBsQ'][normalize-space()='Invoice']")
all_sales_new_transaction_dd_receive_payment= (By.XPATH,"//a[@class='dropdown-item sc-eDPEul inWBsQ'][normalize-space()='Receive Payment']")
all_sales_new_transaction_dd_credit_memo= (By.XPATH,"//a[@class='dropdown-item sc-eDPEul inWBsQ'][normalize-space()='Credit Memo']")
all_sales_new_transaction_dd_sales_receipt = (By.XPATH,"//a[@class='dropdown-item sc-eDPEul inWBsQ'][normalize-space()='Sales Receipt']")
all_sales_new_transaction_dd_refund_receipt = (By.XPATH,"//a[@class='dropdown-item sc-eDPEul inWBsQ'][normalize-space()='Refund Receipt']")
all_sales_table_rows =(By.XPATH,"//table//tr")
all_sales_table_recurring_column=(By.XPATH,"//table//tr//td[1]")
all_sales_table_date_column = (By.XPATH, "//table//tr//td[2]")
all_sales_table_type_column = (By.XPATH, "//table//tr//td[3]")
all_sales_table_transaction_no_column = (By.XPATH, "//table//tr//td[4]")
all_sales_table_customer_name_column = (By.XPATH, "//table//tr//td[5]")
all_sales_table_due_Date_column = (By.XPATH, "//table//tr//td[6]")
all_sales_table_balance_column = (By.XPATH, "//table//tr//td[7]")
all_sales_table_amount_column = (By.XPATH, "//table//tr//td[8]")
all_sales_table_status_column = (By.XPATH, "//table//tr//td[9]")
all_sales_table_send_column = (By.XPATH, "//table//tr//td[10]")
all_sales_table_actions_column = (By.XPATH, "//table//tr//td[11]")
all_sales_next_btn=(By.XPATH,"//a[normalize-space()='>']")
all_sales_page_dropdown = (By.XPATH,"//button[@id='pageDropDown']")
all_sales_page_dd_option25 = (By.XPATH,"//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), '25')]")
all_sales_page_dd_option30 = (By.XPATH, "//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), '30')]")
all_sales_page_dd_option50 = (By.XPATH, "//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), '50')]")
all_sales_pagination_count_text = (By.XPATH,"//span[@class='react-bootstrap-table-pagination-total']")



