import logging
import time


import pytest
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.core import driver
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.conftest import receive_payment_test_data



from actions.actions import Actions


class ReceivePayment:
    def __init__(self, driver):
        #self.expected_name = None
        self.expected_ref_no = None
        self.driver = driver
        self.actions = Actions(driver)

    recpay_btn_mod_Sales = (By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
    recpay_btn_submod_invoice = (By.XPATH, "//a[@class='nav-link'][normalize-space()='Invoices']")
    recpay_btn_submod_recpay= (By.XPATH, "//*[@id='root']/div/div[1]/div[1]/ul/div/div[1]/div[2]/div/div/div/div/li[3]/ul/li[5]/a")
    recpay_btn_receive_payment = (By.XPATH, "//button[@id='zoom-primary']")
    recpay_dd_select_customer = (By.XPATH,"//*[@id='react-select-2-input']")
    recpay_options_customer = By.XPATH,"//div[contains(@class, 'option')]"
    recpay_date_payment_date = (By.XPATH,"//input[@id='payment_date']")
    recpay_datepicker_month_class = (By.CLASS_NAME, "react-datepicker__current-month")
    recpay_next_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--next")
    recpay_prev_btn_class = (By.CLASS_NAME,"react-datepicker__navigation--previous")
    recpay_reference_no = (By.XPATH,"//input[@id='reference_no']")
    recpay_payment_method = (By.XPATH,"//select[@id='payment_method']")
    recpay_payment_method_options = (By.XPATH,"//select[@id='payment_method']/option")
    recpay_deposit_to = (By.XPATH,"//input[1][@role='combobox' and @aria-autocomplete='list' and @id ='react-select-3-input']")
    recpay_deposit_to_options = (By.XPATH,"//div[contains(@class, 'option')]")
    recpay_outstanding_transaction_table_invoice_no = (By.XPATH,"//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//td[2]")
    recpay_outstanding_transaction_table_row = (By.XPATH,"//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//tbody//tr")
    recpay_outstanding_transaction_table_chkbx = (By.XPATH,"//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//td[1]")
    recpay_credit_table_invoice_no = (By.XPATH,"//h5[text()='Credits']/following::table[@class='table table-hover'][1]//td[2]")
    recpay_credit_table_row = (By.XPATH,"//h5[text()='Credits']/following::table[@class='table table-hover'][1]//tbody//tr")
    recpay_credit_chkbx = (By.XPATH, "//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//td[1]")
    recpay_txt_total_outstanding_transaction=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[4]/div[2]/div[1]/div[4]/h5[1]/span[1]")
    recpay_txt_total_credits = (By.XPATH,"//div[6]//div[2]//div[1]//div[4]//h5[1]//span[1]")
    recpay_txt_amount_received =(By.XPATH,"//div[@class='col-md-3 pb-5']//span[1]")
    recpay_memo = (By.XPATH,"//textarea[@aria-label='With textarea']")
    recpay_btn_cancel = (By.XPATH,"//div[@class='expense-footer-btns']//div[1]//button[1]")
    recpay_btn_clr = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[2]")
    recpay_btn_save_close=(By.XPATH, "//div[@class='col-md-12']//div[2]//button[1]")
    recpay_btn_save_new=(By.XPATH, "//div[@class='col-md-12']//div[2]//button[2]")

    def recpay_mod_sales(self):
        self.actions.wait_for_element(self.recpay_btn_mod_Sales)
        self.actions.click(self.recpay_btn_mod_Sales)
        time.sleep(2)

    def rp_submod_invoice(self):
        self.actions.wait_for_element(self.recpay_btn_submod_invoice)
        self.actions.click(self.recpay_btn_submod_invoice)
        time.sleep(2)

    def rp_submod_recpay(self):
        self.actions.wait_for_element(self.recpay_btn_submod_recpay)
        self.actions.click(self.recpay_btn_submod_recpay)
        time.sleep(2)

    def rp_btn_receive_payment(self):
        self.actions.wait_for_element(self.recpay_btn_receive_payment)
        self.actions.click(self.recpay_btn_receive_payment)
        time.sleep(2)

    def rp_dd_select_customer(self, receive_payment_test_data):
        self.actions.scroll_to_the_element(self.recpay_dd_select_customer)
        self.actions.wait_for_element(self.recpay_dd_select_customer)
        self.actions.dropdown_contains(self.recpay_dd_select_customer, self.recpay_options_customer,receive_payment_test_data["rp_customer"])


    def rp_payment_date(self,create_invoice_test_data):
        self.actions.scroll_to_the_element(self.recpay_date_payment_date)
        self.actions.wait_for_element(self.recpay_date_payment_date)
        self.actions.select_date(self.recpay_date_payment_date, self.recpay_datepicker_month_class, self.recpay_next_btn_class, self.recpay_prev_btn_class, create_invoice_test_data["receive_payment_date"])

    def rp_reference_no(self):
        self.actions.scroll_to_the_element(self.recpay_reference_no)
        self.actions.wait_for_element(self.recpay_reference_no)
        self.expected_ref_no = self.actions.get_attribute(self.recpay_reference_no)
        print(self.expected_ref_no)

    def rp_dd_payment_method(self, create_invoice_test_data):
        self.actions.scroll_to_the_element(self.recpay_payment_method)
        self.actions.wait_for_element(self.recpay_payment_method)
        self.actions.dropdown_equals(self.recpay_payment_method, self.recpay_payment_method_options,create_invoice_test_data["rp_payment_method"])

    def rp_dd_deposit_to(self, create_invoice_test_data):
        self.actions.scroll_to_the_element(self.recpay_deposit_to)
        self.actions.wait_for_element(self.recpay_deposit_to)
        self.actions.dropdown_contains(self.recpay_deposit_to, self.recpay_deposit_to_options,create_invoice_test_data["rp_deposit_to"])



    def rp_outstanding_transactions_check_and_enter_amount(self, receive_payment_test_data):
        invoices_to_check = receive_payment_test_data["invoices_to_check"]
        table_xpath = "//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//tbody//tr"


        # Scroll and wait for table to be visible
        self.actions.scroll_to_the_element((By.XPATH, table_xpath))
        yash = self.actions.wait_for_element((By.XPATH, table_xpath))


        found_invoices = []

        retries = 3
        while retries > 0:
            try:
                rows = self.driver.find_elements(By.XPATH, table_xpath)

                for row in rows:
                    invoices_text = row.find_element(By.XPATH, ".//td[2]//a").get_attribute("textContent").strip()
                    print(f"🧾 Found invoice in table: '{invoices_text}'")

                    for invoice_data in invoices_to_check:
                        expected_invoice = invoice_data["invoice_no"]
                        if expected_invoice == invoices_text and invoices_text not in found_invoices:
                            checkbox = row.find_element(By.XPATH, "./td[1]//input[@type='checkbox']")
                            if not checkbox.is_selected():
                                checkbox.click()

                            payment_input = row.find_element(By.XPATH, "./td[6]//input")
                            payment_input.clear()
                            payment_input.send_keys(invoice_data["payment_amount"])

                            print(f"✅ Checked {expected_invoice} and entered ₹{invoice_data['payment_amount']}")
                            found_invoices.append(invoices_text)
                break  # Exit retry loop if successful
            except StaleElementReferenceException:
                print("⚠️ Stale element encountered, retrying...")
                time.sleep(1)
                retries -= 1

        # ✅ Final comparison and assertion
        expected_invoices = {i["invoice_no"] for i in invoices_to_check}
        actual_invoices = set(found_invoices)

        print(f"\n🔍 Expected invoices: {expected_invoices}")
        print(f"📌 Found invoices: {actual_invoices}")

        assert expected_invoices == actual_invoices, \
            f"❌ Missing invoices: {expected_invoices - actual_invoices}"

    def rp_credits_check_and_enter_amount(self, receive_payment_test_data):
        credits_to_check = receive_payment_test_data["credits_to_check"]
        table_xpath = "//h5[text()='Credits']/following::table[@class='table table-hover'][1]//tbody//tr"

        # Scroll and wait for table to be visible
        self.actions.scroll_to_the_element((By.XPATH, table_xpath))
        self.actions.wait_for_element((By.XPATH, table_xpath))

        found_credits = []

        retries = 3
        while retries > 0:
            try:
                rows = self.driver.find_elements(By.XPATH, table_xpath)

                for row in rows:
                    credits_text = row.find_element(By.XPATH, ".//td[2]//a").get_attribute("textContent").strip()
                    print(f"🧾 Found credit in table: '{credits_text}'")

                    for credits_data in credits_to_check:
                        expected_credits = credits_data["credits_no"]
                        if expected_credits == credits_text and credits_text not in found_credits:
                            checkbox = row.find_element(By.XPATH, "./td[1]//input[@type='checkbox']")
                            if not checkbox.is_selected():
                                checkbox.click()

                            payment_input = row.find_element(By.XPATH, "./td[5]//input")
                            payment_input.clear()
                            payment_input.send_keys(credits_data["credits_payment_amount"])

                            print(f"✅ Checked {expected_credits} and entered ₹{credits_data['credits_payment_amount']}")
                            found_credits.append(credits_text)
                break  # Exit retry loop if successful
            except StaleElementReferenceException:
                print("⚠️ Stale element encountered, retrying...")
                time.sleep(1)
                retries -= 1

        # ✅ Final comparison and assertion
        expected_credits = {i["credits_no"] for i in credits_to_check}
        actual_credits = set(found_credits)

        print(f"\n🔍 Expected invoices: {expected_credits}")
        print(f"📌 Found invoices: {actual_credits}")

        assert expected_credits == actual_credits, \
            f"❌ Missing invoices: {expected_credits - actual_credits}"

    def rp_total_outstanding_transactions(self):
        self.actions.scroll_to_the_element(self.recpay_txt_total_outstanding_transaction)
        self.actions.wait_for_element(self.recpay_txt_total_outstanding_transaction)
        total_outstanding = self.actions.get_text(self.recpay_txt_total_outstanding_transaction)
        print(f"total_outstanding:{total_outstanding}")



    def rp_total_credits_transactions(self):
        self.actions.scroll_to_the_element(self.recpay_txt_total_credits)
        self.actions.wait_for_element(self.recpay_txt_total_credits)
        total_credits=self.actions.get_text(self.recpay_txt_total_credits)
        print(f"total_credits:{total_credits}")

    def rp_amount_received(self):
        self.actions.scroll_to_the_element(self.recpay_txt_amount_received)
        self.actions.wait_for_element(self.recpay_txt_amount_received)
        amount_received=self.actions.get_text(self.recpay_txt_amount_received)
        print(f"amount_received:{amount_received}")

    def rp_memo(self, receive_payment_test_data):
        self.actions.scroll_to_the_element(self.recpay_memo)
        self.actions.wait_for_element(self.recpay_memo)
        self.actions.send_keys(self.recpay_memo,receive_payment_test_data["rp_memo"])

    def rp_cancel(self):
        self.actions.wait_for_element(self.recpay_btn_cancel)
        self.actions.scroll_to_the_element(self.recpay_btn_cancel)
        self.actions.click(self.recpay_btn_cancel)

    def rp_clear(self):
        self.actions.wait_for_element(self.recpay_btn_clr)
        self.actions.scroll_to_the_element(self.recpay_btn_clr)
        self.actions.click(self.recpay_btn_clr)

    def rp_save_and_close(self):
        self.actions.wait_for_element(self.recpay_btn_save_close)
        self.actions.scroll_to_the_element(self.recpay_btn_save_close)
        self.actions.click(self.recpay_btn_save_close)

    def rp_save_and_new(self):
        self.actions.wait_for_element(self.recpay_btn_save_new)
        self.actions.scroll_to_the_element(self.recpay_btn_save_new)
        self.actions.click(self.recpay_btn_save_new)

    def rp_validate_total_amount_received_balance(self):
        # 1. Get all Outstanding Transaction Payment inputs
        outstanding_inputs = self.driver.find_elements(By.XPATH,"//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//tbody//tr//td[6]//input")
        outstanding_sum = 0
        for input_el in outstanding_inputs:
            val = input_el.get_attribute("value").strip()
            if val:
                outstanding_sum += float(val)

        # 2. Get all Credit Payment inputs
        credit_inputs = self.driver.find_elements(By.XPATH, "//h5[text()='Credits']/following::table[@class='table table-hover'][1]//tbody//tr//td[5]//input")
        credit_sum = 0
        for input_el in credit_inputs:
            val = input_el.get_attribute("value").strip()
            if val:
                credit_sum += float(val)

        # 3. Get displayed "Total Credit"
        total_amount_received_element = self.driver.find_element(By.XPATH,"//div[6]//div[2]//div[1]//div[4]//h5[1]//span[1]")
        total_amount_received_text = total_amount_received_element.text.strip().replace("₹", "").replace(",", "")
        displayed_total_amount_received = float(total_amount_received_text)

        # 4. Calculate expected total credit
        calculated_amount_received_credit = outstanding_sum - credit_sum

        print(f"🧾 Outstanding Total: ₹{outstanding_sum}")
        print(f"🧾 Credit Used: ₹{credit_sum}")
        print(f"✅ Calculated Total Amount received: ₹{calculated_amount_received_credit}")
        print(f"📌 Displayed Total Amount received: ₹{displayed_total_amount_received}")

        # 5. Assertion
        assert round(calculated_amount_received_credit, 2) == round(displayed_total_amount_received, 2), \
            f"❌ Mismatch: Expected ₹{calculated_amount_received_credit}, but found ₹{displayed_total_amount_received}"

    def rp_validate_total_outstanding_transaction_balance(self):
        # 1. Get all Outstanding Transaction Payment inputs
        outstanding_inputs = self.driver.find_elements(By.XPATH,"//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//tbody//tr//td[6]//input")
        outstanding_sum = 0
        for input_el in outstanding_inputs:
            val = input_el.get_attribute("value").strip()
            if val:
                outstanding_sum += float(val)

        # 2. Get displayed "Total Outstanding Transaction"
        total_outstanding_transactions_element = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[4]/div[2]/div[1]/div[4]/h5[1]/span[1]")
        total_outstanding_transactions_text = total_outstanding_transactions_element.text.strip().replace("₹", "").replace(",", "")
        displayed_outstanding_transactions_received = float(total_outstanding_transactions_text)

        # 3. Assertion
        assert round(outstanding_sum, 2) == round(displayed_outstanding_transactions_received, 2), \
            f"❌ Mismatch: Expected ₹{outstanding_sum}, but found ₹{displayed_outstanding_transactions_received}"

    def rp_validate_total_credits_balance(self):
        # 1. Get all Credit Payment inputs
        credit_inputs = self.driver.find_elements(By.XPATH, "//h5[text()='Credits']/following::table[@class='table table-hover'][1]//tbody//tr//td[5]//input")
        credit_sum = 0
        for input_el in credit_inputs:
            val = input_el.get_attribute("value").strip()
            if val:
                credit_sum += float(val)

        # 2. Get displayed "Total Credits"
        total_credits_element = self.driver.find_element(By.XPATH,"//div[6]//div[2]//div[1]//div[4]//h5[1]//span[1]")
        total_credits_text = total_credits_element.text.strip().replace("₹", "").replace(",", "")
        displayed_credits_received = float(total_credits_text)

        # 3. Assertion
        assert round(credit_sum, 2) == round(displayed_credits_received, 2), \
            f"❌ Mismatch: Expected ₹{credit_sum}, but found ₹{displayed_credits_received}"

