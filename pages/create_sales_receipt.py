from selenium.webdriver.common.by import By

from actions.actions import Actions


class SalesReceipt:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)

    sales_r_plus_new = (By.XPATH, "//button[@class='pe-5 ps-5 btn btn-sm m-3 m-3']")
    sales_r_sales_receipt= (By.XPATH, "//a[normalize-space()='Sales Receipt']")
    sales_r_select_customer = (By.ID, "react-select-2-input")
    sales_r_options_customer = (By.XPATH, "//div[contains(@class, 'option')]")
    sales_r_cust_email = (By.XPATH, "//input[@label='Email']")
    sales_r_billing_address = (By.XPATH, "//label[contains(text(),'Billing')]/following::input[@placeholder='Enter a location']")
    sales_r_options_billing = (By.XPATH, "/html/body/div[3]/div")
    sales_r_shipping_address = (By.XPATH, "//label[contains(text(),'Shipping')]/following::input[@placeholder='Enter a location']")
    sales_r_options_shipping = (By.XPATH, "/html/body/div[4]/div")
    sales_r_location_of_sale = (By.XPATH, "//label[contains(text(),'Location Of Sale')]/following::input[@placeholder='Enter a location']")
    sales_r_options_location_of_sale = (By.XPATH, "/html/body/div[5]/div")
    sales_r_sales_receipt_date = (By.XPATH, "//input[@name='sales_receipt_date']")
    sales_r_current_month = (By.CLASS_NAME, "react-datepicker__current-month")
    sales_r_dt_next_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--next")
    sales_r_dt_prev_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--previous")
    sales_r_sales_receipt_no = (By.XPATH, "//input[@name='sales_receipt_no']")
    sales_r_payment_method= (By.ID, "react-select-4-input")
    sales_r_options_payment_method= (By.XPATH, "//div[contains(@class, 'option')]")
    sales_r_deposit_to = (By.ID, "react-select-5-input")
    sales_r_options_deposit_to = (By.XPATH, "//div[contains(@class, 'option')]")
    sales_r_add_new_lines = (By.XPATH, "//button[@id='zoom-secondary-outline-btn']")
    sales_r_select_product_service = (By.ID, "react-select-10-input")
    sales_r_options_product_service = (By.XPATH, "//div[contains(@class, 'option')]")
    sales_r_product_qty = (By.XPATH, "//table//tbody//td[4]//input")
    sales_r_product_rate = (By.XPATH, "//table//tbody//td[5]//input")
    sales_r_product_amount = (By.XPATH, "//table//tbody//td[6]//input")
    sales_r_product_tax = (By.XPATH, "//table//tbody//td[7]//input")
    sales_r_product_total = (By.XPATH, "//table//tbody//td[7]//input")
    sales_r_txt_sub_total = (By.XPATH, "//h5[1]//span[1]")
    sales_r_txt_total_tax = (By.XPATH, "//div[@class='col-md-6']//h5[2]//span[1]")
    sales_r_balance = (By.XPATH, "//h5[3]//span[1]")
    sales_r_memo = (By.XPATH, "//textarea[@name='memo']")
    sales_r_btn_save_close = (By.XPATH, "//button[@id='zoom-primary-cancel-btn']")
    sales_r_btn_save_new = (By.XPATH, "//button[normalize-space()='Save and New']")
    sales_r_btn_cancel = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[1]")
    sales_r_btn_clear = (By.XPATH, "//div[@class='expense-footer-btns']//div[1]//button[2]")
    sales_r_btn_x = (By.XPATH, "//div[contains(@class, 'toast') and contains(@class, 'show')]//button[contains(@class, 'btn-close')]")


    def sr_plus_new(self):
        self.actions.wait_for_element(self.sales_r_plus_new)
        self.actions.click(self.sales_r_plus_new)

    def sr_sales_receipt(self):
        self.actions.wait_for_element(self.sales_r_sales_receipt)
        self.actions.click(self.sales_r_sales_receipt)

    def sr_select_customer(self, create_sales_receipt_test_data):
        self.actions.wait_for_element(self.sales_r_select_customer)
        self.actions.scroll_to_the_element(self.sales_r_select_customer)
        self.actions.dropdown_equals(self.sales_r_select_customer, self.sales_r_options_customer,create_sales_receipt_test_data["sr_customer"])

    def sr_email(self, create_sales_receipt_test_data):
        self.actions.wait_for_element(self.sales_r_cust_email)
        self.actions.scroll_to_the_element(self.sales_r_cust_email)
        self.actions.send_keys(self.sales_r_cust_email, create_sales_receipt_test_data[""])

    def sr_shipping_address(self, create_sales_receipt_test_data):
        self.actions.wait_for_element(self.sales_r_shipping_address)
        self.actions.scroll_to_the_element(self.sales_r_shipping_address)
        self.actions.dropdown_contains(self.sales_r_shipping_address, self.sales_r_options_shipping, create_sales_receipt_test_data[""])

    def sr_billing_address(self, create_sales_receipt_test_data):
        self.actions.wait_for_element(self.sales_r_billing_address)
        self.actions.scroll_to_the_element(self.sales_r_options_billing)
        self.actions.dropdown_contains(self.sales_r_billing_address, self.sales_r_options_billing,create_sales_receipt_test_data[""])

    def sr_location_of_sale(self, create_sales_receipt_test_data):
        self.actions.wait_for_element(self.sales_r_location_of_sale)
        self.actions.scroll_to_the_element(self.sales_r_location_of_sale)
        self.actions.dropdown_contains(self.sales_r_location_of_sale, self.sales_r_options_location_of_sale,create_sales_receipt_test_data[""])

    def sr_sales_receipt_date(self, create_sales_receipt_test_data):
        self.actions.wait_for_element(self.sales_r_sales_receipt_date)
        self.actions.scroll_to_the_element(self.sales_r_sales_receipt_date)
        self.actions.select_date(self.sales_r_sales_receipt_date, self.sales_r_current_month,self.sales_r_dt_next_btn_class, self.sales_r_dt_prev_btn_class,create_sales_receipt_test_data["sales_receipt_date"])

    def sr_sales_receipt_no(self):
        self.actions.wait_for_element(self.sales_r_sales_receipt_no)
        self.actions.scroll_to_the_element(self.sales_r_sales_receipt_no)
        self.actions.get_attribute(self.sales_r_sales_receipt_no)

    def sr_payment_method(self, create_sales_receipt_test_data):
        self.actions.wait_for_element(self.sales_r_payment_method)
        self.actions.scroll_to_the_element(self.sales_r_payment_method)
        self.actions.dropdown_contains(self.sales_r_payment_method, self.sales_r_options_payment_method,create_sales_receipt_test_data["sr_payment_method"])

    def sr_deposit_to(self, create_sales_receipt_test_data):
        self.actions.wait_for_element(self.sales_r_deposit_to)
        self.actions.scroll_to_the_element(self.sales_r_deposit_to)
        self.actions.dropdown_contains(self.sales_r_deposit_to, self.sales_r_options_deposit_to,create_sales_receipt_test_data["sr_deposit_to"])

    def cm_add_new_lines(self):
        self.actions.wait_for_element(self.sales_r_add_new_lines)
        self.actions.click(self.sales_r_add_new_lines)

    def sr_select_product_service(self, create_sales_receipt_test_data):
        self.actions.wait_for_element(self.sales_r_select_product_service)
        self.actions.scroll_to_the_element(self.sales_r_select_product_service)
        self.actions.dropdown_contains(self.sales_r_select_product_service, self.sales_r_options_product_service ,create_sales_receipt_test_data["sr_product_service"])

    def sr_product_qty(self, create_sales_receipt_test_data):
        self.actions.wait_for_element(self.sales_r_product_qty)
        self.actions.scroll_to_the_element(self.sales_r_product_qty)
        self.actions.clear_text(self.sales_r_product_qty)
        self.actions.send_keys(self.sales_r_product_qty, create_sales_receipt_test_data["sr_quantity"])

    def sr_product_rate(self, create_sales_receipt_test_data):
        self.actions.wait_for_element(self.sales_r_product_rate)
        self.actions.scroll_to_the_element(self.sales_r_product_rate)
        self.actions.send_keys(self.sales_r_product_rate, create_sales_receipt_test_data["rate_per_unit"])

    def sr_product_amount(self):
        self.actions.wait_for_element(self.sales_r_product_amount)
        self.actions.scroll_to_the_element(self.sales_r_product_amount)
        self.actions.get_attribute(self.sales_r_product_amount)

    def sr_product_tax(self):
        self.actions.wait_for_element(self.sales_r_product_tax)
        self.actions.scroll_to_the_element(self.sales_r_product_tax)
        self.actions.get_attribute(self.sales_r_product_tax)

    def sr_product_total(self):
        self.actions.wait_for_element(self.sales_r_product_total)
        self.actions.scroll_to_the_element(self.sales_r_product_total)
        self.actions.get_attribute(self.sales_r_product_total)

    def sr_memo(self, create_credit_memo_test_data):
        self.actions.wait_for_element(self.sales_r_memo)
        self.actions.scroll_to_the_element(self.sales_r_memo)
        self.actions.send_keys(self.sales_r_memo, create_credit_memo_test_data["sr_memo"])

    def sr_cancel(self):
        self.actions.wait_for_element(self.sales_r_btn_cancel)
        self.actions.scroll_to_the_element(self.sales_r_btn_cancel)
        self.actions.click(self.sales_r_btn_cancel)

    def sr_clear(self):
        self.actions.wait_for_element(self.sales_r_btn_clear)
        self.actions.scroll_to_the_element(self.sales_r_btn_clear)
        self.actions.click(self.sales_r_btn_clear)

    def sr_save_and_close(self):
        self.actions.wait_for_element(self.sales_r_btn_save_close)
        self.actions.scroll_to_the_element(self.sales_r_btn_save_close)
        self.actions.click(self.sales_r_btn_save_close)

    def sr_save_and_new(self):
        self.actions.wait_for_element(self.sales_r_btn_save_new)
        self.actions.scroll_to_the_element(self.sales_r_btn_save_new)
        self.actions.click(self.sales_r_btn_save_new)

    def sr_x_button(self):
        self.actions.wait_for_element(self.sales_r_btn_x)
        self.actions.scroll_to_the_element(self.sales_r_btn_x)
        self.actions.click(self.sales_r_btn_x)





