import time

from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from actions.actions import Actions

class BillPayment:
    def __init__(self, driver):
        self.expected_ref_no = None
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 100)

    bill_pay_mod_exp = (By.XPATH,"//img[@src='/svgs/expense.svg']")
    bill_pay_expense_list_submod = (By.XPATH,"//a[normalize-space()='Expenses']")
    bill_pay_expense_list_type_dd = (By.XPATH, "//label[text()='Type']/following-sibling::select")
    bill_pay_options_expense_list_type = (By.XPATH, "//label[text()='Type']/following-sibling::select/option")
    bill_pay_expense_list_table_type_column = (By.XPATH, "//table//tr//td[3]")
    bill_pay_expense_list_table_actions_column = (By.XPATH, "//table//tr//td[12]")
    bill_pay_expense_list_mark_as_paid_btn = (By.XPATH,"//table//tr//td[12]//button[contains(@class, 'expenseListMarkAsPaidTour')]")
    bill_pay_expense_list_table_rows = (By.XPATH, "//table//tbody//tr")
    bill_pay_expense_list_table_transaction_no_column = (By.XPATH, "//table//tr//td[4]")
    bill_pay_dd_select_payee = (By.XPATH, "//label[text()='Payee']/following-sibling::select[contains(@id, 'contact_id')]")
    bill_pay_options_payee = (By.XPATH, "//label[text()='Payee']/following-sibling::select/option")
    bill_pay_payment_account_dd = (By.XPATH,"//label[text()='Payment Account']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    bill_pay_options_payment_account_dd = (By.XPATH,"//div[contains(@class, 'option')]")
    bill_pay_mailing_address = (By.XPATH,"//textarea[@name= 'mailing_address']")
    bill_pay_date = (By.XPATH, "//input[@id='payment_date']")
    bill_pay_date_datepicker_current_month_class = (By.CLASS_NAME, "react-datepicker__current-month")
    bill_pay_date_next_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--next")
    bill_pay_date_prev_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--previous")
    bill_pay_ref_no = (By.XPATH, "//input[@id='payment_date']")
    bill_pay_outstanding_transaction_table_bill_no = (By.XPATH,"//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//td[2]")
    bill_pay_outstanding_transaction_table_row = (By.XPATH, "//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//tbody//tr")
    bill_pay_outstanding_transaction_table_chkbx = (By.XPATH, "//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//td[1]")
    bill_pay_outstanding_transaction_table_due_date = (By.XPATH,"//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//td[3]")
    bill_pay_outstanding_transaction_table_original_amt = (By.XPATH,"//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//td[4]")
    bill_pay_outstanding_transaction_table_open_balance = (By.XPATH,"//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//td[5]")
    bill_pay_outstanding_transaction_table_payment_amt = (By.XPATH,"//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//input[@id='payment']")
    bill_pay_credit_table_credit_no = (By.XPATH, "//h5[text()='Credits']/following::table[@class='table table-hover'][1]//td[2]")
    bill_pay_credit_table_row = (By.XPATH, "//h5[text()='Credits']/following::table[@class='table table-hover'][1]//tbody//tr")
    bill_pay_credit_chkbx = (By.XPATH, "//h5[text()='Credits']/following::table[@class='table table-hover'][1]//td[1]")
    bill_pay_credit_table_original_amt= (By.XPATH, "//h5[text()='Credits']/following::table[@class='table table-hover'][1]//td[3]")
    bill_pay_credit_open_balance = (By.XPATH, "//h5[text()='Credits']/following::table[@class='table table-hover'][1]//td[4]")
    bill_pay_credit_credit_payment = (By.XPATH, "//h5[text()='Credits']/following::table[@class='table table-hover'][1]//td[5]")
    bill_pay_txt_total_outstanding_transaction = (By.XPATH,"//div[5]//div[2]//div[1]//div[4]//h5[1]//span[1]")
    bill_pay_txt_total_credits = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[7]/div[2]/div[1]/div[4]/h5[1]/span[1]")
    bill_pay_txt_amount_received = (By.XPATH, "//div[@class='col-xl-6 col-lg-6 col-md-12 d-flex justify-content-end']//span[1]")
    bill_pay_memo = (By.XPATH, "//textarea[@name='memo']")
    bill_pay_btn_cancel = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[1]")
    bill_pay_btn_clr = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[2]")
    bill_pay_btn_save_close = (By.XPATH, "//div[@class='col-md-12']//div[2]//button[1]")
    bill_pay_btn_save_new = (By.XPATH, "//div[@class='col-md-12']//div[2]//button[2]")
    bill_pay_btn_x = (By.XPATH, "//div[contains(@class, 'toast') and contains(@class, 'show')]//button[contains(@class, 'btn-close')]")


    def bill_b_exp_mod(self):
        self.actions.wait_for_element(self.bill_pay_mod_exp)
        self.actions.scroll_to_the_element(self.bill_pay_mod_exp)
        self.actions.click(self.bill_pay_mod_exp)

    def bill_b_exp_list_submod(self):
        self.actions.wait_for_element(self.bill_pay_expense_list_submod)
        self.actions.scroll_to_the_element(self.bill_pay_expense_list_submod)
        self.actions.click(self.bill_pay_expense_list_submod)
        time.sleep(10)

    def bill_p_mark_as_paid_click(self,bill_payment_test_data):
        self.wait.until(EC.presence_of_all_elements_located(self.bill_pay_expense_list_type_dd))
        self.actions.dropdown_select(self.bill_pay_expense_list_type_dd,bill_payment_test_data["bill_payment_transaction_type"])
        self.wait.until(EC.presence_of_all_elements_located(self.bill_pay_expense_list_table_rows))
        self.actions.scroll_to_the_element(self.bill_pay_expense_list_table_rows)
        time.sleep(2)  # Reduced from 20 to 2 seconds for better performance

        # Get all table rows
        rows = self.driver.find_elements(*self.bill_pay_expense_list_table_rows)

        # Get the expected transaction number from test data
        expected_transaction_no = bill_payment_test_data["bill_payment_transaction_no"].strip().lower()

        found = False

        for row in rows:
            # Get the transaction number cell (4th column based on your table structure)
            try:
                transaction_no_cell = row.find_element(*self.bill_pay_expense_list_table_transaction_no_column)
                transaction_no_text = transaction_no_cell.text.strip().lower()

                if transaction_no_text == expected_transaction_no:
                    # Find and click the "Mark as Paid" button in the ACTION column (last column)
                    action_button = row.find_element(*self.bill_pay_expense_list_mark_as_paid_btn)
                    action_button.click()
                    found = True
                    break
            except NoSuchElementException:
                continue

        if not found:
            raise AssertionError(f"Transaction with number '{expected_transaction_no}' not found in the table")

        # Optional: Add verification that the status changed to "Paid"
        # You might need to add a locator for the status column

    def bill_p_dd_select_payee(self, bill_payment_test_data):
        self.actions.scroll_to_the_element(self.bill_pay_dd_select_payee)
        self.actions.wait_for_element(self.bill_pay_dd_select_payee)
        self.actions.dropdown_contains(self.bill_pay_dd_select_payee, self.bill_pay_options_payee,bill_payment_test_data["bill_payment_payee"])

    def bill_p_dd_payment_account(self, bill_payment_test_data):
        self.actions.scroll_to_the_element(self.bill_pay_payment_account_dd)
        self.actions.wait_for_element(self.bill_pay_payment_account_dd)
        self.actions.dropdown_contains(self.bill_pay_payment_account_dd, self.bill_pay_options_payment_account_dd,bill_payment_test_data["bill_payment_payment_account"])

    def bill_p_payment_date(self, bill_payment_test_data):
        self.actions.scroll_to_the_element(self.bill_pay_date)
        self.actions.wait_for_element(self.bill_pay_date)
        self.actions.select_date(self.bill_pay_date, self.bill_pay_date_datepicker_current_month_class,
                                 self.bill_pay_date_next_btn_class, self.bill_pay_date_prev_btn_class,
                                 bill_payment_test_data["bill_payment_date"])

    def bill_p_reference_no(self, bill_payment_test_data):
        self.actions.scroll_to_the_element(self.bill_pay_ref_no)
        self.actions.wait_for_element(self.bill_pay_ref_no)
        self.expected_ref_no = self.actions.get_attribute(self.bill_pay_ref_no)
        print(self.expected_ref_no)
        self.actions.clear_text(self.bill_pay_ref_no)
        self.actions.send_keys(self.bill_pay_ref_no,bill_payment_test_data["bill_payment_ref_no"])


    def bill_p_outstanding_transactions_check_and_enter_amount(self, bill_payment_test_data):
        bills_to_check = bill_payment_test_data["bill_to_check"]
        table_xpath = self.bill_pay_outstanding_transaction_table_row


        # Scroll and wait for table to be visible
        self.actions.scroll_to_the_element(table_xpath)



        found_bills = []

        retries = 3
        while retries > 0:
            try:
                rows = self.driver.find_elements(*table_xpath)

                for row in rows:
                    bill_text = row.find_element(*self.bill_pay_outstanding_transaction_table_bill_no).get_attribute("textContent").strip()
                    print(f"🧾 Found invoice in table: '{bill_text}'")

                    for bill_data in bills_to_check:
                        expected_invoice = bill_data["bill_no"]
                        if expected_invoice == bill_text and bill_text not in found_bills:
                            checkbox = row.find_element(*self.bill_pay_outstanding_transaction_table_chkbx)
                            if not checkbox.is_selected():
                                checkbox.click()

                            payment_input = row.find_element(*self.bill_pay_outstanding_transaction_table_payment_amt)
                            payment_input.clear()
                            payment_input.send_keys(bill_data["payment_amount"])

                            print(f"✅ Checked {expected_invoice} and entered ₹{bill_data['payment_amount']}")
                            found_bills.append(bill_text)
                break  # Exit retry loop if successful
            except StaleElementReferenceException:
                print("⚠️ Stale element encountered, retrying...")
                time.sleep(1)
                retries -= 1

        # ✅ Final comparison and assertion
        expected_bill = {i["bill_no"] for i in bills_to_check}
        actual_bills = set(found_bills)

        print(f"\n🔍 Expected invoices: {expected_bill}")
        print(f"📌 Found invoices: {actual_bills}")

        assert expected_bill == actual_bills, \
            f"❌ Missing invoices: {expected_bill - actual_bills}"

    def bill_p_credits_check_and_enter_amount(self, bill_payment_test_data):
        credits_to_check = bill_payment_test_data["credits_to_check"]
        table_xpath = self.bill_pay_credit_table_row
        # Scroll and wait for table to be visible
        self.actions.scroll_to_the_element(table_xpath)
        self.actions.wait_for_element(table_xpath)

        found_credits = []

        retries = 3
        while retries > 0:
            try:
                rows = self.driver.find_elements(*table_xpath)

                for row in rows:
                    credits_text = row.find_element(*self.bill_pay_credit_table_credit_no).get_attribute("textContent").strip()
                    print(f"🧾 Found credit in table: '{credits_text}'")

                    for credits_data in credits_to_check:
                        expected_credits = credits_data["credits_no"]
                        if expected_credits == credits_text and credits_text not in found_credits:
                            checkbox = row.find_element(*self.bill_pay_credit_chkbx)
                            if not checkbox.is_selected():
                                checkbox.click()

                            payment_input = row.find_element(*self.bill_pay_credit_credit_payment)
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


    def bill_p_click_x_button(self):
        self.actions.wait_for_element(self.bill_pay_btn_x)
        self.actions.click(self.bill_pay_btn_x)
        time.sleep(2)