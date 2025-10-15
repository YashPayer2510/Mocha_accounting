import re
import time

from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.actions import Actions

STATUS_TYPE_RULES = {
    "open": {
        "expected_types": ["Invoice", "Deposit", "Journal Entry", "Credit Card Credit"],
        "valid_status_keywords": ["due in", "partially paid", "overdue", "open", "deposit"]
    },
    "closed": {
        "expected_types": ["Payment", "Deposit", "Journal Entry"],
        "valid_status_keywords": ["closed"]
    },
    "paid": {
        "expected_types": ["Sales Receipt", "Refund Receipt", "Expense/Check", "Credit Card Credit"],
        "valid_status_keywords": ["paid"]
    },
    "unapplied": {
        "expected_types": ["Credit Memo"],
        "valid_status_keywords": ["unapplied"]
    },
    "applied": {
        "expected_types": ["Credit Memo"],
        "valid_status_keywords": ["applied"]
    },
    "deposited": {
        "expected_types": ["Invoice"],
        "valid_status_keywords": ["deposited"]
    },
    "overdue": {
        "expected_types": ["Invoice"],
        "valid_status_keywords": ["partially paid", "overdue"]
    },
}



class AllSales:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 100)

    all_sales_sales_mod = (By.XPATH,"//img[@src='/svgs/sales.svg']")
    all_sales_all_sales_sub_mod = (By.XPATH,"//a[normalize-space()='All Sales']")
    all_sales_type_dd =(By.XPATH,"//div[@style='display: flex; gap: 10px; flex-direction: column;'][1]//select")
    all_sales_options_type_dd = (By.XPATH,"//label[text()='Type']/following-sibling::select/option")
    all_sales_status_dd = (By.XPATH,"//div[@style='display: flex; gap: 10px; flex-direction: column;'][2]//select")
    all_sales_options_status_dd = (By.XPATH,"//div[@style='display: flex; gap: 10px; flex-direction: column;'][2]//select//option")
    all_sales_search_customer=(By.XPATH,"//input[@name='searchBar' or @label='Customer']")
    all_sales_search_options_customer = (By.XPATH,"//div[@class= 'dropdown-item']")
    all_sales_new_transaction_dd = (By.XPATH,"//button[normalize-space()='New Transaction']")
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
    all_sales_page_dd_option50 = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[2]/div/div[4]/div/div/div[2]/div[1]/span[1]/ul/li[4]/a")
    all_sales_pagination_count_text = (By.XPATH,"//span[@class='react-bootstrap-table-pagination-total']")


    def all_sales_list_sales_module(self):
        self.actions.wait_for_element(self.all_sales_sales_mod)
        self.actions.click(self.all_sales_sales_mod)

    def all_sales_list_all_sales_submodule(self):
        self.actions.wait_for_element(self.all_sales_all_sales_sub_mod)
        self.actions.click(self.all_sales_all_sales_sub_mod)

    # type filter
    def all_sales_verify_transaction_type_filter(self, all_sales_test_data):
        transaction_count = 0
        self.actions.wait_for_element(self.all_sales_type_dd)
        #self.actions.click(self.all_sales_type_dd)
        self.actions.dropdown_contains(self.all_sales_type_dd,self.all_sales_options_type_dd,all_sales_test_data["transaction_info"]["transaction_type"])
        self.actions.scroll_to_the_element(self.all_sales_page_dropdown)
        time.sleep(20)

        while True:
            # 3. Wait for type column to be present
            type_column_elements = self.driver.find_elements(*self.all_sales_table_type_column)

            for transaction_type in type_column_elements:
                transaction_type_text = transaction_type.text.strip().lower()
                expected_type = all_sales_test_data["transaction_info"]["transaction_type"].strip().lower()
                assert expected_type in transaction_type_text, f"Found other status: '{transaction_type.text}'"
                transaction_count += 1

            # 4. Handle pagination
            try:
                self.actions.scroll_to_the_element(self.all_sales_next_btn)
                next_btn = self.driver.find_element(*self.all_sales_next_btn)  # FIX: missing unpacking *
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
                self.wait.until(EC.staleness_of(type_column_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"Pagination ended or button not found (possibly last page): {e}")
                break


        assert transaction_count > 0, "No selected transaction found!"
        print(f"✅ Total selected transaction Entries: {transaction_count}.")
        print(f"✅ All visible statuses contain {transaction_count}.")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.all_sales_pagination_count_text)
        )
        pagination_text = pagination_text_element.text.strip()

        # Extract the last number using regex
        match = re.search(r"of\s+(\d+)", pagination_text)
        if match:
            total_count = int(match.group(1))
            print(f"✅ Total rows in pagination: {total_count}")
        else:
            raise AssertionError("❌ Could not extract total row count from pagination text.")

        # Compare extracted total count with counted overdue entries
        assert total_count == transaction_count, f"❌ Mismatch: Filtered transaction count = {transaction_count}, but pagination shows = {total_count}"
        return total_count

    # open status filter
    def all_sales_verify_transaction_open_status_filter(self, all_sales_test_data):
        expected_status = all_sales_test_data["Status_Group"]["open_status"].lower()
        expected_types = all_sales_test_data["Status_Group"]["open_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.all_sales_status_dd)
        self.actions.dropdown_contains(self.all_sales_status_dd, self.all_sales_options_status_dd,all_sales_test_data["Status_Group"]["open_status"])


        self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.all_sales_table_type_column)
            status_elements = self.driver.find_elements(*self.all_sales_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "open":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "invoice":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue",]), \
                            f"Unexpected status '{transaction_status}' for type 'Invoice'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "closed", "applied", "unapplied"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.all_sales_next_btn)
                next_btn = self.driver.find_element(*self.all_sales_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {all_sales_test_data['Status_Group']['open_status']}"
        print(f"✅ Verified {transaction_count} transactions for status: {all_sales_test_data['Status_Group']['open_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.all_sales_pagination_count_text)
        )
        pagination_text = pagination_text_element.text.strip()

        # Extract the last number using regex
        match = re.search(r"of\s+(\d+)", pagination_text)
        if match:
            total_count = int(match.group(1))
            print(f"✅ Total rows in pagination: {total_count}")
        else:
            raise AssertionError("❌ Could not extract total row count from pagination text.")

        # Compare extracted total count with counted overdue entries
        assert total_count == transaction_count, f"❌ Mismatch: Filtered transaction count = {transaction_count}, but pagination shows = {total_count}"
        return total_count

    # closed status filter
    def all_sales_verify_transaction_closed_status_filter(self, all_sales_test_data):
        expected_status = all_sales_test_data["Status_Group"]["closed_status"].lower()
        expected_types = all_sales_test_data["Status_Group"]["closed_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.all_sales_status_dd)
        self.actions.dropdown_contains(self.all_sales_status_dd, self.all_sales_options_status_dd,all_sales_test_data["Status_Group"]["closed_status"])


        self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.all_sales_table_type_column)
            status_elements = self.driver.find_elements(*self.all_sales_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "open":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "invoice":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue"]), \
                            f"Unexpected status '{transaction_status}' for type 'Invoice'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "closed", "applied", "unapplied"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.all_sales_next_btn)
                next_btn = self.driver.find_element(*self.all_sales_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {all_sales_test_data['Status_Group']['closed_status']}"
        print(f"✅ Verified {transaction_count} transactions for status: {all_sales_test_data['Status_Group']['closed_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.all_sales_pagination_count_text)
        )
        pagination_text = pagination_text_element.text.strip()

        # Extract the last number using regex
        match = re.search(r"of\s+(\d+)", pagination_text)
        if match:
            total_count = int(match.group(1))
            print(f"✅ Total rows in pagination: {transaction_count}")
            print(f"✅ Total rows in pagination: {total_count}")
        else:
            raise AssertionError("❌ Could not extract total row count from pagination text.")

        # Compare extracted total count with counted overdue entries
        assert total_count == transaction_count, f"❌ Mismatch: Filtered transaction count = {transaction_count}, but pagination shows = {total_count}"

    # paid status filter
    def all_sales_verify_transaction_paid_status_filter(self, all_sales_test_data):
        expected_status = all_sales_test_data["Status_Group"]["paid_status"].lower()
        expected_types = all_sales_test_data["Status_Group"]["paid_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.all_sales_status_dd)
        self.actions.dropdown_contains(self.all_sales_status_dd, self.all_sales_options_status_dd,all_sales_test_data["Status_Group"]["paid_status"])


        self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.all_sales_table_type_column)
            status_elements = self.driver.find_elements(*self.all_sales_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "open":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "invoice":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue"]), \
                            f"Unexpected status '{transaction_status}' for type 'Invoice'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "closed", "applied", "unapplied", "deposited"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.all_sales_next_btn)
                next_btn = self.driver.find_element(*self.all_sales_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except StaleElementReferenceException:
                print("✅ Pagination element went stale — assumed end of pagination.")
                break


            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {all_sales_test_data['Status_Group']['paid_status']}"
        print(f"✅ Verified {transaction_count} transactions for status: {all_sales_test_data['Status_Group']['paid_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.all_sales_pagination_count_text)
        )
        pagination_text = pagination_text_element.text.strip()

        # Extract the last number using regex
        match = re.search(r"of\s+(\d+)", pagination_text)
        if match:
            total_count = int(match.group(1))
            print(f"✅ Total transactions: {transaction_count}")
            print(f"✅ Total rows in pagination: {total_count}")
        else:
            raise AssertionError("❌ Could not extract total row count from pagination text.")

        # Compare extracted total count with counted overdue entries
        assert total_count == transaction_count, f"❌ Mismatch: Filtered transaction count = {transaction_count}, but pagination shows = {total_count}"
        return total_count

    # deposited status filter
    def all_sales_verify_transaction_deposited_status_filter(self, all_sales_test_data):
        expected_status = all_sales_test_data["Status_Group"]["deposited_status"].lower()
        expected_types = all_sales_test_data["Status_Group"]["deposited_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.all_sales_status_dd)
        self.actions.dropdown_contains(self.all_sales_status_dd, self.all_sales_options_status_dd,all_sales_test_data["Status_Group"]["deposited_status"])


        self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.all_sales_table_type_column)
            status_elements = self.driver.find_elements(*self.all_sales_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "open":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "invoice":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue"]), \
                            f"Unexpected status '{transaction_status}' for type 'Invoice'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "closed", "applied", "unapplied","deposited"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.all_sales_next_btn)
                next_btn = self.driver.find_element(*self.all_sales_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except StaleElementReferenceException:
                print("✅ Pagination element went stale — assumed end of pagination.")
                break


            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {all_sales_test_data['Status_Group']['deposited_status']}"
        print(f"✅ Verified {transaction_count} transactions for status: {all_sales_test_data['Status_Group']['deposited_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.all_sales_pagination_count_text)
        )
        pagination_text = pagination_text_element.text.strip()

        # Extract the last number using regex
        match = re.search(r"of\s+(\d+)", pagination_text)
        if match:
            total_count = int(match.group(1))
            print(f"✅ Total transactions: {transaction_count}")
            print(f"✅ Total rows in pagination: {total_count}")
        else:
            raise AssertionError("❌ Could not extract total row count from pagination text.")

        # Compare extracted total count with counted overdue entries
        assert total_count == transaction_count, f"❌ Mismatch: Filtered transaction count = {transaction_count}, but pagination shows = {total_count}"
        return total_count

    # applied status filter
    def all_sales_verify_transaction_applied_status_filter(self, all_sales_test_data):
        expected_status = all_sales_test_data["Status_Group"]["applied_status"].lower()
        expected_types = all_sales_test_data["Status_Group"]["applied_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.all_sales_status_dd)
        self.actions.dropdown_contains(self.all_sales_status_dd, self.all_sales_options_status_dd,all_sales_test_data["Status_Group"]["applied_status"])


        self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.all_sales_table_type_column)
            status_elements = self.driver.find_elements(*self.all_sales_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "open":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "invoice":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue"]), \
                            f"Unexpected status '{transaction_status}' for type 'Invoice'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "closed", "applied", "unapplied","deposited"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.all_sales_next_btn)
                next_btn = self.driver.find_element(*self.all_sales_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except StaleElementReferenceException:
                print("✅ Pagination element went stale — assumed end of pagination.")
                break


            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {all_sales_test_data['Status_Group']['applied_status']}"
        print(f"✅ Verified {transaction_count} transactions for status: {all_sales_test_data['Status_Group']['applied_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.all_sales_pagination_count_text)
        )
        pagination_text = pagination_text_element.text.strip()

        # Extract the last number using regex
        match = re.search(r"of\s+(\d+)", pagination_text)
        if match:
            total_count = int(match.group(1))
            print(f"✅ Total transactions: {transaction_count}")
            print(f"✅ Total rows in pagination: {total_count}")
        else:
            raise AssertionError("❌ Could not extract total row count from pagination text.")

        # Compare extracted total count with counted overdue entries
        assert total_count == transaction_count, f"❌ Mismatch: Filtered transaction count = {transaction_count}, but pagination shows = {total_count}"

    # unapplied status filter
    def all_sales_verify_transaction_unapplied_status_filter(self, all_sales_test_data):
        expected_status = all_sales_test_data["Status_Group"]["unapplied_status"].lower()
        expected_types = all_sales_test_data["Status_Group"]["unapplied_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.all_sales_status_dd)
        self.actions.dropdown_contains(self.all_sales_status_dd, self.all_sales_options_status_dd,all_sales_test_data["Status_Group"]["unapplied_status"])


        self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.all_sales_table_type_column)
            status_elements = self.driver.find_elements(*self.all_sales_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "open":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "invoice":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue"]), \
                            f"Unexpected status '{transaction_status}' for type 'Invoice'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "closed", "applied", "unapplied","deposited"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.all_sales_next_btn)
                next_btn = self.driver.find_element(*self.all_sales_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except StaleElementReferenceException:
                print("✅ Pagination element went stale — assumed end of pagination.")
                break


            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {all_sales_test_data['Status_Group']['unapplied_status']}"
        print(f"✅ Verified {transaction_count} transactions for status: {all_sales_test_data['Status_Group']['unapplied_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.all_sales_pagination_count_text)
        )
        pagination_text = pagination_text_element.text.strip()

        # Extract the last number using regex
        match = re.search(r"of\s+(\d+)", pagination_text)
        if match:
            total_count = int(match.group(1))
            print(f"✅ Total transactions: {transaction_count}")
            print(f"✅ Total rows in pagination: {total_count}")
        else:
            raise AssertionError("❌ Could not extract total row count from pagination text.")

        # Compare extracted total count with counted overdue entries
        assert total_count == transaction_count, f"❌ Mismatch: Filtered transaction count = {transaction_count}, but pagination shows = {total_count}"

    # partially paid status filter
    def all_sales_verify_transaction_partially_paid_status_filter(self, all_sales_test_data):
        expected_status = all_sales_test_data["Status_Group"]["partially-paid_status"].lower()
        expected_types = all_sales_test_data["Status_Group"]["partially-paid_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.all_sales_status_dd)
        self.actions.dropdown_contains(self.all_sales_status_dd, self.all_sales_options_status_dd,all_sales_test_data["Status_Group"]["partially-paid_status"])


        self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.all_sales_table_type_column)
            status_elements = self.driver.find_elements(*self.all_sales_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "open":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "invoice":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue"]), \
                            f"Unexpected status '{transaction_status}' for type 'Invoice'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "closed", "applied", "unapplied","deposited", "partially paid"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.all_sales_next_btn)
                next_btn = self.driver.find_element(*self.all_sales_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except StaleElementReferenceException:
                print("✅ Pagination element went stale — assumed end of pagination.")
                break


            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {all_sales_test_data['Status_Group']['partially-paid_status']}"
        print(f"✅ Verified {transaction_count} transactions for status: {all_sales_test_data['Status_Group']['partially-paid_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.all_sales_pagination_count_text)
        )
        pagination_text = pagination_text_element.text.strip()

        # Extract the last number using regex
        match = re.search(r"of\s+(\d+)", pagination_text)
        if match:
            total_count = int(match.group(1))
            print(f"✅ Total transactions: {transaction_count}")
            print(f"✅ Total rows in pagination: {total_count}")
        else:
            raise AssertionError("❌ Could not extract total row count from pagination text.")

        # Compare extracted total count with counted overdue entries
        assert total_count == transaction_count, f"❌ Mismatch: Filtered transaction count = {transaction_count}, but pagination shows = {total_count}"

    # overdue status filter
    def all_sales_verify_transaction_overdue_status_filter(self, all_sales_test_data):
        expected_status = all_sales_test_data["Status_Group"]["overdue_status"].lower()
        expected_types = all_sales_test_data["Status_Group"]["overdue_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.all_sales_status_dd)
        self.actions.dropdown_contains(self.all_sales_status_dd, self.all_sales_options_status_dd,all_sales_test_data["Status_Group"]["overdue_status"])


        self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.all_sales_table_type_column)
            status_elements = self.driver.find_elements(*self.all_sales_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "open":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "invoice":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue"]), \
                            f"Unexpected status '{transaction_status}' for type 'Invoice'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "closed", "applied", "unapplied","deposited", "overdue"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.all_sales_next_btn)
                next_btn = self.driver.find_element(*self.all_sales_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except StaleElementReferenceException:
                print("✅ Pagination element went stale — assumed end of pagination.")
                break


            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {all_sales_test_data['Status_Group']['overdue_status']}"
        print(f"✅ Verified {transaction_count} transactions for status: {all_sales_test_data['Status_Group']['overdue_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.all_sales_pagination_count_text)
        )
        pagination_text = pagination_text_element.text.strip()

        # Extract the last number using regex
        match = re.search(r"of\s+(\d+)", pagination_text)
        if match:
            total_count = int(match.group(1))
            print(f"✅ Total transactions: {transaction_count}")
            print(f"✅ Total rows in pagination: {total_count}")
        else:
            raise AssertionError("❌ Could not extract total row count from pagination text.")

        # Compare extracted total count with counted overdue entries
        assert total_count == transaction_count, f"❌ Mismatch: Filtered transaction count = {transaction_count}, but pagination shows = {total_count}"
        return total_count

    # void status filter
    def all_sales_verify_transaction_void_status_filter(self, all_sales_test_data):
        expected_status = all_sales_test_data["Status_Group"]["void_status"].lower()
        expected_types = all_sales_test_data["Status_Group"]["void_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.all_sales_status_dd)
        self.actions.dropdown_contains(self.all_sales_status_dd, self.all_sales_options_status_dd,all_sales_test_data["Status_Group"]["void_status"])


        self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.all_sales_table_type_column)
            status_elements = self.driver.find_elements(*self.all_sales_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "open":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "invoice":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue"]), \
                            f"Unexpected status '{transaction_status}' for type 'Invoice'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "closed", "applied", "unapplied","deposited","overdue","void"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.all_sales_next_btn)
                next_btn = self.driver.find_element(*self.all_sales_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except StaleElementReferenceException:
                print("✅ Pagination element went stale — assumed end of pagination.")
                break


            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {all_sales_test_data['Status_Group']['void_status']}"
        print(f"✅ Verified {transaction_count} transactions for status: {all_sales_test_data['Status_Group']['void_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.all_sales_pagination_count_text)
        )
        pagination_text = pagination_text_element.text.strip()

        # Extract the last number using regex
        match = re.search(r"of\s+(\d+)", pagination_text)
        if match:
            total_count = int(match.group(1))
            print(f"✅ Total transactions: {transaction_count}")
            print(f"✅ Total rows in pagination: {total_count}")
        else:
            raise AssertionError("❌ Could not extract total row count from pagination text.")

        # Compare extracted total count with counted overdue entries
        assert total_count == transaction_count, f"❌ Mismatch: Filtered transaction count = {transaction_count}, but pagination shows = {total_count}"

    #  type and status filter
    def all_sales_verify_transaction_type_status_filter(self, all_sales_test_data):
        # Extract test data
        selected_status = all_sales_test_data["transaction_info"]["transaction_status"].lower()
        selected_type = all_sales_test_data["transaction_info"]["transaction_type"]

        # Validate the status exists in the rule map
        if selected_status not in STATUS_TYPE_RULES:
            raise AssertionError(f"❌ Unhandled status filter: {selected_status}")

        expected_types = STATUS_TYPE_RULES[selected_status]["expected_types"]
        valid_status_keywords = STATUS_TYPE_RULES[selected_status]["valid_status_keywords"]
        transaction_count = 0

        # STEP 1: Select the transaction TYPE first
        self.actions.wait_for_element(self.all_sales_type_dd)
        self.actions.dropdown_contains(self.all_sales_type_dd,self.all_sales_options_type_dd,selected_type)

        # STEP 2: Wait for list/table to refresh
        self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
        time.sleep(2)  # Optional: adjust delay if needed for table load

        # STEP 3: Now select the STATUS
        self.actions.wait_for_element(self.all_sales_status_dd)
        self.actions.dropdown_contains(
            self.all_sales_status_dd,
            self.all_sales_options_status_dd,
            all_sales_test_data["transaction_info"]["transaction_status"]
        )

        # STEP 4: Wait for list/table to refresh again
        self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
        time.sleep(2)  # Optional: adjust delay if needed for table load

        # STEP 5: Loop through paginated table
        while True:
            type_elements = self.driver.find_elements(*self.all_sales_table_type_column)
            status_elements = self.driver.find_elements(*self.all_sales_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch in type/status cell count"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()
                transaction_count += 1

                # A) Validate type is the one we selected
                assert transaction_type.lower() == selected_type.lower(), (
                    f"❌ Type mismatch: expected '{selected_type}', got '{transaction_type}'"
                )

                # B) Type must be valid for this status
                assert transaction_type in expected_types, (
                    f"❌ Unexpected type '{transaction_type}' for status '{selected_status}'"
                )

                # C) Status must contain at least one expected keyword
                assert any(keyword in transaction_status for keyword in valid_status_keywords), (
                    f"❌ Invalid status '{transaction_status}' for type '{transaction_type}' and status '{selected_status}'"
                )

            # Go to next page if possible
            try:
                self.actions.scroll_to_the_element(self.all_sales_next_btn)
                next_btn = self.driver.find_element(*self.all_sales_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                break
            except Exception as e:
                print(f"❌ Pagination error: {e}")
                break

        # Final assertions
        assert transaction_count > 0, f"No transactions found for status: {selected_status}"
        print(f"✅ Verified {transaction_count} transactions for status '{selected_status}' and type '{selected_type}'")

        # Optional: match pagination count
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.all_sales_pagination_count_text)
        )
        pagination_text = pagination_text_element.text.strip()
        match = re.search(r"of\s+(\d+)", pagination_text)
        if not match:
            raise AssertionError("❌ Couldn't extract row count from pagination text")
        total_count = int(match.group(1))
        assert total_count == transaction_count, (
            f"❌ Count mismatch: table rows = {transaction_count}, pagination = {total_count}"
        )
        print(f"✅ Pagination matches: {total_count} rows")

    # type, status and customer filter
    def all_sales_verify_transaction_type_status_customer_filter(self, all_sales_test_data):
        # Extract test data
        selected_status = all_sales_test_data["transaction_info"]["transaction_status"].lower()
        selected_type = all_sales_test_data["transaction_info"]["transaction_type"]
        selected_customer = all_sales_test_data["transaction_info"]["customer"]

        # Validate the status exists in the rule map
        if selected_status not in STATUS_TYPE_RULES:
            raise AssertionError(f"❌ Unhandled status filter: {selected_status}")

        expected_types = STATUS_TYPE_RULES[selected_status]["expected_types"]
        valid_status_keywords = STATUS_TYPE_RULES[selected_status]["valid_status_keywords"]
        transaction_count = 0

        # STEP 1: Select the transaction TYPE first
        self.actions.wait_for_element(self.all_sales_type_dd)
        self.actions.dropdown_contains(
            self.all_sales_type_dd,
            self.all_sales_options_type_dd,
            selected_type
        )

        # STEP 2: Wait for list/table to refresh
        self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
        time.sleep(2)  # Optional: adjust delay if needed for table load

        # STEP 3: Now select the STATUS
        self.actions.wait_for_element(self.all_sales_status_dd)
        self.actions.dropdown_contains(
            self.all_sales_status_dd,
            self.all_sales_options_status_dd,
            selected_status
        )

        self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
        time.sleep(2)  # Optional: adjust delay if needed for table load

        # STEP 4: Now select the customer
        self.actions.wait_for_element(self.all_sales_status_dd)
        self.actions.dropdown_contains(
            self.all_sales_search_customer,
            self.all_sales_search_options_customer,
            selected_customer
        )

        # STEP 5: Wait for list/table to refresh again
        self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
        time.sleep(2)  # Optional: adjust delay if needed for table load

        # STEP 6: Loop through paginated table
        while True:
            type_elements = self.driver.find_elements(*self.all_sales_table_type_column)
            status_elements = self.driver.find_elements(*self.all_sales_table_status_column)
            customer_elements = self.driver.find_elements(*self.all_sales_table_customer_name_column)

            assert len(type_elements) == len(status_elements), "Mismatch in type/status cell count"

            for t_elem, s_elem, c_elem in zip(type_elements, status_elements, customer_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()
                transaction_customer = c_elem.text.strip()
                transaction_count += 1

                # A) Validate type is the one we selected
                assert transaction_type.lower() == selected_type.lower(), (
                    f"❌ Type mismatch: expected '{selected_type}', got '{transaction_type}'"
                )

                # B) Type must be valid for this status
                assert transaction_type in expected_types, (
                    f"❌ Unexpected type '{transaction_type}' for status '{selected_status}'"
                )

                # C) Status must contain at least one expected keyword
                assert any(keyword in transaction_status for keyword in valid_status_keywords), (
                    f"❌ Invalid status '{transaction_status}' for type '{transaction_type}' and status '{selected_status}'"
                )

                # D)Validate customer in customer column
                assert transaction_customer.lower() == selected_customer.lower(), (
                    f"❌ Type mismatch: expected '{selected_customer}', got '{transaction_customer}'")

            # Go to next page if possible
            try:
                self.actions.scroll_to_the_element(self.all_sales_next_btn)
                next_btn = self.driver.find_element(*self.all_sales_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.all_sales_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                break
            except Exception as e:
                print(f"❌ Pagination error: {e}")
                break

        # Final assertions
        assert transaction_count > 0, f"No transactions found for status: {selected_status}"
        print(f"✅ Verified {transaction_count} transactions for status '{selected_status}', type '{selected_type}' and customer'{selected_customer}'")

        # Optional: match pagination count
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.all_sales_pagination_count_text)
        )
        pagination_text = pagination_text_element.text.strip()
        match = re.search(r"of\s+(\d+)", pagination_text)
        if not match:
            raise AssertionError("❌ Couldn't extract row count from pagination text")
        total_count = int(match.group(1))
        assert total_count == transaction_count, (
            f"❌ Count mismatch: table rows = {transaction_count}, pagination = {total_count}"
        )
        print(f"✅ Pagination matches: {total_count} rows")
