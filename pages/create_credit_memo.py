from selenium.webdriver.common.by import By

from actions.actions import Actions


class CreditMemo:
    def __init__(self, driver):
        #self.expected_name = None
        self.expected_ref_no = None
        self.driver = driver
        self.actions = Actions(driver)

    credit_m_plus_new = (By.XPATH, "//button[@class='pe-5 ps-5 btn btn-sm m-3 m-3']")
    credit_m_credit_memo = (By.XPATH, "//a[normalize-space()='Credit Memo']")
    credit_m_select_customer = (By.XPATH, "//label[text()='Customer *']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    credit_m_options_customer = (By.XPATH, "//div[contains(@class, 'option')]")
    credit_m_cust_email = (By.XPATH, "//input[@label='Email']")
    credit_m_billing_address = (By.XPATH, "//label[contains(text(),'Billing')]/following::input[@placeholder='Enter a location']")
    credit_m_options_billing = (By.XPATH, "/html/body/div[3]/div")
    credit_m_shipping_address = (By.XPATH, "//label[contains(text(),'Shipping')]/following::input[@placeholder='Enter a location']")
    credit_m_options_shipping = (By.XPATH, "/html/body/div[4]/div")
    credit_m_location_of_sale = (By.XPATH, "//label[contains(text(),'Location Of Sale')]/following::input[@placeholder='Enter a location']")
    credit_m_options_location_of_sale = (By.XPATH, "/html/body/div[5]/div")
    credit_m_credit_memo_date = (By.XPATH, "//input[@name='credit_memo_date']")
    credit_m_current_month = (By.CLASS_NAME, "react-datepicker__current-month")
    credit_m_dt_next_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--next")
    credit_m_dt_prev_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--previous")
    credit_m_credit_memo_no = (By.XPATH, "//input[@name='credit_memo_no']")
    credit_m_select_transactions = (By.XPATH, "//label[text()='Select Transaction']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    credit_m_options_transactions = (By.XPATH, "//div[contains(@class, 'option')]")
    credit_m_add_new_lines = (By.XPATH, "//button[@id='zoom-secondary-outline-btn']")
    credit_m_select_product_service = (By.XPATH, "//label[text()='PRODUCT/SERVICE *']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    credit_m_options_product_service = (By.XPATH, "//div[contains(@class, 'option')]")
    credit_m_product_qty = (By.XPATH, "//table//tbody//td[5]//input")
    credit_m_product_rate = (By.XPATH, "//table//tbody//td[6]//input")
    credit_m_product_amount = (By.XPATH, "//table//tbody//td[7]//input")
    credit_m_product_tax = (By.XPATH, "//table//tbody//td[8]//input")
    credit_m_gst_rate = (By.XPATH, "//table//tbody//td[8]//span")
    credit_m_total_amount = (By.XPATH, "//table//tbody//td[9]//div")
    credit_m_delete_lineitems = (By.XPATH, "//table//tbody//td[10]//button")
    credit_m_txt_sub_total = (By.XPATH, "//h5[1]//span[1]")
    credit_m_total_tax = (By.XPATH, "//div[@class='col-md-6']//h5[2]//span[1]")
    credit_m_balance = (By.XPATH, "//h5[3]//span[1]")
    credit_m_memo = (By.XPATH, "//textarea[@name='memo']")
    credit_m_btn_save_close = (By.XPATH, "//button[@id='zoom-primary-cancel-btn']")
    credit_m_btn_save_new = (By.XPATH, "//button[normalize-space()='Save and New']")
    credit_m_btn_cancel = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[1]")
    credit_m_btn_clear = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[2]")
    credit_m_btn_x = (By.XPATH,"//div[contains(@class, 'toast') and contains(@class, 'show')]//button[contains(@class, 'btn-close')]")
    def cm_plus_new(self):
        self.actions.wait_for_element(self.credit_m_plus_new)
        self.actions.click(self.credit_m_plus_new)

    def cm_credit_memo(self):
        self.actions.wait_for_element(self.credit_m_credit_memo)
        self.actions.click(self.credit_m_credit_memo)

    def cm_select_customer(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.credit_m_select_customer)
        self.actions.scroll_to_the_element(self.credit_m_select_customer)
        self.actions.dropdown_equals(self.credit_m_select_customer, self.credit_m_options_customer,
                                     create_credit_memo_test_data["cm_customer"])

    def cm_select_customer_sales_flow(self, customer_name):
        self.actions.wait_for_element(self.credit_m_select_customer)
        self.actions.scroll_to_the_element(self.credit_m_select_customer)
        self.actions.dropdown_equals(self.credit_m_select_customer, self.credit_m_options_customer,
                                     customer_name)

    def cm_email(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.credit_m_cust_email)
        self.actions.scroll_to_the_element(self.credit_m_cust_email)
        self.actions.send_keys(self.credit_m_cust_email, create_credit_memo_test_data[""])

    def cm_shipping_address(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.credit_m_shipping_address)
        self.actions.scroll_to_the_element(self.credit_m_shipping_address)
        self.actions.dropdown_contains(self.credit_m_shipping_address, self.credit_m_options_shipping,
                                       create_credit_memo_test_data[""])

    def cm_billing_address(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.credit_m_billing_address)
        self.actions.scroll_to_the_element(self.credit_m_billing_address)
        self.actions.dropdown_contains(self.credit_m_billing_address, self.credit_m_options_billing,
                                       create_credit_memo_test_data[""])

    def cm_location_of_sale(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.credit_m_location_of_sale)
        self.actions.scroll_to_the_element(self.credit_m_location_of_sale)
        self.actions.dropdown_contains(self.credit_m_location_of_sale, self.credit_m_options_location_of_sale,
                                       create_credit_memo_test_data[""])

    def cm_credit_memo_date(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.credit_m_credit_memo_date)
        self.actions.scroll_to_the_element(self.credit_m_credit_memo_date)
        self.actions.select_date(self.credit_m_credit_memo_date, self.credit_m_current_month,
                                 self.credit_m_dt_next_btn_class, self.credit_m_dt_prev_btn_class,
                                 create_credit_memo_test_data["credit_memo_date"])
    def cm_credit_memo_no(self):
        self.actions.wait_for_element(self.credit_m_credit_memo_no)
        self.actions.scroll_to_the_element(self.credit_m_credit_memo_no)
        self.credit_no = self.actions.get_attribute_value(self.credit_m_credit_memo_no)
        print(self.credit_no)
        return self.credit_no

    def cm_select_transactions(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.credit_m_select_transactions)
        self.actions.scroll_to_the_element(self.credit_m_select_transactions)
        self.actions.dropdown_equals(self.credit_m_select_transactions, self.credit_m_options_transactions,
                                     create_credit_memo_test_data["cm_select_transaction"])

    def cm_select_transactions_sales_module(self, sales_transaction_list):
        self.actions.wait_for_element(self.credit_m_select_transactions)
        self.actions.scroll_to_the_element(self.credit_m_select_transactions)
        self.actions.dropdown_contains(self.credit_m_select_transactions, self.credit_m_options_transactions,sales_transaction_list)

    def cm_add_new_lines(self):
        self.actions.wait_for_element(self.credit_m_add_new_lines)
        self.actions.click(self.credit_m_add_new_lines)

    def cm_select_product_service(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.credit_m_select_product_service)
        self.actions.scroll_to_the_element(self.credit_m_select_product_service)
        self.actions.dropdown_equals(self.credit_m_select_product_service, self.credit_m_options_product_service,
                                     create_credit_memo_test_data[""])

    def cm_product_qty(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.credit_m_product_qty)
        self.actions.scroll_to_the_element(self.credit_m_product_qty)
        self.actions.clear_text(self.credit_m_product_qty)
        self.actions.send_keys(self.credit_m_product_qty, create_credit_memo_test_data["cm_quantity"])

    def cm_product_rate(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.credit_m_product_rate)
        self.actions.scroll_to_the_element(self.credit_m_product_rate)
        self.actions.send_keys(self.credit_m_product_rate, create_credit_memo_test_data[""])

    def cm_product_amount(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.credit_m_product_amount)
        self.actions.scroll_to_the_element(self.credit_m_product_amount)
        self.actions.get_attribute(self.credit_m_product_amount)

    def cm_product_tax(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.credit_m_product_tax)
        self.actions.scroll_to_the_element(self.credit_m_product_tax)
        self.actions.get_attribute(self.credit_m_product_tax)

    def cm_gst_tax(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.credit_m_gst_rate)
        self.actions.scroll_to_the_element(self.credit_m_gst_rate)
        # Get the text value
        gst_text = self.actions.get_text(self.credit_m_gst_rate).strip()
        print(f"🧾 GST Text: {gst_text}")
        return gst_text

    def cm_product_total(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.credit_m_total_amount)
        self.actions.scroll_to_the_element(self.credit_m_total_amount)
        self.actions.get_attribute(self.credit_m_total_amount)

    def cm_memo(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.credit_m_memo)
        self.actions.scroll_to_the_element(self.credit_m_memo)
        self.actions.send_keys(self.credit_m_memo, create_credit_memo_test_data[""])

    def cm_cancel(self):
        self.actions.wait_for_element(self.credit_m_btn_cancel)
        self.actions.scroll_to_the_element(self.credit_m_btn_cancel)
        self.actions.click(self.credit_m_btn_cancel)

    def cm_clear(self):
        self.actions.wait_for_element(self.credit_m_btn_clear)
        self.actions.scroll_to_the_element(self.credit_m_btn_clear)
        self.actions.click(self.credit_m_btn_clear)

    def cm_save_and_close(self):
        self.actions.wait_for_element(self.credit_m_btn_save_close)
        self.actions.scroll_to_the_element(self.credit_m_btn_save_close)
        self.actions.click(self.credit_m_btn_save_close)

    def cm_save_and_new(self):
        self.actions.wait_for_element(self.credit_m_btn_save_new)
        self.actions.scroll_to_the_element(self.credit_m_btn_save_new)
        self.actions.click(self.credit_m_btn_save_new)

    def cm_x_button(self):
        self.actions.wait_for_element(self.credit_m_btn_x)
        self.actions.scroll_to_the_element(self.credit_m_btn_x)
        self.actions.click(self.credit_m_btn_x)