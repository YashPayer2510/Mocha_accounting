import logging
import re
import time


import pytest
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.actions import Actions
from pages.all_sales_page import AllSales
from tests.conftest import all_sales_test_data
from tests.conftest import customer_list_test_data
from tests.conftest import customer_transaction_list_test_data


logger = logging.getLogger(__name__)
class CustomerList:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 100)
        self.all_sales = AllSales(driver)

    cust_list_sales_mod = (By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
    cust_list_customer_sub_mod = (By.XPATH, "//a[normalize-space()='Customers']")
    cust_list_card_total_sale_count = (By.XPATH,"//div[@class='row customersOverviewTour']//p[text()='Total Sales']/preceding-sibling::h5")
    cust_list_card_overdue_count = (By.XPATH, "//div[@class='row customersOverviewTour']//p[text()='Overdue']/preceding-sibling::h5")
    cust_list_card_open_invoice_count = (By.XPATH, "//div[@class='row customersOverviewTour']//p[text()='Open Invoices']/preceding-sibling::h5")
    cust_list_card_paid_invoice_count = (By.XPATH, "//div[@class='row customersOverviewTour']//p[text()='Paid Invoices']/preceding-sibling::h5")
    cust_list_customer_table_row = (By.XPATH,"//table//tbody//tr")
    cust_list_customer_name_column = (By.XPATH,"//table//tbody//tr//td[1]")
    cust_list_customer_contact_column = (By.XPATH,"//table//tbody//tr//td[2]")
    cust_list_customer_email_column = (By.XPATH,"//table//tbody//tr//td[3]")
    cust_list_customer_open_balance_column = (By.XPATH, "//table//tbody//tr//td[4]")
    cust_list_actions_icons_column = (By.XPATH,"//table//tbody//tr//td[5]")
    cust_list_edit_icons = (By.XPATH,"//tbody/tr/td[5]/div[1]/button[1]//*[name()='svg']")
    cust_list_next_btn = (By.XPATH, "//a[normalize-space()='>']")
    cust_list_page_dropdown = (By.XPATH, "//button[@id='pageDropDown']")
    cust_list_page_dd_option25 = (By.XPATH, "//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), '25')]")
    cust_list_page_dd_option30 = (By.XPATH, "//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), '30')]")
    cust_list_page_dd_option50 = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[2]/div/div[4]/div/div/div[2]/div[1]/span[1]/ul/li[4]/a")
    cust_list_pagination_count_text = (By.XPATH, "//span[@class='react-bootstrap-table-pagination-total']")
    cust_list_customer_search_bar = (By.XPATH,"//input[@name='searchBar']")


    def customer_list_sales_module(self):
        self.actions.wait_for_element(self.cust_list_sales_mod)
        self.actions.click(self.cust_list_sales_mod)

    def customer_list_customer_submodule(self):
        self.actions.wait_for_element(self.cust_list_customer_sub_mod)
        self.actions.click(self.cust_list_customer_sub_mod)


    def assert_invoice_total_count_in_all_sales_with_total_invoice_displayed(self, all_sales_test_data):
        self.all_sales.all_sales_list_sales_module()
        logger.info("Click on Sales module")
        self.all_sales.all_sales_list_all_sales_submodule()
        logger.info("Click on All sales sub-module")
        actual_transaction_count = self.all_sales.all_sales_verify_transaction_type_filter(all_sales_test_data)
        logger.info("Collecting the transaction count from the all sales page")
        print(f"total account: '{actual_transaction_count}'")
        self.actions.wait_for_element(self.cust_list_customer_sub_mod)
        self.actions.click(self.cust_list_customer_sub_mod)
        logger.info("Click on customer sub-module")
        time.sleep(2)
        self.actions.wait_for_element(self.cust_list_card_total_sale_count)
        self.actions.scroll_to_the_element(self.cust_list_card_total_sale_count)
        displayed_total_sale_count = self.actions.get_text(self.cust_list_card_total_sale_count)
        logger.info("Get the displayed total count in All sales page")
        print(f"total sale count displayed on customer list: {displayed_total_sale_count}")
        assert int(actual_transaction_count) == int(displayed_total_sale_count), (
            f"❌ Count mismatch: All Sales shows {actual_transaction_count}, but count on customer list shows {displayed_total_sale_count}"
        )
        print(f"✅ customer list and All Sales count match: {actual_transaction_count}")


    def assert_overdue_total_count_in_all_sales_with_total_overdue_displayed(self, all_sales_test_data):
        self.all_sales.all_sales_list_sales_module()
        logger.info("Click on Sales module")
        self.all_sales.all_sales_list_all_sales_submodule()
        logger.info("Click on All sales sub-module")
        actual_transaction_count = self.all_sales.all_sales_verify_transaction_overdue_status_filter(all_sales_test_data)
        logger.info("Collecting the transaction count from the all sales page")
        print(f"total count: '{actual_transaction_count}'")
        self.actions.wait_for_element(self.cust_list_customer_sub_mod)
        self.actions.click(self.cust_list_customer_sub_mod)
        logger.info("Click on customer sub-module")
        time.sleep(2)
        self.actions.wait_for_element(self.cust_list_card_overdue_count)
        self.actions.scroll_to_the_element(self.cust_list_card_overdue_count)
        displayed_total_sale_count = self.actions.get_text(self.cust_list_card_overdue_count)
        logger.info("Get the displayed total count in All sales page")
        print(f"total sale count displayed on customer list: {displayed_total_sale_count}")
        assert int(actual_transaction_count) == int(displayed_total_sale_count), (
            f"❌ Count mismatch: All Sales shows {actual_transaction_count}, but count on customer list shows {displayed_total_sale_count}"
        )
        print(f"✅ customer list and All Sales count match: {actual_transaction_count}")

    def assert_open_total_count_in_all_sales_with_total_open_displayed(self, all_sales_test_data):
        self.all_sales.all_sales_list_sales_module()
        logger.info("Click on Sales module")
        self.all_sales.all_sales_list_all_sales_submodule()
        logger.info("Click on All sales sub-module")
        actual_transaction_count = self.all_sales.all_sales_verify_transaction_open_status_filter(all_sales_test_data)
        logger.info("Collecting the transaction count from the all sales page")
        print(f"total count: '{actual_transaction_count}'")
        self.actions.wait_for_element(self.cust_list_customer_sub_mod)
        self.actions.click(self.cust_list_customer_sub_mod)
        logger.info("Click on customer sub-module")
        time.sleep(2)
        self.actions.wait_for_element(self.cust_list_card_open_invoice_count)
        self.actions.scroll_to_the_element(self.cust_list_card_open_invoice_count)
        displayed_total_sale_count = self.actions.get_text(self.cust_list_card_open_invoice_count)
        logger.info("Get the displayed total count in All sales page")
        print(f"total sale count displayed on customer list: {displayed_total_sale_count}")
        assert int(actual_transaction_count) == int(displayed_total_sale_count), (
            f"❌ Count mismatch: All Sales shows {actual_transaction_count}, but count on customer list shows {displayed_total_sale_count}"
        )
        print(f"✅ customer list and All Sales count match: {actual_transaction_count}")


    def assert_paid_total_count_in_all_sales_with_total_paid_displayed(self, all_sales_test_data):
        self.all_sales.all_sales_list_sales_module()
        logger.info("Click on Sales module")
        self.all_sales.all_sales_list_all_sales_submodule()
        logger.info("Click on All sales sub-module")
        actual_transaction_count = self.all_sales.all_sales_verify_transaction_deposited_status_filter(all_sales_test_data)
        logger.info("Collecting the transaction count from the all sales page")
        print(f"total count: '{actual_transaction_count}'")
        self.actions.wait_for_element(self.cust_list_customer_sub_mod)
        self.actions.click(self.cust_list_customer_sub_mod)
        logger.info("Click on customer sub-module")
        time.sleep(2)
        self.actions.wait_for_element(self.cust_list_card_paid_invoice_count)
        self.actions.scroll_to_the_element(self.cust_list_card_paid_invoice_count)
        displayed_total_sale_count = self.actions.get_text(self.cust_list_card_paid_invoice_count)
        logger.info("Get the displayed total count in All sales page")
        print(f"total sale count displayed on customer list: {displayed_total_sale_count}")
        assert int(actual_transaction_count) == int(displayed_total_sale_count), (
            f"❌ Count mismatch: All Sales shows {actual_transaction_count}, but count on customer list shows {displayed_total_sale_count}"
        )
        print(f"✅ customer list and All Sales count match: {actual_transaction_count}")

    def verify_customer_search_bar(self, customer_list_test_data):
        name_count = 0
        expected_name = customer_list_test_data["customer_name"]

        self.actions.wait_for_element(self.cust_list_customer_search_bar)
        self.actions.send_keys(self.cust_list_customer_search_bar, expected_name)
        logger.info("Customer name entered.")

        self.wait.until(EC.presence_of_all_elements_located(self.cust_list_customer_table_row))
        logger.info("List displayed according to searched name.")
        time.sleep(2)


        while True:
            # Refetch elements each time
            self.wait.until(EC.presence_of_all_elements_located(self.cust_list_customer_name_column))
            customer_name_elements = self.driver.find_elements(*self.cust_list_customer_name_column)
            time.sleep(1)  # allow render

            for _ in range(2):  # retry stale reads max 2 times
                try:
                    for e_elem in customer_name_elements:
                        try:
                            displayed_customer_name = e_elem.text.strip()
                            assert expected_name.lower() in displayed_customer_name.lower(), \
                                f"Wrong name displayed: {displayed_customer_name}"
                            name_count += 1
                        except StaleElementReferenceException:
                            logger.warning("Stale element encountered, retrying this row.")
                            break  # refetch all elements
                    else:
                        break  # inner loop successful, no stale exception
                except Exception as e:
                    logger.warning(f"Unexpected error during row check: {e}")
                    continue

            try:
                self.actions.scroll_to_the_element(self.cust_list_next_btn)
                next_btn = self.driver.find_element(*self.cust_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.cust_list_customer_table_row))
            except NoSuchElementException:
                logger.info("No next button found — assumed end of pagination.")
                break
            except Exception as e:
                logger.warning(f"Pagination ended or error occurred: {e}")
                break

        assert name_count > 0, "No searched name found!"
        print(f"✅ Total matched customer entries: {name_count}.")

        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.cust_list_pagination_count_text)
        )
        pagination_text = pagination_text_element.text.strip()

        match = re.search(r"of\s+(\d+)", pagination_text)
        if match:
            total_count = int(match.group(1))
            print(f"✅ Total rows in pagination: {total_count}")
        else:
            raise AssertionError("Could not extract total row count from pagination text.")

        assert total_count == name_count, (
            f"Mismatch: Filtered customer count = {name_count}, "
            f"but pagination shows = {total_count}"
        )

        return total_count

    def verify_customer_name_clickable(self, customer_transaction_list_test_data ):
        self.actions.click(self.cust_list_sales_mod)
        logger.info("Click on Sales module")
        self.actions.click(self.cust_list_customer_sub_mod)
        logger.info("Click on All sales sub-module")

        expected_name = customer_transaction_list_test_data["transaction_info"]["customer_name"].strip().lower()

        self.wait.until(EC.presence_of_all_elements_located(self.cust_list_customer_table_row))
        time.sleep(2)

        while True:
            customer_name_row_elements = self.driver.find_elements(*self.cust_list_customer_name_column)

            for elem in customer_name_row_elements:
                name_text = elem.text.strip().lower()
                print(f"Found customer name '{name_text}'")
                return name_text  # Stop after clicking
            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.cust_list_next_btn)
                next_btn = self.driver.find_element(*self.cust_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    logger.warning("Reached last page, name not found.")
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.cust_list_customer_table_row))
                self.wait.until(EC.staleness_of(customer_name_row_elements[0]))

            except NoSuchElementException:
                logger.warning("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                logger.error(f"❌ Unexpected error during pagination: {e}")
                break

        # If loop exits without clicking
        assert False, f"❌ Customer name '{expected_name}' not found across pages"

    def verify_customer_name_clickable_navigation(self, customer_transaction_list_test_data ):
        expected_name = customer_transaction_list_test_data["transaction_info"]["customer_name"].strip().lower()

        self.wait.until(EC.presence_of_all_elements_located(self.cust_list_customer_table_row))
        time.sleep(2)

        while True:
            customer_name_row_elements = self.driver.find_elements(*self.cust_list_customer_name_column)

            for elem in customer_name_row_elements:
                name_text = elem.text.strip().lower()
                elem.click()
                print(f"Found customer name '{name_text}'")
                return name_text  # Stop after clicking
            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.cust_list_next_btn)
                next_btn = self.driver.find_element(*self.cust_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    logger.warning("Reached last page, name not found.")
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.cust_list_customer_table_row))
                self.wait.until(EC.staleness_of(customer_name_row_elements[0]))

            except NoSuchElementException:
                logger.info("✅ No next button found — assumed end of pagination.")
                break

            except Exception as e:
                logger.info(f"❌ Unexpected error during pagination: {e}")
                break

        # If loop exits without clicking
        assert False, f"❌ Customer name '{expected_name}' not found across pages"

    def verify_customer_name_and_get_open_balance(self, customer_transaction_list_test_data):
        expected_name = customer_transaction_list_test_data["transaction_info"]["customer_name"].strip().lower()

        self.wait.until(EC.presence_of_all_elements_located(self.cust_list_customer_table_row))
        time.sleep(2)

        while True:
            customer_name_elements = self.driver.find_elements(*self.cust_list_customer_name_column)

            for elem in customer_name_elements:
                name_text = elem.text.strip().lower()
                if expected_name in name_text:
                    logger.info(f" Found customer '{name_text}'")

                    # Navigate to the parent <tr> to access sibling <td> for balance
                    row = elem.find_element(By.XPATH, "./ancestor::tr")
                    balance_td = row.find_elements(By.TAG_NAME, "td")[3]  # 4th column (index 3) = Open Balance
                    open_balance = balance_td.text.strip()
                    logger.info(f" Open balance for '{name_text}' is: {open_balance}")

                    # You can optionally click here
                    elem.click()
                    return open_balance

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.cust_list_next_btn)
                next_btn = self.driver.find_element(*self.cust_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    logger.info("Reached last page — customer not found.")
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.cust_list_customer_table_row))
                self.wait.until(EC.staleness_of(customer_name_elements[0]))

            except NoSuchElementException:
                logger.info(" No next button found — assumed end of pagination.")
                break

            except Exception as e:
                logger.error(f" Unexpected error during pagination: {e}")
                break

        # If loop exits without finding the customer
        assert False, f" Customer name '{expected_name}' not found across pages"
