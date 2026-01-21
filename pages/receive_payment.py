import time

from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By

from actions.actions import Actions


class ReceivePayment:
    def __init__(self, driver):
        self.expected_ref_no = None
        self.driver = driver
        self.actions = Actions(driver)

    recpay_btn_mod_Sales = (By.XPATH,"//img[@src='/svgs/sales.svg']")
    recpay_btn_submod_invoice = (By.XPATH, "//a[@class='nav-link'][normalize-space()='Invoices']")
    recpay_btn_submod_recpay= (By.XPATH, "//a[@class='nav-link'][normalize-space()='Receive Payment']")
    recpay_btn_receive_payment = (By.XPATH, "//button[@id='zoom-primary']")
    recpay_dd_select_customer = (By.XPATH,"//label[text()='Customer *']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    recpay_options_customer = By.XPATH,"//div[contains(@class, 'option')]"
    recpay_date_payment_date = (By.XPATH,"//input[@id='payment_date']")
    recpay_datepicker_month_class = (By.CLASS_NAME, "react-datepicker__current-month")
    recpay_next_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--next")
    recpay_prev_btn_class = (By.CLASS_NAME,"react-datepicker__navigation--previous")
    recpay_reference_no = (By.XPATH,"//input[@id='reference_no']")
    recpay_payment_method = (By.XPATH,"//select[@id='payment_method']")
    recpay_payment_method_options = (By.XPATH,"//select[@id='payment_method']/option")
    recpay_deposit_to = (By.XPATH,"//label[text()='Deposit To *']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    recpay_deposit_to_options = (By.XPATH,"//div[contains(@class, 'option')]")
    recpay_outstanding_transaction_table_invoice_no = (By.XPATH,"//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//td[2]")
    recpay_outstanding_transaction_table_row = (By.XPATH,"//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//tbody//tr")
    recpay_outstanding_transaction_table_chkbx = (By.XPATH,"//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//td[1]")
    recpay_credit_table_invoice_no = (By.XPATH,"//h5[text()='Credits']/following::table[@class='table table-hover'][1]//td[2]")
    recpay_credit_table_row = (By.XPATH,"//h5[text()='Credits']/following::table[@class='table table-hover'][1]//tbody//tr")
    recpay_credit_chkbx = (By.XPATH, "//h5[text()='Credits']/following::table[@class='table table-hover'][1]//td[1]")
    recpay_txt_total_outstanding_transaction=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[4]/div[2]/div[1]/div[4]/h5[1]/span[1]")
    recpay_txt_total_credits = (By.XPATH,"//div[6]//div[2]//div[1]//div[4]//h5[1]//span[1]")
    recpay_txt_amount_received =(By.XPATH,"//div[@class='col-md-3 pb-5']//span[1]")
    recpay_memo = (By.XPATH,"//textarea[@aria-label='With textarea']")
    recpay_btn_cancel = (By.XPATH,"//div[@class='expense-footer-btns']//div[1]//button[1]")
    recpay_btn_clr = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[2]")
    recpay_btn_save_close=(By.XPATH, "//div[@class='col-md-12']//div[2]//button[1]")
    recpay_btn_save_new=(By.XPATH, "//div[@class='col-md-12']//div[2]//button[2]")

    recpay_all_sales_transaction_no_column_tbl= (By.XPATH,"//table//td[4]")
    recpay_all_sales_btn_nxt_invoicelist = (By.XPATH,"//a[normalize-space()='>']")

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

    def rp_dd_select_customer_sales_flow(self, customer_name):
        self.actions.scroll_to_the_element(self.recpay_dd_select_customer)
        self.actions.wait_for_element(self.recpay_dd_select_customer)
        self.actions.dropdown_contains(self.recpay_dd_select_customer, self.recpay_options_customer,customer_name)



    def rp_payment_date(self,receive_payment_test_data):
        self.actions.scroll_to_the_element(self.recpay_date_payment_date)
        self.actions.wait_for_element(self.recpay_date_payment_date)
        self.actions.select_date(self.recpay_date_payment_date, self.recpay_datepicker_month_class, self.recpay_next_btn_class, self.recpay_prev_btn_class, receive_payment_test_data["receive_payment_date"])

    def rp_reference_no(self):
        self.actions.scroll_to_the_element(self.recpay_reference_no)
        self.actions.wait_for_element(self.recpay_reference_no)
        self.expected_ref_no = self.actions.get_attribute_value(self.recpay_reference_no)
        print(self.expected_ref_no)

    def rp_dd_payment_method(self, receive_payment_test_data):
        self.actions.scroll_to_the_element(self.recpay_payment_method)
        self.actions.wait_for_element(self.recpay_payment_method)
        self.actions.dropdown_equals(self.recpay_payment_method, self.recpay_payment_method_options,receive_payment_test_data["rp_payment_method"])


    def rp_dd_deposit_to(self, receive_payment_test_data):
        self.actions.scroll_to_the_element(self.recpay_deposit_to)
        self.actions.wait_for_element(self.recpay_deposit_to)
        self.actions.dropdown_contains(self.recpay_deposit_to, self.recpay_deposit_to_options,receive_payment_test_data["rp_deposit_to"])

    def rp_dd_deposit_to_sales_flow(self, deposit_to_coa):
        self.actions.scroll_to_the_element(self.recpay_deposit_to)
        self.actions.wait_for_element(self.recpay_deposit_to)
        self.actions.dropdown_contains(self.recpay_deposit_to, self.recpay_deposit_to_options, deposit_to_coa)



    def rp_outstanding_transactions_check_and_enter_amount(self, receive_payment_test_data):
        invoices_to_check = receive_payment_test_data["invoices_to_check"]
        table_xpath = "//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//tbody//tr"


        # Scroll and wait for table to be visible
        self.actions.scroll_to_the_element((By.XPATH, table_xpath))


        found_invoices = []

        retries = 3
        while retries > 0:
            try:
                rows = self.driver.find_elements(By.XPATH, table_xpath)

                for row in rows:
                    invoices_text = row.find_element(By.XPATH, ".//td[2]//a").get_attribute("textContent").strip()
                    print(f" Found invoice in table: '{invoices_text}'")

                    for invoice_data in invoices_to_check:
                        expected_invoice = invoice_data["invoice_no"]
                        if expected_invoice == invoices_text and invoices_text not in found_invoices:
                            checkbox = row.find_element(By.XPATH, "./td[1]//input[@type='checkbox']")
                            if not checkbox.is_selected():
                                checkbox.click()

                            payment_input = row.find_element(By.XPATH, "./td[6]//input")
                            payment_input.clear()
                            payment_input.send_keys(invoice_data["payment_amount"])

                            print(f"Checked {expected_invoice} and entered ₹{invoice_data['payment_amount']}")
                            found_invoices.append(invoices_text)
                break  # Exit retry loop if successful
            except StaleElementReferenceException:
                print("Stale element encountered, retrying...")
                time.sleep(1)
                retries -= 1

        #  Final comparison and assertion
        expected_invoices = {i["invoice_no"] for i in invoices_to_check}
        actual_invoices = set(found_invoices)

        print(f"\n🔍 Expected invoices: {expected_invoices}")
        print(f" Found invoices: {actual_invoices}")

        assert expected_invoices == actual_invoices, \
            f" Missing invoices: {expected_invoices - actual_invoices}"

    def rp_outstanding_transactions_check_and_enter_amount_sales_flow(self, invoice_list, receive_payment_test_data):
        # Normalize invoice_list into list of dicts
        if isinstance(invoice_list, str):
            invoice_list = [{
                "invoice_no": invoice_list,
                "payment_amount": receive_payment_test_data.get(
                    "rp_payment_amt_outstanding_transaction", "0"
                )
            }]

        # Table rows under "Outstanding Transactions"
        table_xpath = "//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//tbody//tr"

        # NEXT button under only the Outstanding Transactions section
        next_button_xpath = (
            "//h5[normalize-space()='Outstanding Transactions']"
            "/following::ul[contains(@class,'pagination')][1]"
            "//a[@aria-label='Go to next page' and @aria-disabled='false']"
        )

        self.actions.scroll_to_the_element((By.XPATH, table_xpath))

        found_invoices = []

        expected_invoices = [item["invoice_no"] for item in invoice_list]

        # Continue until all invoices are found OR pages exhausted
        while True:

            retries = 3
            while retries > 0:
                try:
                    rows = self.driver.find_elements(By.XPATH, table_xpath)

                    for row in rows:
                        row_text = row.find_element(By.XPATH, ".//td[2]").get_attribute("textContent").strip()

                        for invoice_data in invoice_list:
                            expected_invoice = invoice_data["invoice_no"]

                            # If found on this page
                            if expected_invoice in row_text and expected_invoice not in found_invoices:

                                checkbox = row.find_element(By.XPATH, "./td[1]//input[@type='checkbox']")
                                if not checkbox.is_selected():
                                    checkbox.click()

                                payment_input = row.find_element(By.XPATH, "./td[6]//input")
                                payment_input.clear()
                                payment_input.send_keys(invoice_data["payment_amount"])

                                print(f"✓ Checked {expected_invoice} and entered ₹{invoice_data['payment_amount']}")
                                found_invoices.append(expected_invoice)

                    break  # processed current page successfully

                except StaleElementReferenceException:
                    print("Stale element, retrying...")
                    time.sleep(1)
                    retries -= 1

            # Stop if all found
            if set(found_invoices) == set(expected_invoices):
                break

            # Try clicking next pagination button
            try:
                next_button = self.driver.find_element(By.XPATH, next_button_xpath)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
                next_button.click()
                time.sleep(1.2)

            except Exception:
                # No Next button -> no more pages
                break

        # Final validation
        missing_invoices = [i for i in expected_invoices if i not in found_invoices]

        if missing_invoices:
            print(f"Missing invoices: {missing_invoices}")
            assert False, f"Missing invoices in outstanding transactions: {missing_invoices}"

        print("All expected invoices were found and processed successfully.")

    def rp_outstanding_transactions_check_and_enter_amount_new(self, receive_payment_test_data):
        invoices_to_check = receive_payment_test_data["invoices_to_check"]
        table_xpath = "//h5[text()='Outstanding Transactions']/following::table[@class='table table-hover'][1]//tbody//tr"
        self.actions.wait_for_element((By.XPATH, table_xpath))
        next_button_xpath = "//h5[normalize-space()='Outstanding Transactions']     /following::ul[contains(@class,'pagination')][1]     //a[@aria-label='Go to next page']"
        expected_invoices = {i["invoice_no"] for i in invoices_to_check}
        found_invoices = set()

        def process_table_rows():
            """Reads rows and returns number of newly found invoices."""
            rows = self.driver.find_elements(By.XPATH, table_xpath)
            new_found = 0

            for row in rows:
                try:
                    invoices_text = row.find_element(By.XPATH, ".//td[2]//a").get_attribute("textContent").strip()
                except:
                    continue

                for invoice_data in invoices_to_check:
                    expected_invoice = invoice_data["invoice_no"]

                    if expected_invoice == invoices_text and invoices_text not in found_invoices:
                        checkbox = row.find_element(By.XPATH, "./td[1]//input[@type='checkbox']")
                        if not checkbox.is_selected():
                            checkbox.click()

                        payment_input = row.find_element(By.XPATH, "./td[6]//input")
                        payment_input.clear()
                        payment_input.send_keys(invoice_data["payment_amount"])

                        found_invoices.add(invoices_text)
                        new_found += 1

                        print(f"Found & filled {expected_invoice}")

            return new_found
        while True:
            # Process the current page
            newly_found = process_table_rows()

            if found_invoices == expected_invoices:
                print("All invoices found, stopping pagination.")
                break  # All invoices located

            # Locate NEXT button
            try:
                next_button = self.driver.find_element(By.XPATH, next_button_xpath)
            except NoSuchElementException:
                print(" No NEXT button — reached last page.")
                break

            # Check if NEXT is disabled
            parent_li = next_button.find_element(By.XPATH, "./..")
            if "disabled" in parent_li.get_attribute("class"):
                print("NEXT button disabled — no more pages.")
                break

            # Click NEXT page and wait for load
            print("➡ Clicking NEXT to load more transactions...")
            self.driver.execute_script("arguments[0].click();", next_button)
            time.sleep(1.2)

        # Final assertion
        print(f"\nExpected: {expected_invoices}")
        print(f"Found:    {found_invoices}")

        assert expected_invoices == found_invoices, \
            f"Missing invoices: {expected_invoices - found_invoices}"

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
                    print(f"Found credit in table: '{credits_text}'")

                    for credits_data in credits_to_check:
                        expected_credits = credits_data["credits_no"]
                        if expected_credits == credits_text and credits_text not in found_credits:
                            checkbox = row.find_element(By.XPATH, "./td[1]//input[@type='checkbox']")
                            if not checkbox.is_selected():
                                checkbox.click()

                            payment_input = row.find_element(By.XPATH, "./td[5]//input")
                            payment_input.clear()
                            payment_input.send_keys(credits_data["credits_payment_amount"])

                            print(f"Checked {expected_credits} and entered ₹{credits_data['credits_payment_amount']}")
                            found_credits.append(credits_text)
                break  # Exit retry loop if successful
            except StaleElementReferenceException:
                print(" Stale element encountered, retrying...")
                time.sleep(1)
                retries -= 1

        # Final comparison and assertion
        expected_credits = {i["credits_no"] for i in credits_to_check}
        actual_credits = set(found_credits)

        print(f"\nExpected invoices: {expected_credits}")
        print(f" Found invoices: {actual_credits}")

        assert expected_credits == actual_credits, \
            f" Missing invoices: {expected_credits - actual_credits}"

    def rp_credits_check_and_enter_amount_sales_flow(self, receive_payment_test_data):
        credits_to_check = receive_payment_test_data["credits_to_check"]

        table_xpath = "//h5[text()='Credits']/following::table[@class='table table-hover'][1]//tbody//tr"

        # Scroll and wait for table
        self.actions.scroll_to_the_element((By.XPATH, table_xpath))
        self.actions.wait_for_element((By.XPATH, table_xpath))

        expected_credits = {item["credits_no"] for item in credits_to_check}
        found_credits = []

        retries = 3
        while retries > 0:
            try:
                rows = self.driver.find_elements(By.XPATH, table_xpath)

                for row in rows:
                    credit_text = row.find_element(By.XPATH, ".//td[2]//a").get_attribute("textContent").strip()

                    for credit_data in credits_to_check:
                        expected_credit = credit_data["credits_no"]

                        # Match credit number
                        if expected_credit == credit_text and expected_credit not in found_credits:

                            # Select checkbox
                            checkbox = row.find_element(By.XPATH, "./td[1]//input[@type='checkbox']")
                            if not checkbox.is_selected():
                                checkbox.click()

                            # Enter amount
                            payment_input = row.find_element(By.XPATH, "./td[5]//input")
                            payment_input.clear()
                            payment_input.send_keys(credit_data["credits_payment_amount"])

                            print(f"Checked {expected_credit} and entered ₹{credit_data['credits_payment_amount']}")
                            found_credits.append(expected_credit)

                break

            except StaleElementReferenceException:
                print("Stale element encountered. Retrying...")
                retries -= 1
                time.sleep(1)

        missing_credits = expected_credits - set(found_credits)

        print(f"\nExpected Credits: {expected_credits}")
        print(f"Found Credits: {set(found_credits)}")

        assert not missing_credits, \
            f"Missing Credits in table: {missing_credits}"

        print("All expected credits found and processed successfully.")

    def rp_credits_check_and_enter_amount_sales_flow_latest(self,credit_list, receive_payment_test_data):
        # Normalize invoice_list into list of dicts
        if isinstance(credit_list, str):
            credit_list = [{
                "credits_no": credit_list,
                "credits_payment_amount": receive_payment_test_data.get(
                    "rp_payment_amt_credit_transaction", "0"
                )
            }]

        assert credit_list, "No credits provided to process in Receive Payment"

        table_xpath = "//h5[text()='Credits']/following::table[@class='table table-hover'][1]//tbody//tr"

        next_button_xpath = (
            "//h5[normalize-space()='Credits']"
            "/following::ul[contains(@class,'pagination')][1]"
            "//a[@aria-label='Go to next page' and @aria-disabled='false']"
        )

        self.actions.scroll_to_the_element((By.XPATH, table_xpath))
        found_credits = []
        expected_credits = [item["credits_no"] for item in credit_list]

        while True:
            retries = 3
            while retries > 0:
                try:
                    rows = self.driver.find_elements(By.XPATH, table_xpath)

                    for row in rows:
                        credit_text = row.find_element(
                            By.XPATH, ".//td[2]//a"
                        ).get_attribute("textContent").strip()

                        for credit_data in credit_list:
                            expected_credit = credit_data["credits_no"]


                            if expected_credit in credit_text and expected_credit not in found_credits:

                                checkbox = row.find_element(
                                    By.XPATH, "./td[1]//input[@type='checkbox']"
                                )
                                if not checkbox.is_selected():
                                    checkbox.click()

                                payment_input = row.find_element(By.XPATH, "./td[5]//input")
                                payment_input.clear()
                                payment_input.send_keys(credit_data["credits_payment_amount"])

                                print(
                                    f"✓ Checked {expected_credit} and entered ₹{credit_data['credits_payment_amount']}"
                                )

                                found_credits.append(expected_credit)

                    break  # Page processed successfully

                except StaleElementReferenceException:
                    print("Stale element encountered while processing credits, retrying...")
                    time.sleep(1)
                    retries -= 1

            # Stop if all credits found
            if set(found_credits) == set(expected_credits):
                break

            # Try next page
            try:
                next_button = self.driver.find_element(By.XPATH, next_button_xpath)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
                next_button.click()
                time.sleep(1.2)
            except Exception:
                break  # No more pages

        missing_credits = [c for c in expected_credits if c not in found_credits]

        if missing_credits:
            assert False, f"Missing credits in Credits table: {missing_credits}"

        print("All expected credits were found and processed successfully.")

    def rp_credits_check_and_enter_amount_new(self, receive_payment_test_data):
        credits_to_check = receive_payment_test_data["credits_to_check"]
        table_xpath = "//h5[text()='Credits']/following::table[@class='table table-hover'][1]//tbody//tr"
        self.actions.wait_for_element((By.XPATH, table_xpath))
        next_button_xpath = "//h5[normalize-space()='Credits']     /following::ul[contains(@class,'pagination')][1]     //a[@aria-label='Go to next page']"

        # Scroll to table
        self.actions.scroll_to_the_element((By.XPATH, table_xpath))
        self.actions.wait_for_element((By.XPATH, table_xpath))

        expected_credits = {i["credits_no"] for i in credits_to_check}
        found_credits = set()

        def process_table_rows():
            """Reads rows on the current page and selects matching credits."""
            rows = self.driver.find_elements(By.XPATH, table_xpath)
            new_found = 0

            for row in rows:
                try:
                    credits_text = row.find_element(By.XPATH, ".//td[2]//a").get_attribute("textContent").strip()
                except:
                    continue

                print(f"Found credit: {credits_text}")

                for credit_data in credits_to_check:
                    expected_credit = credit_data["credits_no"]

                    if expected_credit == credits_text and credits_text not in found_credits:
                        checkbox = row.find_element(By.XPATH, "./td[1]//input[@type='checkbox']")
                        if not checkbox.is_selected():
                            checkbox.click()

                        payment_input = row.find_element(By.XPATH, "./td[5]//input")
                        payment_input.clear()
                        payment_input.send_keys(credit_data["credits_payment_amount"])

                        found_credits.add(credits_text)
                        new_found += 1
                        print(f"Selected {expected_credit}, entered ₹{credit_data['credits_payment_amount']}")

            return new_found


        while True:
            process_table_rows()

            # Stop if all expected credits found
            if found_credits == expected_credits:
                print(" All credits found, stopping pagination.")
                break

            # Try finding NEXT button
            try:
                next_button = self.driver.find_element(By.XPATH, next_button_xpath)
            except NoSuchElementException:
                print("No NEXT button — reached last page of credits.")
                break

            # If NEXT button is disabled → stop
            parent_li = next_button.find_element(By.XPATH, "./..")
            if "disabled" in parent_li.get_attribute("class"):
                print("NEXT button disabled — no more pages.")
                break

            # Click NEXT
            print("➡ Clicking NEXT to load more credits...")
            self.driver.execute_script("arguments[0].click();", next_button)
            time.sleep(1.2)  # small wait to load next page

        print(f"\n Expected credits: {expected_credits}")
        print(f" Found credits: {found_credits}")

        assert expected_credits == found_credits, \
            f"Missing credits: {expected_credits - found_credits}"

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

