import logging
import re
import time
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.actions import Actions
from pages.customer_list import CustomerList

logger = logging.getLogger(__name__)


class CustomerTransactionList:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 100)
        self.customer_list = CustomerList(driver)

    customer_transaction_list_sales_mod = (By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
    customer_transaction_list_sub_mod = (By.XPATH, "//a[normalize-space()='Customers']")
    #customer_transaction_list_sub_mod =(By.XPATH,"")
    customer_transaction_list_cust_name = (By.XPATH, "//h6[@class='text-black fw-bold']")
    customer_transaction_list_open_amt = (By.XPATH,"//div[@class='me-5']//span[1]")
    customer_transaction_list_overdue_amt = (By.XPATH,"//div[@class='col-md-6']//div[2]//p[1]//span[1]")
    customer_transaction_list_transaction_list_section = (By.XPATH,"//a[@class='nav-link sc-kdBSHD fyvSCS active']")
    customer_transaction_list_customer_details_section = (By.XPATH,"//a[@class='nav-link sc-kdBSHD fyvSCS']")
    customer_transaction_list_type_dd = (By.XPATH,"//div[@class='d-xl-flex flex-row justify-content-between']//div//div[1]//select[1]")
    customer_transaction_list_options_type_dd = (By.XPATH,"//label[text()='Type']/following-sibling::select/option")
    customer_transaction_list_status_dd = (By.XPATH,"//div[@class='d-xl-flex flex-row justify-content-between']//div//div[2]//select[1]")
    customer_transaction_list_options_status_dd = (By.XPATH, "//label[text()='Status']/following-sibling::select/option")
    customer_transaction_list_new_transaction_dd = (By.XPATH, "//button[normalize-space()='New Transaction']")
    customer_transaction_list_new_transaction_dd_invoices = (By.XPATH, "//a[@class='dropdown-item sc-eDPEul inWBsQ'][normalize-space()='Invoice']")
    customer_transaction_list_new_transaction_dd_receive_payment = (By.XPATH, "//a[@class='dropdown-item sc-eDPEul inWBsQ'][normalize-space()='Receive Payment']")
    customer_transaction_list_new_transaction_dd_credit_memo = (By.XPATH, "//a[@class='dropdown-item sc-eDPEul inWBsQ'][normalize-space()='Credit Memo']")
    customer_transaction_list_new_transaction_dd_sales_receipt = (By.XPATH, "//a[@class='dropdown-item sc-eDPEul inWBsQ'][normalize-space()='Sales Receipt']")
    customer_transaction_list_new_transaction_dd_refund_receipt = (By.XPATH, "//a[@class='dropdown-item sc-eDPEul inWBsQ'][normalize-space()='Refund Receipt']")
    customer_transaction_list_table_rows = (By.XPATH, "//table//tr")
    customer_transaction_list_table_recurring_column = (By.XPATH, "//table//tr//td[1]")
    customer_transaction_list_table_date_column = (By.XPATH, "//table//tr//td[2]")
    customer_transaction_list_table_type_column = (By.XPATH, "//table//tr//td[3]")
    customer_transaction_list_table_transaction_no_column = (By.XPATH, "//table//tr//td[4]")
    customer_transaction_list_table_memo_column = (By.XPATH, "//table//tr//td[5]")
    customer_transaction_list_table_due_Date_column = (By.XPATH, "//table//tr//td[6]")
    customer_transaction_list_table_balance_column = (By.XPATH, "//table//tr//td[7]")
    customer_transaction_list_table_amount_column = (By.XPATH, "//table//tr//td[8]")
    customer_transaction_list_status_column = (By.XPATH,"//table//tr//td[9]")
    customer_transaction_list_table_actions_column = (By.XPATH, "//table//tr//td[10]")
    customer_transaction_list_next_btn = (By.XPATH, "//a[normalize-space()='>']")
    customer_transaction_list_dropdown = (By.XPATH, "//button[@id='pageDropDown']")
    customer_transaction_list_dd_option25 = (By.XPATH, "//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), '25')]")
    customer_transaction_list_option30 = (By.XPATH, "//ul[contains(@class, 'dropdown-menu')]/li/a[contains(text(), '30')]")
    customer_transaction_list_dd_option50 = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[2]/div/div[4]/div/div/div[2]/div[1]/span[1]/ul/li[4]/a")
    customer_transaction_list_pagination_count_text = (By.XPATH, "//span[@class='react-bootstrap-table-pagination-total']")


    def customer_transaction_list_sales_module(self):
        self.actions.wait_for_element(self.customer_transaction_list_sales_mod)
        self.actions.click(self.customer_transaction_list_sales_mod)

    def customer_transaction_list_all_sales_submodule(self):
        self.actions.wait_for_element(self.customer_transaction_list_sub_mod)
        self.actions.click(self.customer_transaction_list_sub_mod)

    def customer_transaction_list_verify_customer_clickable_navigation(self, customer_transaction_list_test_data):
        customer_list_displayed_name = self.customer_list.verify_customer_name_clickable(customer_transaction_list_test_data)
        print(f"customer_transaction_list_displayed_customer_name:{customer_list_displayed_name}")
        self.customer_list.verify_customer_name_clickable_navigation(customer_transaction_list_test_data)
        time.sleep(2)
        customer_transaction_list_displayed_customer_name=self.actions.get_text(self.customer_transaction_list_cust_name)
        print(f"customer_transaction_list_displayed_customer_name:{customer_transaction_list_displayed_customer_name}")
        assert customer_transaction_list_displayed_customer_name.lower() == customer_list_displayed_name.lower(), \
            f"❌ Customer name mismatch: expected '{customer_list_displayed_name}', got '{customer_transaction_list_displayed_customer_name}'"

    def customer_transaction_verify_open_balance_with_transaction_list(self, customer_transaction_list_test_data):
        self.customer_list.customer_list_sales_module()
        self.customer_list.customer_list_customer_submodule()
        customer_list_displayed_open_balance = self.customer_list.verify_customer_name_and_get_open_balance(customer_transaction_list_test_data)
        #self.customer_list.verify_customer_name_clickable_navigation(customer_transaction_list_test_data)
        time.sleep(2)
        customer_transaction_list_displayed_open_balance =  self.actions.get_text(self.customer_transaction_list_open_amt)
        assert customer_list_displayed_open_balance== customer_transaction_list_displayed_open_balance, f" both the open balance ae not same"

    def customer_transaction_list_verify_open_balance_with_sum_transactions(self,customer_transaction_list_test_data):
        self.customer_list.verify_customer_name_clickable_navigation(customer_transaction_list_test_data)
        self.wait.until(EC.presence_of_all_elements_located(self.customer_transaction_list_table_rows))
        time.sleep(2)

        # Get and clean displayed open balance
        self.actions.wait_for_element(self.customer_transaction_list_open_amt)
        displayed_open_balance_text = self.actions.get_text(self.customer_transaction_list_open_amt)
        try:
            cleaned_balance = displayed_open_balance_text.replace("₹", "").replace(",", "").replace(" ", "").strip()
            displayed_open_balance = float(cleaned_balance)

        except ValueError:
            logger.error(f"Could not convert displayed open balance: {displayed_open_balance_text}")
            assert False, "Invalid format for displayed open balance"

        total_balance_sum = 0.0  # Initialize total

        while True:
            # Fetch all amounts from balance column on the current page
            balance_column_elements = self.driver.find_elements(*self.customer_transaction_list_table_balance_column)

            for b_elem in balance_column_elements:
                balance_text = b_elem.text.strip()

                if balance_text:
                    try:
                        clean_text = balance_text.replace("₹", "").replace(",", "").replace(" ", "").strip()
                        total_balance_sum += float(clean_text)
                    except ValueError:
                        logger.warning(f"Could not convert balance value: {balance_text}")
                        continue

            # Pagination logic
            try:
                self.actions.scroll_to_the_element(self.customer_transaction_list_next_btn)
                next_btn = self.driver.find_element(*self.customer_transaction_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    logger.info(f"Reached last page. Total balance sum: {total_balance_sum}")
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.customer_transaction_list_table_rows))
                self.wait.until(EC.staleness_of(balance_column_elements[0]))

            except NoSuchElementException:
                logger.info(
                    f"No next button found — assumed end of pagination. Total balance sum: {total_balance_sum}")
                break

            except Exception as e:
                logger.error(f"Unexpected error during pagination: {e}")
                break

        # Assert after pagination completes
        assert round(displayed_open_balance, 2) == round(total_balance_sum, 2), (
            f"Mismatch in Open Balance: Displayed = ₹{displayed_open_balance}, Calculated = ₹{total_balance_sum}"
        )

        logger.info(f"Open Balance matches: ₹{total_balance_sum}")

    def customer_transaction_list_verify_overdue_amount_with_overdue_transactions_sum(self,customer_transaction_list_test_data):
        self.customer_list.verify_customer_name_clickable_navigation(customer_transaction_list_test_data)
        expected_status = customer_transaction_list_test_data["Status_Group"]["overdue_status"].lower()
        expected_types = customer_transaction_list_test_data["Status_Group"]["overdue_expected_types"]
        transaction_count = 0
        total_balance_sum = 0.0

        # Select status from dropdown
        self.actions.wait_for_element(self.customer_transaction_list_status_dd)
        self.actions.dropdown_contains(
            self.customer_transaction_list_status_dd,
            self.customer_transaction_list_options_status_dd,
            customer_transaction_list_test_data["Status_Group"]["overdue_status"]
        )

        self.wait.until(EC.presence_of_all_elements_located(self.customer_transaction_list_table_rows))
        time.sleep(2)

        while True:
            # Get all type, status, and balance column elements
            type_elements = self.driver.find_elements(*self.customer_transaction_list_table_type_column)
            status_elements = self.driver.find_elements(*self.customer_transaction_list_table_balance_column)
            balance_elements = self.driver.find_elements(*self.customer_transaction_list_table_balance_column)
            print(f"type_elements:{type_elements}")
            print(f"type_elements:{status_elements}")
            #assert len(type_elements) == len(status_elements), "Mismatch between types and statuses"

            for t_elem, s_elem, b_elem in zip(type_elements, status_elements, balance_elements):
                transaction_type = t_elem.text.strip()
                transaction_status = s_elem.text.strip().lower()
                balance_text = b_elem.text.strip()
                transaction_count += 1

                # Validate status logic
                if expected_status == "open":
                    if transaction_type.lower() == "invoice":
                        assert any(
                            keyword in transaction_status for keyword in ["due in", "partially paid", "overdue"]), \
                            f"Unexpected status '{transaction_status}' for type 'Invoice'"
                    else:
                        assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                elif expected_status in ["paid", "closed", "applied", "unapplied", "deposited", "overdue"]:
                    assert transaction_type in expected_types, f"Unexpected transaction type: {transaction_type}"
                else:
                    raise AssertionError(f" Unhandled status filter: {expected_status}")

                # Add balance amount
                if balance_text:
                    try:
                        clean_text = balance_text.replace("₹", "").replace(",", "").replace(" ", "").strip()
                        total_balance_sum += float(clean_text)
                    except ValueError:
                        print(f" Skipping invalid balance value: {balance_text}")
                        continue

            # Pagination handling
            try:
                self.actions.scroll_to_the_element(self.customer_transaction_list_next_btn)
                next_btn = self.driver.find_element(*self.customer_transaction_list_next_btn)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    break

                next_btn.click()
                self.wait.until(EC.presence_of_all_elements_located(self.customer_transaction_list_table_rows))
                self.wait.until(EC.staleness_of(type_elements[0]))

            except NoSuchElementException:
                print(" No next button found — assumed end of pagination.")
                break
            except StaleElementReferenceException:
                print(" Pagination element went stale — assumed end of pagination.")
                break
            except Exception as e:
                print(f" Unexpected error during pagination: {e}")
                break

        # Final validation after pagination
        assert transaction_count > 0, f"No transactions found for status: {customer_transaction_list_test_data['Status_Group']['overdue_status']}"
        print(
            f" Verified {transaction_count} transactions for status: {customer_transaction_list_test_data['Status_Group']['overdue_status']}")

        # Extract pagination total row count
        pagination_text_element = self.wait.until(
            EC.presence_of_element_located(self.customer_transaction_list_pagination_count_text))
        pagination_text = pagination_text_element.text.strip()
        match = re.search(r"of\s+(\d+)", pagination_text)
        if match:
            total_count = int(match.group(1))
            print(f" Total transactions: {transaction_count}")
            print(f" Total rows in pagination: {total_count}")
        else:
            raise AssertionError(" Could not extract total row count from pagination text.")
        assert total_count == transaction_count, f" Mismatch: Filtered transaction count = {transaction_count}, but pagination shows = {total_count}"

        # --- Overdue Amount Assertion ---
        # Get displayed overdue amount (top-right)
        overdue_amount_text = self.actions.get_text(self.customer_transaction_list_overdue_amt)
        try:
            cleaned_displayed_overdue = float(overdue_amount_text.replace("₹", "").replace(",", "").replace(" ", "").strip())
            displayed_overdue_balance_amount = float(cleaned_displayed_overdue)
        except ValueError:
            raise AssertionError(f" Invalid format for displayed overdue amount: {overdue_amount_text}")

        # Compare with sum of balances
        assert round(displayed_overdue_balance_amount, 2) == round(total_balance_sum, 2), \
            f" Overdue mismatch: Displayed = ₹{displayed_overdue_balance_amount}, Calculated = ₹{total_balance_sum}"

        print(f" Overdue amount verified successfully: ₹{total_balance_sum}")
        return total_balance_sum


