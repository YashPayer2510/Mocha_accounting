import logging
import re
import time
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from webdriver_manager.core import driver
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.conftest import expense_list_test_data
from datetime import datetime, timedelta
from actions.actions import Actions

STATUS_TYPE_RULES = {
    "unpaid": {
        "expected_types": ["Bill"],
        "valid_status_keywords": ["unpaid","partially paid", "overdue", "deposited"]
    },
    "paid": {
        "expected_types": ["Expense", "Check", "Credit Card Credit"],
        "valid_status_keywords": ["paid"]
    },
    "unapplied": {
        "expected_types": ["Vendor Credit"],
        "valid_status_keywords": ["unapplied"]
    },
    "applied": {
        "expected_types": ["Vendor Credit", "Bill Payment"],
        "valid_status_keywords": ["applied"]
    },
    "deposited": {
        "expected_types": ["Bill"],
        "valid_status_keywords": ["deposited"]
    },
    "overdue": {
        "expected_types": ["Bill"],
        "valid_status_keywords": ["partially paid", "overdue"]
    }

}

class ExpenseList:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 100)

    expense_list_expense_mod = (By.XPATH,"//img[@src='/svgs/expense.svg']")
    expense_list_expense_list_submod = (By.XPATH,"//a[normalize-space()='Expenses']")
    expense_list_type_dd = (By.XPATH,"//label[text()='Type']/following-sibling::select")
    expense_list_options_type = (By.XPATH,"//label[text()='Type']/following-sibling::select/option")
    expense_list_filter_btn = (By.XPATH,"//button[@id='zoom-primary-btn2']")
    expense_list_category_filter_dd = (By.XPATH,"//select[@name='category']")
    expense_list_options_categories_filter = (By.XPATH,"//select[@name='category']//option")
    expense_list_status_filter_dd = (By.XPATH,"//select[@name='status']")
    expense_list_options_status_filter = (By.XPATH,"//select[@name='status']//option")
    expense_list_payee_searchbaar_filter = (By.XPATH,"//select[@name='payee']")
    expense_list_search_options_payee = (By.XPATH, "//select[@name='payee']//option")
    expense_list_period_filter_dd = (By.XPATH,"//div[text()='Custom Date']/ancestor::div[contains(@class, 'css-hlgwow')]//input[contains(@id, 'react-select')]")
    expense_list_options_period_filter = (By.XPATH,"//div[contains(@class, 'option')]")
    expense_list_start_date_filter = (By.XPATH,"//input[@placeholder='Start date']")
    expense_list_end_date_filter = (By.XPATH,"//input[@placeholder='End date']")
    expense_list_current_month_date_filter = (By.CSS_SELECTOR, "div.ant-picker-header-view")
    expense_list_prev_btn_date_filter = (By.XPATH, "//div[@class='ant-picker-panel'][1]//div[@class= 'ant-picker-header']//button[@class= 'ant-picker-header-prev-btn'][1]")
    expense_list_nxt_btn_date_filter = (By.XPATH, "//div[@class='ant-picker-panel'][2]//div[@class= 'ant-picker-header']//button[@class= 'ant-picker-header-next-btn'][1]")
    expense_list_reset_filter_btn = (By.XPATH,"//button[@id='zoom-primary-cancel-btn']")
    expense_list_apply_filter_btn = (By.XPATH,"//button[@id='zoom-primary-btn float-end mb-3']")
    expense_list_close_filter_btn = (By.XPATH,"//div[@class='modal-header sc-kOHTFB ivaBOY']//button[@aria-label='Close']")
    expense_list_new_transaction_dd = (By.XPATH, "//button[normalize-space()='New Transaction']")
    expense_list_new_transaction_dd_expense = (By.XPATH, "//a[@class='dropdown-item sc-eDPEul inWBsQ'][normalize-space()='Expense']")
    expense_list_new_transaction_dd_bill = (By.XPATH, "//a[@class='dropdown-item sc-eDPEul inWBsQ'][normalize-space()='Bill']")
    expense_list_transaction_dd_check = (By.XPATH, "//a[@class='dropdown-item sc-eDPEul inWBsQ'][normalize-space()='Check']")
    expense_list_transaction_dd_purchase_order = (By.XPATH, "//a[@class='dropdown-item sc-eDPEul inWBsQ'][normalize-space()='Purchase Order']")
    expense_list_transaction_dd_vendor_credit = (By.XPATH, "//a[@class='dropdown-item sc-eDPEul inWBsQ'][normalize-space()='Vendor Credir']")
    expense_list_table_rows = (By.XPATH, "//table//tbody//tr")
    expense_list_table_date_column=(By.XPATH,"//table//tr//td[2]")
    expense_list_table_type_column = (By.XPATH, "//table//tr//td[3]")
    expense_list_table_transaction_no_column = (By.XPATH, "//table//tr//td[4]")
    expense_list_table_payee_column = (By.XPATH, "//table//tr//td[5]")
    expense_list_table_category_column = (By.XPATH, "//table//tr//td[6]")
    expense_list_table_balance_column = (By.XPATH, "//table//tr//td[7]")
    expense_list_table_total_column = (By.XPATH, "//table//tr//td[8]")
    expense_list_table_due_date_column = (By.XPATH, "//table//tr//td[9]")
    expense_list_table_status_column = (By.XPATH, "//table//tr//td[10]")
    expense_list_table_send_column = (By.XPATH, "//table//tr//td[11]")
    expense_list_table_actions_column = (By.XPATH, "//table//tr//td[12]")
    expense_list_next_btn = (By.XPATH, "//a[normalize-space()='>']")
    expense_list_page_dropdown = (By.XPATH, "//button[@id='pageDropDown']")
    expense_list_dd_option25 = (By.XPATH, "//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), '25')]")
    expense_list_page_dd_option30 = (By.XPATH, "//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), '30')]")
    expense_list_page_dd_option50 = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[2]/div/div[4]/div/div/div[2]/div[1]/span[1]/ul/li[4]/a")
    expense_list_pagination_count_text = (By.XPATH, "//span[@class='react-bootstrap-table-pagination-total']")

    def expense_list_expense_module(self):
        self.actions.wait_for_element(self.expense_list_expense_mod)
        self.actions.click(self.expense_list_expense_mod)

    def expense_list_expense_list_submodule(self):
        self.actions.wait_for_element(self.expense_list_expense_list_submod)
        self.actions.click(self.expense_list_expense_list_submod)

    def expense_list_filter_btn_submodule(self):
        self.actions.wait_for_element(self.expense_list_filter_btn)
        self.actions.click(self.expense_list_filter_btn)

    #  type filter
    def expense_verify_transaction_type_filter(self, expense_list_test_data):
        transaction_count = 0
        self.actions.wait_for_element(self.expense_list_type_dd)
        #self.actions.click(self.all_sales_type_dd)
        self.actions.dropdown_select(self.expense_list_type_dd, expense_list_test_data["transaction_info"]["transaction_type"])
        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
        self.actions.scroll_to_the_element(self.expense_list_page_dropdown)
        time.sleep(20)

        while True:
            # 3. Wait for type column to be present
            type_column_elements = self.driver.find_elements(*self.expense_list_table_type_column)

            for transaction_type in type_column_elements:
                transaction_type_text = transaction_type.text.strip().lower()
                expected_type = expense_list_test_data["transaction_info"]["transaction_type"].strip().lower()
                assert expected_type in transaction_type_text, f"Found other status: '{transaction_type.text}'"
                transaction_count += 1

            # 4. Handle pagination
            try:
                self.actions.scroll_to_the_element(self.expense_list_next_btn)
                next_btn = self.driver.find_element(*self.expense_list_next_btn)  # FIX: missing unpacking *
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
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
            EC.presence_of_element_located(self.expense_list_pagination_count_text)
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

    # select date range
    def select_date_range(self, expense_list_test_data):
        start_date_str = expense_list_test_data["transaction_info"]["start_date"]
        end_date_str = expense_list_test_data["transaction_info"]["end_date"]

        def parse_date(date_str):
            _, full_date_str = date_str.split(", ", 1)
            return datetime.strptime(full_date_str.strip(), "%B %d, %Y")

        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)

        # 1. Open calendar popup
        self.wait.until(EC.element_to_be_clickable(self.expense_list_start_date_filter)).click()
        time.sleep(1)

        for index, date_obj in enumerate([start_date, end_date]):
            target_month = date_obj.strftime("%b %Y")

            while True:
                visible_months = [
                    elem.text.strip().replace("\n", " ")
                    for elem in self.driver.find_elements(*self.expense_list_current_month_date_filter)
                ]

                if target_month in visible_months:
                    break
                elif datetime.strptime(visible_months[0], "%b %Y") > date_obj:
                    self.driver.find_element(*self.expense_list_prev_btn_date_filter).click()
                else:
                    self.driver.find_element(*self.expense_list_nxt_btn_date_filter).click()

                time.sleep(0.4)

            full_date = date_obj.strftime("%Y-%m-%d")
            dynamic_xpath = f"//td[@title='{full_date}']/div[contains(@class,'ant-picker-cell-inner')]"
            self.wait.until(EC.element_to_be_clickable((By.XPATH, dynamic_xpath))).click()
            time.sleep(0.4)

        # 4. Click apply
        self.wait.until(EC.element_to_be_clickable(self.expense_list_apply_filter_btn)).click()

    # verify the list according to selected date range
    def verify_expense_dates_within_range(self, expense_list_test_data):
        # Extract and parse start and end dates from JSON
        start_date_str = expense_list_test_data["transaction_info"]["start_date"].split(', ', 1)[1].strip()
        end_date_str = expense_list_test_data["transaction_info"]["end_date"].split(', ', 1)[1].strip()

        start_date = datetime.strptime(start_date_str, "%B %d, %Y")
        end_date = datetime.strptime(end_date_str, "%B %d, %Y")

        while True:
            # Always re-fetch after page change
            self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_date_column))
            date_elements = self.driver.find_elements(*self.expense_list_table_date_column)

            for date_elem in date_elements:
                date_text = date_elem.text.strip()
                if not date_text:
                    continue
                ui_date = datetime.strptime(date_text, "%d/%m/%Y")
                assert start_date <= ui_date <= end_date, f"Date {ui_date.strftime('%d/%m/%Y')} is out of range."

            try:
                self.actions.scroll_to_the_element(self.expense_list_next_btn)
                next_btn = self.driver.find_element(*self.expense_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()

                # Wait for page to update
                self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
                self.wait.until(EC.staleness_of(date_elements[0]))  # wait for old row to disappear

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"Pagination ended or button not found (possibly last page): {e}")
                break

    # unpaid status filter
    def expense_list_verify_transaction_unpaid_status_filter(self, expense_list_test_data):
        expected_status = expense_list_test_data["Status_Group"]["unpaid_status"].lower()
        expected_types = expense_list_test_data["Status_Group"]["unpaid_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.expense_list_status_filter_dd)
        self.actions.dropdown_contains(self.expense_list_status_filter_dd, self.expense_list_options_status_filter,expense_list_test_data["Status_Group"]["unpaid_status"])

        self.actions.click(self.expense_list_apply_filter_btn)

        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.expense_list_table_type_column)
            status_elements = self.driver.find_elements(*self.expense_list_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "unpaid":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "bill":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue",]), \
                            f"Unexpected status '{transaction_status}' for type 'Bill'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "applied", "unapplied"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.expense_list_next_btn)
                next_btn = self.driver.find_element(*self.expense_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {expense_list_test_data['Status_Group']['unpaid_status']}"
        print(f"✅ Verified {transaction_count} transactions for status: {expense_list_test_data['Status_Group']['unpaid_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.expense_list_pagination_count_text)
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

    # paid status filter
    def expense_list_verify_transaction_paid_status_filter(self, expense_list_test_data):
        expected_status = expense_list_test_data["Status_Group"]["paid_status"].lower()
        expected_types = expense_list_test_data["Status_Group"]["paid_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.expense_list_status_filter_dd)
        self.actions.dropdown_contains(self.expense_list_status_filter_dd, self.expense_list_options_status_filter,expense_list_test_data["Status_Group"]["paid_status"])

        self.actions.click(self.expense_list_apply_filter_btn)

        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.expense_list_table_type_column)
            status_elements = self.driver.find_elements(*self.expense_list_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "unpaid":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "bill":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue",]), \
                            f"Unexpected status '{transaction_status}' for type 'Bill'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "applied", "unapplied"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.expense_list_next_btn)
                next_btn = self.driver.find_element(*self.expense_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {expense_list_test_data['Status_Group']['paid_status']}"
        print(f"✅ Verified {transaction_count} transactions for status: {expense_list_test_data['Status_Group']['paid_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.expense_list_pagination_count_text)
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

    # partially-paid status filter
    def expense_list_verify_transaction_partially_paid_status_filter(self, expense_list_test_data):
        expected_status = expense_list_test_data["Status_Group"]["partially-paid_status"].lower()
        expected_types = expense_list_test_data["Status_Group"]["partially-paid_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.expense_list_status_filter_dd)
        self.actions.dropdown_contains(self.expense_list_status_filter_dd, self.expense_list_options_status_filter,expense_list_test_data["Status_Group"]["partially-paid_status"])

        self.actions.click(self.expense_list_apply_filter_btn)

        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.expense_list_table_type_column)
            status_elements = self.driver.find_elements(*self.expense_list_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "unpaid":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "bill":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue",]), \
                            f"Unexpected status '{transaction_status}' for type 'Bill'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "applied", "unapplied"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.expense_list_next_btn)
                next_btn = self.driver.find_element(*self.expense_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {expense_list_test_data['Status_Group']['partially-paid_status']}"
        print(f"✅ Verified {transaction_count} transactions for status: {expense_list_test_data['Status_Group']['partially-paid_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.expense_list_pagination_count_text)
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

    # deposited status filter
    def expense_list_verify_transaction_deposited_status_filter(self, expense_list_test_data):
        expected_status = expense_list_test_data["Status_Group"]["deposited_status"].lower()
        expected_types = expense_list_test_data["Status_Group"]["deposited_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.expense_list_status_filter_dd)
        self.actions.dropdown_contains(self.expense_list_status_filter_dd, self.expense_list_options_status_filter,expense_list_test_data["Status_Group"]["deposited_status"])

        self.actions.click(self.expense_list_apply_filter_btn)

        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.expense_list_table_type_column)
            status_elements = self.driver.find_elements(*self.expense_list_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "unpaid":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "bill":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue",]), \
                            f"Unexpected status '{transaction_status}' for type 'Bill'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "applied", "unapplied"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.expense_list_next_btn)
                next_btn = self.driver.find_element(*self.expense_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {expense_list_test_data['Status_Group']['deposited_status']}"
        print(f"✅ Verified {transaction_count} transactions for status: {expense_list_test_data['Status_Group']['deposited_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.expense_list_pagination_count_text)
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

    # applied status filter
    def expense_list_verify_transaction_applied_status_filter(self, expense_list_test_data):
        expected_status = expense_list_test_data["Status_Group"]["applied_status"].lower()
        expected_types = expense_list_test_data["Status_Group"]["applied_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.expense_list_status_filter_dd)
        self.actions.dropdown_contains(self.expense_list_status_filter_dd, self.expense_list_options_status_filter,expense_list_test_data["Status_Group"]["applied_status"])

        self.actions.click(self.expense_list_apply_filter_btn)

        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.expense_list_table_type_column)
            status_elements = self.driver.find_elements(*self.expense_list_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "unpaid":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "bill":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue",]), \
                            f"Unexpected status '{transaction_status}' for type 'Bill'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "applied", "unapplied"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.expense_list_next_btn)
                next_btn = self.driver.find_element(*self.expense_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {expense_list_test_data['Status_Group']['applied_status']}"
        print(f"✅ Verified {transaction_count} transactions for status: {expense_list_test_data['Status_Group']['applied_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.expense_list_pagination_count_text)
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

    # unapplied status filter
    def expense_list_verify_transaction_unapplied_status_filter(self, expense_list_test_data):
        expected_status = expense_list_test_data["Status_Group"]["unapplied_status"].lower()
        expected_types = expense_list_test_data["Status_Group"]["unapplied_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.expense_list_status_filter_dd)
        self.actions.dropdown_contains(self.expense_list_status_filter_dd, self.expense_list_options_status_filter,expense_list_test_data["Status_Group"]["unapplied_status"])

        self.actions.click(self.expense_list_apply_filter_btn)

        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.expense_list_table_type_column)
            status_elements = self.driver.find_elements(*self.expense_list_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "unpaid":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "bill":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue",]), \
                            f"Unexpected status '{transaction_status}' for type 'Bill'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "applied", "unapplied"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.expense_list_next_btn)
                next_btn = self.driver.find_element(*self.expense_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {expense_list_test_data['Status_Group']['unapplied_status']}"
        print(f"✅ Verified {transaction_count} transactions for status: {expense_list_test_data['Status_Group']['unapplied_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.expense_list_pagination_count_text)
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

    # overdue status filter
    def expense_list_verify_transaction_overdue_status_filter(self, expense_list_test_data):
        expected_status = expense_list_test_data["Status_Group"]["overdue_status"].lower()
        expected_types = expense_list_test_data["Status_Group"]["overdue_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.expense_list_status_filter_dd)
        self.actions.dropdown_contains(self.expense_list_status_filter_dd, self.expense_list_options_status_filter,
                                       expense_list_test_data["Status_Group"]["overdue_status"])

        self.actions.click(self.expense_list_apply_filter_btn)

        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.expense_list_table_type_column)
            status_elements = self.driver.find_elements(*self.expense_list_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "unpaid":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "bill":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue", ]), \
                            f"Unexpected status '{transaction_status}' for type 'Bill'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "applied", "unapplied"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.expense_list_next_btn)
                next_btn = self.driver.find_element(*self.expense_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {expense_list_test_data['Status_Group']['overdue_status']}"
        print(
            f"✅ Verified {transaction_count} transactions for status: {expense_list_test_data['Status_Group']['overdue_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.expense_list_pagination_count_text)
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

    # void status filter
    def expense_list_verify_transaction_void_status_filter(self, expense_list_test_data):
        expected_status = expense_list_test_data["Status_Group"]["void_status"].lower()
        expected_types = expense_list_test_data["Status_Group"]["void_expected_types"]  # List of transaction types expected for the selected status
        transaction_count = 0

        # Wait for status dropdown, click and select the status
        self.actions.wait_for_element(self.expense_list_status_filter_dd)
        self.actions.dropdown_contains(self.expense_list_status_filter_dd, self.expense_list_options_status_filter,
                                       expense_list_test_data["Status_Group"]["void_status"])

        self.actions.click(self.expense_list_apply_filter_btn)

        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
        time.sleep(2)

        while True:
            # Fetch all types and statuses for current page
            type_elements = self.driver.find_elements(*self.expense_list_table_type_column)
            status_elements = self.driver.find_elements(*self.expense_list_table_status_column)

            assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem in zip(type_elements, status_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()

                transaction_count += 1

                # --- Verification Logic ---
                if expected_status == "unpaid":
                    # Special condition for "Invoice" with open-related sub-statuses
                    if transaction_type.lower() == "bill":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue", ]), \
                            f"Unexpected status '{transaction_status}' for type 'Bill'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "applied", "unapplied"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f"❌ Unhandled status filter: {expected_status}")

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.expense_list_next_btn)
                next_btn = self.driver.find_element(*self.expense_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        assert transaction_count > 0, f"No transactions found for status: {expense_list_test_data['Status_Group']['void_status']}"
        print(
            f"✅ Verified {transaction_count} transactions for status: {expense_list_test_data['Status_Group']['void_status']}")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.expense_list_pagination_count_text)
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

    #  type and status filter
    def expense_list_verify_transaction_type_status_filter(self, expense_list_test_data):
        # Extract test data
        selected_status = expense_list_test_data["transaction_info"]["transaction_status"].lower()
        selected_type = expense_list_test_data["transaction_info"]["transaction_type"]

        # Validate the status exists in the rule map
        if selected_status not in STATUS_TYPE_RULES:
            raise AssertionError(f"❌ Unhandled status filter: {selected_status}")

        expected_types = STATUS_TYPE_RULES[selected_status]["expected_types"]
        valid_status_keywords = STATUS_TYPE_RULES[selected_status]["valid_status_keywords"]
        transaction_count = 0
        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
        time.sleep(2)

       # Select the transaction TYPE first
        self.actions.wait_for_element(self.expense_list_type_dd)
        self.actions.dropdown_select(self.expense_list_type_dd,selected_type)
        # Wait for list/table to refresh again
        time.sleep(4)
        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
        # click on filter button
        self.actions.wait_for_element(self.expense_list_filter_btn)
        self.actions.click(self.expense_list_filter_btn)
        # Now select the STATUS
        self.actions.wait_for_element(self.expense_list_status_filter_dd)
        self.actions.dropdown_equals(self.expense_list_status_filter_dd,self.expense_list_options_status_filter,expense_list_test_data["transaction_info"]["transaction_status"]
        )
        # click on apply button
        self.actions.click(self.expense_list_apply_filter_btn)
        # Wait for list/table to refresh again
        time.sleep(2)
        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
         # Optional: adjust delay if needed for table load

        # Loop through paginated table
        while True:
            type_elements = self.driver.find_elements(*self.expense_list_table_type_column)
            status_elements = self.driver.find_elements(*self.expense_list_table_status_column)

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
                self.actions.scroll_to_the_element(self.expense_list_next_btn)
                next_btn = self.driver.find_element(*self.expense_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                break
            except Exception as e:
                print(f"❌ Pagination error: {e}")
                break
        print(f"transaction count:{transaction_count}")
        # Final assertions
        assert transaction_count > 0, f"No transactions found for status: {selected_status}"
        print(f"✅ Verified {transaction_count} transactions for status '{selected_status}' and type '{selected_type}'")

        # Optional: match pagination count
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.expense_list_pagination_count_text)
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
    def expense_list_verify_transaction_type_status_customer_filter(self, expense_list_test_data):
        # Extract test data
        selected_status = expense_list_test_data["transaction_info"]["transaction_status"].lower()
        selected_type = expense_list_test_data["transaction_info"]["transaction_type"]
        selected_customer = expense_list_test_data["transaction_info"]["payee"]

        # Validate the status exists in the rule map
        if selected_status not in STATUS_TYPE_RULES:
            raise AssertionError(f"❌ Unhandled status filter: {selected_status}")

        expected_types = STATUS_TYPE_RULES[selected_status]["expected_types"]
        valid_status_keywords = STATUS_TYPE_RULES[selected_status]["valid_status_keywords"]
        transaction_count = 0

        #Select the transaction TYPE first
        self.actions.wait_for_element(self.expense_list_type_dd)
        self.actions.dropdown_select(self.expense_list_type_dd,selected_type)
        # Wait for list/table to refresh
        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
        time.sleep(4)

        #click on filter button
        self.actions.wait_for_element(self.expense_list_filter_btn)
        self.actions.click(self.expense_list_filter_btn)

         # Optional: adjust delay if needed for table load

        # STEP 3: Now select the STATUS
        self.actions.wait_for_element(self.expense_list_status_filter_dd)
        self.actions.dropdown_contains(
            self.expense_list_status_filter_dd,
            self.expense_list_options_status_filter,
            selected_status
        )
        # Now select the customer
        self.actions.wait_for_element(self.expense_list_payee_searchbaar_filter)
        #self.actions.send_keys(self.expense_list_payee_searchbaar_filter,selected_customer)
        self.actions.select_value_from_dropdown(self.expense_list_payee_searchbaar_filter,selected_customer)

        # click on apply button
        self.actions.click(self.expense_list_apply_filter_btn)
        # Wait for list/table to refresh again
        time.sleep(4)
        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))

        # Loop through paginated table
        while True:
            type_elements = self.driver.find_elements(*self.expense_list_table_type_column)
            status_elements = self.driver.find_elements(*self.expense_list_table_status_column)
            customer_elements = self.driver.find_elements(*self.expense_list_table_payee_column)

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
                self.actions.scroll_to_the_element(self.expense_list_next_btn)
                next_btn = self.driver.find_element(*self.expense_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
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
            EC.presence_of_element_located(self.expense_list_pagination_count_text)
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

    # Period selection
    def verify_date_range_dropdown_filter(self, expense_list_test_data):
        filter_value = expense_list_test_data["transaction_info"]["date_range"]
        transaction_count = 0
        if filter_value == "Custom Date":
            print("Skipping 'Custom Date' as per requirement.")
            return

        # Step 1: Calculate expected date range
        today = datetime.today().date()
        if filter_value == "Today":
            expected_start = expected_end = today
        elif filter_value == "Yesterday":
            expected_start = expected_end = today - timedelta(days=1)
        elif filter_value == "This Month":
            expected_start = today.replace(day=1)
            expected_end = today
        elif filter_value == "This Year":
            expected_start = today.replace(month=1, day=1)
            expected_end = today
        elif filter_value == "Last 30 Days":
            expected_start = today - timedelta(days=30)
            expected_end = today
        elif filter_value == "Last 60 Days":
            expected_start = today - timedelta(days=60)
            expected_end = today
        elif filter_value == "Last 90 Days":
            expected_start = today - timedelta(days=90)
            expected_end = today
        else:
            raise ValueError(f"Unsupported date filter: {filter_value}")

        # Step 2: Apply filter
        self.actions.wait_for_element(self.expense_list_filter_btn)
        self.actions.click(self.expense_list_filter_btn)
        self.actions.dropdown_equals(
            self.expense_list_period_filter_dd,
            self.expense_list_options_period_filter,
            filter_value
        )
        self.actions.click(self.expense_list_apply_filter_btn)
        time.sleep(4)  # Wait for results to load

        # Step 3: Collect ALL transactions across pagination
        all_transaction_dates = []

        while True:
            # Get dates from current page
            date_elements = self.driver.find_elements(*self.expense_list_table_date_column)
            for elem in date_elements:
                date_text = elem.text.strip()
                transaction_count += 1
                try:
                    parsed_date = datetime.strptime(date_text, "%d/%m/%Y").date()
                    all_transaction_dates.append(parsed_date)
                except ValueError:
                    print(f"Skipping unrecognized date: {date_text}")

            # Check for next page
            try:
                next_btn = self.driver.find_element(*self.expense_list_next_btn)
                if "disabled" in next_btn.get_attribute("class") or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.staleness_of(date_elements[0]))
                time.sleep(2)  # Wait for next page to load
            except NoSuchElementException:
                break

        # Step 4: Validate ALL dates at once
        invalid_dates = [
            date for date in all_transaction_dates
            if not (expected_start <= date <= expected_end)
        ]

        assert not invalid_dates, (
            f"❌ {len(invalid_dates)}/{len(all_transaction_dates)} transactions "
            f"are outside {expected_start} to {expected_end}: {invalid_dates}"
        )

        print(
            f"✅ All {len(all_transaction_dates)} transactions are within "
            f"range: {expected_start} to {expected_end}"
        )
        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.expense_list_pagination_count_text)
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

    #category filter
    def verify_category_dropdown_filter(self, expense_list_test_data):
        category_selected = expense_list_test_data["transaction_info"]["category"].strip().lower()
        transaction_count = 0
        self.actions.wait_for_element(self.expense_list_filter_btn)
        self.actions.click(self.expense_list_filter_btn)
        self.actions.dropdown_contains(self.expense_list_category_filter_dd,self.expense_list_options_categories_filter,category_selected)
        self.actions.click(self.expense_list_apply_filter_btn)
        time.sleep(4)
        self.actions.wait_for_element(self.expense_list_table_rows)
        while True:
            # Wait for type column to be present
            category_column_elements = self.driver.find_elements(*self.expense_list_table_category_column)

            for category in category_column_elements:
                category_text = category.text.strip().lower()
                assert category_selected in category_text, f"Found other status: '{category_text.text}'"
                transaction_count += 1

           # Handles Paginations
            try:
                    self.actions.scroll_to_the_element(self.expense_list_next_btn)
                    next_btn = self.driver.find_element(*self.expense_list_next_btn)  # FIX: missing unpacking *
                    class_attr = next_btn.get_attribute("class") or ""

                    if "disabled" in class_attr or not next_btn.is_enabled():
                        break

                    next_btn.click()
                    self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
                    self.wait.until(EC.staleness_of(category_column_elements[0]))

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
                EC.presence_of_element_located(self.expense_list_pagination_count_text)
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
            print(f"Transaction count after filter:{transaction_count}")
            print(f"Transaction count displayed:{total_count}")
            return total_count


    def expense_list_verify_transaction_category_type_status_customer_date_range_filter(self, expense_list_test_data):
        # Extract test data
        selected_status = expense_list_test_data["transaction_info"]["transaction_status"].lower()
        selected_type = expense_list_test_data["transaction_info"]["transaction_type"]
        selected_customer = expense_list_test_data["transaction_info"]["payee"]
        selected_category = expense_list_test_data["transaction_info"]["category"].strip().lower()
        selected_date_range = expense_list_test_data["transaction_info"]["date_range"]

        # Validate the status exists in the rule map
        if selected_status not in STATUS_TYPE_RULES:
            raise AssertionError(f"❌ Unhandled status filter: {selected_status}")

        expected_types = STATUS_TYPE_RULES[selected_status]["expected_types"]
        valid_status_keywords = STATUS_TYPE_RULES[selected_status]["valid_status_keywords"]
        transaction_count = 0

        if selected_date_range == "Custom Date":
            print("Skipping 'Custom Date' as per requirement.")
            return

        # Step 1: Calculate expected date range
        today = datetime.today().date()
        if selected_date_range == "Today":
            expected_start = expected_end = today
        elif selected_date_range == "Yesterday":
            expected_start = expected_end = today - timedelta(days=1)
        elif selected_date_range == "This Month":
            expected_start = today.replace(day=1)
            expected_end = today
        elif selected_date_range == "This Year":
            expected_start = today.replace(month=1, day=1)
            expected_end = today
        elif selected_date_range == "Last 30 Days":
            expected_start = today - timedelta(days=30)
            expected_end = today
        elif selected_date_range == "Last 60 Days":
            expected_start = today - timedelta(days=60)
            expected_end = today
        elif selected_date_range == "Last 90 Days":
            expected_start = today - timedelta(days=90)
            expected_end = today
        else:
            raise ValueError(f"Unsupported date filter: {selected_date_range}")
        #Select the transaction TYPE first
        self.actions.wait_for_element(self.expense_list_type_dd)
        self.actions.dropdown_select(self.expense_list_type_dd,selected_type)
        # Wait for list/table to refresh
        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
        time.sleep(4)

        #click on filter button
        self.actions.wait_for_element(self.expense_list_filter_btn)
        self.actions.click(self.expense_list_filter_btn)
        # select catgeory
        self.actions.wait_for_element(self.expense_list_category_filter_dd)
        self.actions.dropdown_contains(self.expense_list_category_filter_dd, self.expense_list_options_categories_filter,selected_category)
        time.sleep(2)
        # Now select the STATUS
        self.actions.wait_for_element(self.expense_list_status_filter_dd)
        self.actions.dropdown_contains(self.expense_list_status_filter_dd,self.expense_list_options_status_filter,selected_status)
        time.sleep(2)
        # Now select the customer
        self.actions.wait_for_element(self.expense_list_payee_searchbaar_filter)
        #self.actions.send_keys(self.expense_list_payee_searchbaar_filter,selected_customer)
        self.actions.dropdown_contains(self.expense_list_payee_searchbaar_filter,self.expense_list_search_options_payee,selected_customer)
        # Now select the date range
        self.actions.wait_for_element(self.expense_list_period_filter_dd)
        self.actions.dropdown_contains(self.expense_list_period_filter_dd, self.expense_list_options_period_filter,selected_date_range)
        time.sleep(2)
        # click on apply button
        self.actions.click(self.expense_list_apply_filter_btn)
        # Wait for list/table to refresh again
        time.sleep(4)
        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))

        all_transaction_dates = []
        # Loop through paginated table
        while True:
            type_elements = self.driver.find_elements(*self.expense_list_table_type_column)
            status_elements = self.driver.find_elements(*self.expense_list_table_status_column)
            customer_elements = self.driver.find_elements(*self.expense_list_table_payee_column)
            category_elements = self.driver.find_elements(*self.expense_list_table_category_column)
            date_elements = self.driver.find_elements(*self.expense_list_table_date_column)

            assert len(type_elements) == len(status_elements), "Mismatch in type/status cell count"

            for t_elem, s_elem, c_elem, categ_elem, dt_elem in zip(type_elements, status_elements, customer_elements, category_elements, date_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()
                transaction_customer = c_elem.text.strip()
                transaction_category = categ_elem.text.strip().lower()
                transaction_date_range = dt_elem.text.strip()
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

                # E)Validate category in category column
                assert selected_category.lower() in transaction_category.lower(), (
                    f"Category mismatch: expected '{selected_category}' to be in '{transaction_category}'")
                # F)Validate date range in date column
                try:
                    parsed_date = datetime.strptime(transaction_date_range, "%d/%m/%Y").date()
                    all_transaction_dates.append(parsed_date)
                except ValueError:
                    print(f"Skipping unrecognized date: {transaction_date_range}")

            # Go to next page if possible
            try:
                self.actions.scroll_to_the_element(self.expense_list_next_btn)
                next_btn = self.driver.find_element(*self.expense_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                break
            except Exception as e:
                print(f"❌ Pagination error: {e}")
                break

        # Final assertions
        assert transaction_count > 0, f"No transactions found for status: {selected_status}"
        print(f"✅ Verified {transaction_count} transactions for status '{selected_status}', type '{selected_type}', date range '{selected_date_range}' and customer'{selected_customer}'")

        # Step 4: Validate ALL dates at once
        invalid_dates = [
            date for date in all_transaction_dates
            if not (expected_start <= date <= expected_end)
        ]

        assert not invalid_dates, (
            f"❌ {len(invalid_dates)}/{len(all_transaction_dates)} transactions "
            f"are outside {expected_start} to {expected_end}: {invalid_dates}"
        )

        print(
            f"✅ All {len(all_transaction_dates)} transactions are within "
            f"range: {expected_start} to {expected_end}"
        )
        # Optional: match pagination count
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.expense_list_pagination_count_text)
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


    def expense_list_verify_transaction_category_type_status_customer_selecte_date_range_filter(self, expense_list_test_data):
        # Extract test data
        selected_status = expense_list_test_data["transaction_info"]["transaction_status"].lower()
        selected_type = expense_list_test_data["transaction_info"]["transaction_type"]
        selected_customer = expense_list_test_data["transaction_info"]["payee"]
        selected_category = expense_list_test_data["transaction_info"]["category"].strip().lower()
        selected_start_date = expense_list_test_data["transaction_info"]["start_date"]
        selected_end_date_str = expense_list_test_data["transaction_info"]["end_date"]


        # Validate the status exists in the rule map
        if selected_status not in STATUS_TYPE_RULES:
            raise AssertionError(f"❌ Unhandled status filter: {selected_status}")

        expected_types = STATUS_TYPE_RULES[selected_status]["expected_types"]
        valid_status_keywords = STATUS_TYPE_RULES[selected_status]["valid_status_keywords"]
        transaction_count = 0
        # Select the transaction TYPE first
        self.actions.wait_for_element(self.expense_list_type_dd)
        self.actions.dropdown_select(self.expense_list_type_dd, selected_type)
        # Wait for list/table to refresh
        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
        time.sleep(4)

        # click on filter button
        self.actions.wait_for_element(self.expense_list_filter_btn)
        self.actions.click(self.expense_list_filter_btn)
        # select catgeory
        self.actions.wait_for_element(self.expense_list_category_filter_dd)
        self.actions.dropdown_contains(self.expense_list_category_filter_dd,
                                       self.expense_list_options_categories_filter, selected_category)
        time.sleep(2)
        # Now select the STATUS
        self.actions.wait_for_element(self.expense_list_status_filter_dd)
        self.actions.dropdown_contains(self.expense_list_status_filter_dd, self.expense_list_options_status_filter,
                                       selected_status)
        time.sleep(2)
        # Now select the customer
        self.actions.wait_for_element(self.expense_list_payee_searchbaar_filter)
        # self.actions.send_keys(self.expense_list_payee_searchbaar_filter,selected_customer)
        self.actions.dropdown_contains(self.expense_list_payee_searchbaar_filter,
                                       self.expense_list_search_options_payee, selected_customer)

        def parse_date(date_str):
            _, full_date_str = date_str.split(", ", 1)
            return datetime.strptime(full_date_str.strip(), "%B %d, %Y")

        start_date = parse_date(selected_start_date)
        end_date = parse_date(selected_end_date_str)

        # 1. Open calendar popup
        self.wait.until(EC.element_to_be_clickable(self.expense_list_start_date_filter)).click()
        time.sleep(1)

        for index, date_obj in enumerate([start_date, end_date]):
            target_month = date_obj.strftime("%b %Y")

            while True:
                visible_months = [
                    elem.text.strip().replace("\n", " ")
                    for elem in self.driver.find_elements(*self.expense_list_current_month_date_filter)
                ]

                if target_month in visible_months:
                    break
                elif datetime.strptime(visible_months[0], "%b %Y") > date_obj:
                    self.driver.find_element(*self.expense_list_prev_btn_date_filter).click()
                else:
                    self.driver.find_element(*self.expense_list_nxt_btn_date_filter).click()

                time.sleep(0.4)

            full_date = date_obj.strftime("%Y-%m-%d")
            dynamic_xpath = f"//td[@title='{full_date}']/div[contains(@class,'ant-picker-cell-inner')]"
            self.wait.until(EC.element_to_be_clickable((By.XPATH, dynamic_xpath))).click()
        time.sleep(2)
        # click on apply button
        self.actions.click(self.expense_list_apply_filter_btn)
        # Wait for list/table to refresh again
        time.sleep(4)
        self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))

        all_transaction_dates = []
        #start_date = datetime.strptime(selected_start_date, "%B %d, %Y")
        #end_date = datetime.strptime(selected_end_date_str, "%B %d, %Y")

        # Loop through paginated table
        while True:
            type_elements = self.driver.find_elements(*self.expense_list_table_type_column)
            status_elements = self.driver.find_elements(*self.expense_list_table_status_column)
            customer_elements = self.driver.find_elements(*self.expense_list_table_payee_column)
            category_elements = self.driver.find_elements(*self.expense_list_table_category_column)
            date_elements = self.driver.find_elements(*self.expense_list_table_date_column)

            assert len(type_elements) == len(status_elements), "Mismatch in type/status cell count"

            for t_elem, s_elem, c_elem, categ_elem, dt_elem in zip(type_elements, status_elements, customer_elements, category_elements, date_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()
                transaction_customer = c_elem.text.strip()
                transaction_category = categ_elem.text.strip().lower()
                transaction_date_range = dt_elem.text.strip()
                transaction_count += 1

                # A) Validate date range with selected dates
                if not transaction_date_range:
                    continue
                ui_date = datetime.strptime(transaction_date_range, "%d/%m/%Y")
                assert start_date <= ui_date <= end_date, f"Date {ui_date.strftime('%d/%m/%Y')} is out of range."

                # B) Validate type is the one we selected
                assert transaction_type.lower() == selected_type.lower(), (
                    f"❌ Type mismatch: expected '{selected_type}', got '{transaction_type}'"
                )

                # C) Type must be valid for this status
                assert transaction_type in expected_types, (
                    f"❌ Unexpected type '{transaction_type}' for status '{selected_status}'"
                )

                # D) Status must contain at least one expected keyword
                assert any(keyword in transaction_status for keyword in valid_status_keywords), (
                    f"❌ Invalid status '{transaction_status}' for type '{transaction_type}' and status '{selected_status}'"
                )

                # E)Validate customer in customer column
                assert transaction_customer.lower() == selected_customer.lower(), (
                    f"❌ Type mismatch: expected '{selected_customer}', got '{transaction_customer}'")

                # F)Validate category in category column
                assert selected_category.lower() in transaction_category.lower(), (
                    f"Category mismatch: expected '{selected_category}' to be in '{transaction_category}'")

            # Go to next page if possible
            try:
                self.actions.scroll_to_the_element(self.expense_list_next_btn)
                next_btn = self.driver.find_element(*self.expense_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.expense_list_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                break
            except Exception as e:
                print(f"❌ Pagination error: {e}")
                break
        # Final assertions
        assert transaction_count > 0, f"No transactions found for status: {selected_status}"
        print(
            f"✅ Verified {transaction_count} transactions for status '{selected_status}', type '{selected_type}', date range '{selected_start_date}to {selected_end_date_str}' and customer'{selected_customer}'")

        # Optional: match pagination count
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.expense_list_pagination_count_text)
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









