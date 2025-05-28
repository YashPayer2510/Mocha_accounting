import logging
import re
import time

import pytest
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.actions import Actions



class InvoicesList:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 10)

    invoice_list_sales_mod = (By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
    invoice_list_invoices_submod = (By.XPATH,"//*[@id='root']/div/div[1]/div[1]/ul/div/div[1]/div[2]/div/div/div/div/li[3]/ul/li[2]/a")
    invoice_list_overdue_amount = (By.XPATH,"//div[@class='container-fluid']//div[1]//div[1]//div[1]//h5[1]//span[1]")
    invoice_list_not_due_yet_amount = (By.XPATH,"//div[@class='container-fluid']//div[1]//div[1]//div[2]//h5[1]//span[1]")
    invoice_list_not_deposited_amount = (By.XPATH,"//div[@class='body flex-grow-1 px-3 mb-5']//div[2]//div[1]//div[1]//h5[1]//span[1]")
    invoice_list_deposited_amount = (By.XPATH,"//div[@class='body flex-grow-1 px-3 mb-5']//div[2]//div[1]//div[2]//h5[1]//span[1]")
    invoice_list_search_bar = (By.XPATH,"//input[@placeholder='Search Invoices']")
    invoice_list_create_invoice = (By.XPATH,"")
    invoice_list_table_rows =(By.XPATH,"//table//tr")
    invoice_list_table_recurring_column=(By.XPATH,"//table//tr//td[1]")
    invoice_list_table_date_column = (By.XPATH, "//table//tr//td[2]")
    invoice_list_table_invoice_no_column = (By.XPATH, "//table//tr//td[3]")
    invoice_list_table_name_column = (By.XPATH, "//table//tr//td[4]")
    invoice_list_table_total_amount_column = (By.XPATH, "//table//tr//td[5]")
    invoice_list_table_paid_amount_column = (By.XPATH, "//table//tr//td[6]")
    invoice_list_table_balance_column = (By.XPATH, "//table//tr//td[7]")
    invoice_list_table_due_date_column = (By.XPATH, "//table//tr//td[8]")
    invoice_list_table_status_column = (By.XPATH, "//table//tr//td[9]")
    invoice_list_table_term_column = (By.XPATH, "//table//tr//td[10]")
    invoice_list_table_send_column = (By.XPATH, "//table//tr//td[11]")
    invoice_list_table_actions_column = (By.XPATH, "//table//tr//td[12]")
    invoice_list_pagination_nxt_btn = (By.XPATH,"//a[normalize-space()='>>']")
    invoice_list_status = (By.XPATH,"//button[normalize-space()='Status']")
    invoice_list_options_status = (By.XPATH,"//ul[contains(@class, 'dropdown')]/li/a")
    invoice_list_options_status_overdue = (By.XPATH,"//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), 'Over Due')]")
    invoice_list_options_status_not_due_yet= (By.XPATH,"//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), 'Not Due Yet')]")
    invoice_list_options_status_not_deposited = (By.XPATH,"//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), 'Not Deposited')]")
    invoice_list_options_status_deposit = (By.XPATH,"//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), 'Deposited')]")
    invoice_list_next_btn=(By.XPATH,"//a[normalize-space()='>']")
    invoice_list_page_dropdown = (By.XPATH,"//button[@id='pageDropDown']")
    invoice_list_page_dd_option25 = (By.XPATH,"//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), '25')]")
    invoice_list_page_dd_option30 = (By.XPATH, "//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), '30')]")
    invoice_list_page_dd_option50 = (By.XPATH, "//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), '50')]")
    invoice_list_pagination_count_text = (By.XPATH,"//span[@class='react-bootstrap-table-pagination-total']")


    def inv_list_sales_module(self):
        self.actions.wait_for_element(self.invoice_list_sales_mod)
        self.actions.click(self.invoice_list_sales_mod)

    def inv_list_invoice_submodule(self):
        self.actions.wait_for_element(self.invoice_list_invoices_submod)
        self.actions.click(self.invoice_list_invoices_submod)

    def inv_list_overdue_amt(self):
        self.actions.wait_for_element(self.invoice_list_overdue_amount)
        self.actions.scroll_to_the_element(self.invoice_list_overdue_amount)
        overdue_text = self.actions.get_text(self.invoice_list_overdue_amount)
        print(f"Overdue amount text: {overdue_text}")

        # Remove ₹ symbol, commas, and convert to float
        try:
            cleaned = overdue_text.replace("₹", "").replace(",", "").strip()
            return float(cleaned)
        except ValueError:
            print("Failed to parse overdue amount")
            return 0.0


    def inv_list_not_due_yet_amt(self):
        self.actions.wait_for_element(self.invoice_list_not_due_yet_amount)
        self.actions.scroll_to_the_element(self.invoice_list_not_due_yet_amount)
        not_due_yet_text = self.actions.get_text(self.invoice_list_not_due_yet_amount)
        print(f"Not due yet amount text: {not_due_yet_text}")

        # Remove ₹ symbol, commas, and convert to float
        try:
            cleaned = not_due_yet_text.replace("₹", "").replace(",", "").strip()
            return float(cleaned)
        except ValueError:
            print("Failed to parse not due yet amount")
            return 0.0


    def inv_list_deposited_amt(self):
        self.actions.wait_for_element(self.invoice_list_deposited_amount)
        self.actions.scroll_to_the_element(self.invoice_list_deposited_amount)
        deposited_text = self.actions.get_text(self.invoice_list_deposited_amount)
        print(f"deposited amount text: {deposited_text}")

        # Remove ₹ symbol, commas, and convert to float
        try:
            cleaned = deposited_text.replace("₹", "").replace(",", "").strip()
            return float(cleaned)
        except ValueError:
            print("Failed to parse deposited amount")
            return 0.0

    def inv_list_not_deposited_amt(self):
        self.actions.wait_for_element(self.invoice_list_not_deposited_amount)
        self.actions.scroll_to_the_element(self.invoice_list_not_deposited_amount)
        not_deposited_text = self.actions.get_text(self.invoice_list_not_deposited_amount)
        print(f"Not deposited amount text: {not_deposited_text}")

        # Remove ₹ symbol, commas, and convert to float
        try:
            cleaned = not_deposited_text.replace("₹", "").replace(",", "").strip()
            return float(cleaned)
        except ValueError:
            print("Failed to parse deposited amount")
            return 0.0

    def inv_list_verify_overdue_amount(self):
        total_overdue_balance = 0.0
        page_count=1
        while True:
            # wait for rows to be present
            self.wait.until(EC.presence_of_all_elements_located(self.invoice_list_table_rows))

            # fetch status & balance cells
            statuses = self.driver.find_elements(*self.invoice_list_table_status_column)
            balances = self.driver.find_elements(*self.invoice_list_table_balance_column)

            for status_el, balance_el in zip(statuses, balances):
                if "Overdue" in status_el.text:
                    raw = balance_el.text
                    try:
                        # parse ₹ and commas, convert to float
                        amt = float(raw.replace("₹", "").replace(",", "").strip())
                        total_overdue_balance += amt
                    except ValueError:
                        # skip bad data
                        continue

            # handle pagination
            try:
                next_btn = self.driver.find_element(*self.invoice_list_next_btn)
                if "disabled" in (next_btn.get_attribute("class") or ""):
                    break
                next_btn.click()
                page_count += 1
                print(f"Navigated to page {page_count}")
                time.sleep(2)
                self.wait.until(EC.staleness_of(balances[0]))  # Wait for table to refresh
            except NoSuchElementException:
                break  # No next button means end of pages
            except Exception as e:
                print(f"Unexpected error while paginating: {e}")
                break

        print(f"Total Overdue Balance: ₹{total_overdue_balance:.2f}")
        overdue = self.inv_list_overdue_amt()
        assert abs(total_overdue_balance -  overdue), "Mismatch amount"

    def inv_list_verify_not_due_yet_amount(self):
        total_not_due_yet_balance = 0.0
        page_count = 1

        while True:
            # wait for rows to be present
            self.wait.until(EC.presence_of_all_elements_located(self.invoice_list_table_rows))

            # fetch status & balance cells
            statuses = self.driver.find_elements(*self.invoice_list_table_status_column)
            balances = self.driver.find_elements(*self.invoice_list_table_balance_column)

            for status_el, balance_el in zip(statuses, balances):
                if "Due" in status_el.text:
                    raw = balance_el.text
                    try:
                        # parse ₹ and commas, convert to float
                        amt = float(raw.replace("₹", "").replace(",", "").strip())
                        total_not_due_yet_balance += amt
                    except ValueError:
                        # skip bad data
                        continue

            # handle pagination
            try:
                next_btn = self.driver.find_element(*self.invoice_list_next_btn)
                if "disabled" in (next_btn.get_attribute("class") or ""):
                    break
                next_btn.click()
                page_count += 1
                print(f"Navigated to page {page_count}")
                time.sleep(4)
                self.wait.until(EC.staleness_of(balances[0]))  # Wait for table to refresh
            except NoSuchElementException:
                break  # No next button means end of pages

            except Exception as e:
                print(f"Unexpected error while paginating: {e}")
                break

        print(f"Total Not due yet Balance: ₹{total_not_due_yet_balance:.2f}")
        not_due_yet = self.inv_list_not_due_yet_amt()

        assert abs(total_not_due_yet_balance - not_due_yet) < 0.01, \
            f"Mismatch amount: Calculated ₹{total_not_due_yet_balance:.2f}, Expected ₹{not_due_yet:.2f}"

    def inv_list_verify_not_deposited_amount(self):
        total_not_deposited_balance = 0.0
        page_count= 1

        while True:
            # wait for rows to be present
            self.wait.until(EC.presence_of_all_elements_located(self.invoice_list_table_rows))

            # fetch status & balance cells
            statuses = self.driver.find_elements(*self.invoice_list_table_status_column)
            balances = self.driver.find_elements(*self.invoice_list_table_balance_column)

            for status_el, balance_el in zip(statuses, balances):
                if "Due" in status_el.text or "Overdue" in status_el.text:
                    raw = balance_el.text
                    try:
                        # parse ₹ and commas, convert to float
                        amt = float(raw.replace("₹", "").replace(",", "").strip())
                        total_not_deposited_balance += amt
                    except ValueError:
                        # skip bad data
                        continue

            # handle pagination
            try:
                next_btn = self.driver.find_element(*self.invoice_list_next_btn)
                if "disabled" in (next_btn.get_attribute("class") or ""):
                    break
                next_btn.click()
                page_count += 1
                print(f"Navigated to page {page_count}")
                time.sleep(2)
                self.wait.until(EC.staleness_of(balances[0]))
            except NoSuchElementException:
                break  # No next button means end of pages
            except Exception as e:
                print(f"Unexpected error while paginating: {e}")
                break

        print(f"Total Not Deposited Balance (calculated): ₹{total_not_deposited_balance:.2f}")

        # Get displayed total and convert to float
        not_deposited = self.inv_list_not_deposited_amt()

        # Final assertion
        assert abs(total_not_deposited_balance - not_deposited) < 0.01, \
            f"Mismatch amount: Calculated ₹{total_not_deposited_balance:.2f}, Expected ₹{not_deposited:.2f}"

    def inv_list_verify_deposited_amount(self):
        total_deposited_balance = 0.0
        page_count =1

        while True:
            # wait for rows to be present
            self.wait.until(EC.presence_of_all_elements_located(self.invoice_list_table_rows))

            # fetch status & balance cells
            statuses = self.driver.find_elements(*self.invoice_list_table_status_column)
            paid = self.driver.find_elements(*self.invoice_list_table_paid_amount_column)

            for status_el, paid_el in zip(statuses, paid):
                    if "Deposited" in status_el.text:
                        raw = paid_el.text
                        try:
                            # parse ₹ and commas, convert to float
                            amt = float(raw.replace("₹", "").replace(",", "").strip())
                            total_deposited_balance += amt
                        except ValueError:
                            # skip bad data
                            continue

            # handle pagination
            try:
                next_btn = self.driver.find_element(*self.invoice_list_next_btn)
                if "disabled" in (next_btn.get_attribute("class") or ""):
                    break
                next_btn.click()
                next_btn.click()
                page_count += 1
                print(f"Navigated to page {page_count}")
                time.sleep(2)
                time.sleep(5)
                self.wait.until(EC.staleness_of(paid[0]))  # Wait for table to refresh
            except NoSuchElementException:
                break  # No next button means end of pages

            except Exception as e:
                print(f"Unexpected error while paginating: {e}")
                break

        print(f"Total Deposited Balance: ₹{total_deposited_balance:.2f}")
        deposited = self.inv_list_deposited_amt()
        print(f"Total Deposited Balance: ₹{deposited:.2f}")
        assert total_deposited_balance == deposited, f"Mismatch amount: Calculated ₹{total_deposited_balance:.2f}, Expected ₹{deposited:.2f}"


    def inv_list_verify_deposited2_amount(self):
        total_deposited_balance = 0.0

        while True:
            # wait for rows to be present
            self.wait.until(EC.presence_of_all_elements_located(self.invoice_list_table_rows))

            # fetch paid amount cells
            paid = self.driver.find_elements(*self.invoice_list_table_paid_amount_column)

            for element in paid:
                raw = element.text
                try:
                    # parse ₹ and commas, convert to float
                    amt = float(raw.replace("₹", "").replace(",", "").strip())
                    total_deposited_balance += amt
                except ValueError:
                    # skip bad data
                    continue

            # handle pagination
            try:
                next_btn = self.driver.find_element(*self.invoice_list_next_btn)
                if "disabled" in (next_btn.get_attribute("class") or ""):
                    break
                next_btn.click()
                self.wait.until(EC.staleness_of(paid[0]))  # Wait for table to refresh
            except NoSuchElementException:
                break  # No next button means end of pages
            except Exception as e:
                print(f"Unexpected error while paginating: {e}")
                break

        print(f"Total Deposited Balance (calculated): ₹{total_deposited_balance:.2f}")

        # Compare with expected value from UI
        deposited = self.inv_list_deposited_amt()  # This should return a float
        print(f"Deposited amount from UI: ₹{deposited:.2f}")

        # Assert with tolerance (due to float rounding issues)
        assert abs(total_deposited_balance - deposited) < 0.01, "Mismatch in deposited amount"

    def inv_list_verify_overdue_filter(self):
        overdue_count = 0

        # 1. Click on the Status dropdown
        status_dropdown = self.wait.until(EC.element_to_be_clickable(self.invoice_list_status))
        status_dropdown.click()

        # 2. Select 'Over Due'
        overdue_option = self.wait.until(EC.element_to_be_clickable(self.invoice_list_options_status_overdue))
        overdue_option.click()

        self.wait.until(EC.presence_of_all_elements_located(self.invoice_list_table_rows))
        time.sleep(10)
        while True:
            # 3. Wait for status column to be present
            status_column_elements = self.driver.find_elements(*self.invoice_list_table_status_column)

            for status in status_column_elements:
                status_text = status.text.strip().lower()
                assert "overdue" in status_text, f"Found other status: '{status.text}'"
                overdue_count += 1

            # 4. Handle pagination
            try:
                next_btn = self.driver.find_element(*self.invoice_list_next_btn)  # FIX: missing unpacking *
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.staleness_of(status_column_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error while paginating: {e}")
                break


        assert overdue_count > 0, "No Overdue entries found!"
        print(f"✅ Total Overdue Entries: {overdue_count}")
        print("✅ All visible statuses contain 'Overdue'.")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.invoice_list_pagination_count_text)
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
        assert total_count == overdue_count, f"❌ Mismatch: Overdue count = {overdue_count}, but pagination shows = {total_count}"



    def inv_list_verify_not_due_yet_filter(self):
        not_due_yet_count = 0

        # 1. Click on the Status dropdown
        status_dropdown = self.wait.until(EC.element_to_be_clickable(self.invoice_list_status))
        status_dropdown.click()

        # 2. Select 'Not Due yet'
        not_due_yet_option = self.wait.until(EC.element_to_be_clickable(self.invoice_list_options_status_not_due_yet))
        not_due_yet_option.click()

        self.wait.until(EC.presence_of_all_elements_located(self.invoice_list_table_rows))
        time.sleep(10)
        while True:
            # 3. Wait for status column to be present
            status_column_elements = self.driver.find_elements(*self.invoice_list_table_status_column)

            for status in status_column_elements:
                status_text = status.text.strip().lower()
                assert "Due" in status_text, f"Found other status: '{status.text}'"
                not_due_yet_count += 1

            # 4. Handle pagination
            try:
                next_btn = self.driver.find_element(*self.invoice_list_next_btn)  # FIX: missing unpacking *
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.staleness_of(status_column_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error while paginating: {e}")
                break


        assert not_due_yet_count > 0, "No not due yet entries found!"
        print(f"✅ Total not due yet Entries: {not_due_yet_count}")
        print("✅ All visible statuses contain 'not due yet count.")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.invoice_list_pagination_count_text)
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
        assert total_count == not_due_yet_count, f"❌ Mismatch: not due yet count = {not_due_yet_count}, but pagination shows = {total_count}"


    def inv_list_verify_not_deposited_filter(self):
        not_deposited_count = 0

        # 1. Click on the Status dropdown
        status_dropdown = self.wait.until(EC.element_to_be_clickable(self.invoice_list_status))
        status_dropdown.click()

        # 2. Select 'Not Deposited'
        not_deposited_option = self.wait.until(EC.element_to_be_clickable(self.invoice_list_options_status_not_deposited))
        not_deposited_option.click()

        self.wait.until(EC.presence_of_all_elements_located(self.invoice_list_table_rows))
        time.sleep(10)
        while True:
            # 3. Wait for status column to be present
            status_column_elements = self.driver.find_elements(*self.invoice_list_table_status_column)

            for status in status_column_elements:
                status_text = status.text.strip().lower()
                assert ("overdue" in status_text or "Due" in status_text), f"Found other status: '{status.text}'"
                not_deposited_count += 1

            # 4. Handle pagination
            try:
                next_btn = self.driver.find_element(*self.invoice_list_next_btn)  # FIX: missing unpacking *
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.staleness_of(status_column_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error while paginating: {e}")
                break


        assert not_deposited_count > 0, "No Not Deposited entries found!"
        print(f"✅ Total Not Deposited Entries: {not_deposited_count}")
        print("✅ All visible statuses contain not deposited count.")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.invoice_list_pagination_count_text)
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
        assert total_count == not_deposited_count, f"❌ Mismatch: Not Deposited count = {not_deposited_count}, but pagination shows = {total_count}"

    def inv_list_verify_deposited_filter(self):
        deposited_count = 0

        # 1. Click on the Status dropdown
        status_dropdown = self.wait.until(EC.element_to_be_clickable(self.invoice_list_status))
        status_dropdown.click()

        # 2. Select 'Deposited'
        not_deposited_option = self.wait.until(EC.element_to_be_clickable(self.invoice_list_options_status_deposit))
        not_deposited_option.click()

        self.wait.until(EC.presence_of_all_elements_located(self.invoice_list_table_rows))
        time.sleep(10)
        while True:
            # 3. Wait for status column to be present
            status_column_elements = self.driver.find_elements(*self.invoice_list_table_status_column)

            for status in status_column_elements:
                status_text = status.text.strip().lower()
                assert "Deposited" in status_text, f"Found other status: '{status.text}'"
                deposited_count += 1

            # 4. Handle pagination
            try:
                next_btn = self.driver.find_element(*self.invoice_list_next_btn)  # FIX: missing unpacking *
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.staleness_of(status_column_elements[0]))

            except NoSuchElementException:
                print("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error while paginating: {e}")
                break


        assert deposited_count > 0, "No Deposited entries found!"
        print(f"✅ Total Deposited Entries: {deposited_count}")
        print("✅ All visible statuses contain deposited count.")

        # Wait for the pagination text to be visible
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.invoice_list_pagination_count_text)
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
        assert total_count == deposited_count, f"❌ Mismatch:Deposited count = {deposited_count}, but pagination shows = {total_count}"

