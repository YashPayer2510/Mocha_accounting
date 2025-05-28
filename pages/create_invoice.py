import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from actions.actions import Actions
from tests.conftest import create_invoice_test_data

class Create_Invoice:
    def __init__(self, driver):
        #self.expected_name = None
        self.invoice_no = None
        self.driver = driver
        self.actions = Actions(driver)

    inv_btn_submod_Sales= (By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
    inv_btn_submod_invoice =(By.XPATH,"//a[@class='nav-link'][normalize-space()='Invoices']")
    inv_btn_create_invoice = (By.XPATH,"//button[normalize-space()='Create Invoice']")
    inv_dd_customer= (By.XPATH,"//*[@id='react-select-2-input']")
    inv_options_customer = By.XPATH,"//div[contains(@class, 'option')]"
    inv_dd_credit_terms = (By.ID,"react-select-3-input")
    inv_invoice_no = (By.XPATH,"//input[@label='Invoice No']")
    inv_options_credit_terms =(By.XPATH,"//div[@role='option' and contains(@class, 'css-10wo9uf-option')]")
    inv_dd_location_of_sale =(By.XPATH,"//*[@id='root']/div/div[1]/div[2]/div[2]/div/form/div[4]/div[2]/div/div/input")
    inv_options_location_of_sale = (By.XPATH, "//span[contains(@class, 'pac-item')]")
    inv_dd_billing =(By.XPATH,"//*[@id=root]/div/div[1]/div[2]/div[2]/div/form/div[5]/div[1]/div/div/input")
    inv_options_billing =(By.XPATH,"//span[contains(@class, 'pac-item')]")
    inv_dd_shipvia =(By.XPATH,"//*[@id='root']/div/div[1]/div[2]/div[2]/div/form/div[5]/div[2]/div/div/input")
    inv_options_shipvia= (By.XPATH, "//span[contains(@class, 'pac-item')]")
    inv_dd_shipping_to =(By.XPATH,"//*[@id='root']/div/div[1]/div[2]/div[2]/div/form/div[5]/div[3]/div/div/input")
    inv_options_shipping_to = (By.XPATH, "//span[contains(@class, 'pac-item')]")
    inv_datep_invoice_date =(By.XPATH,"//input[@name='invoice_date']")
    inv_datepicker_month_class = (By.CLASS_NAME,"react-datepicker__current-month")
    inv_next_btn_class = (By.CLASS_NAME,"react-datepicker__navigation--next")
    inv_prev_btn_class = (By.CLASS_NAME,"react-datepicker__navigation--previous")
    inv_datep_shipping_date = (By.XPATH,"//input[@name='shipping_date']")
    inv_datep_due_date = (By.XPATH, "//input[@name='due_date']")
    inv_btn_add_items = (By.XPATH,"//button[@class='btn btn-light sc-eqUAAy kJGDIg shadow-none']")
    inv_dd_select_product = (By.XPATH,"//div[contains(@class,'modal-content')]//div[contains(@class,'css-19bb58m')]//input")
    inv_options_select_productservice =(By.XPATH,"//div[contains(@class, 'option')]")
    inv_inp_quanitiy = (By.XPATH,"//input[@name='quantity']")
    inv_inp_rate_per_unit = (By.XPATH,"//input[@name='rate']")
    inv_btn_prod_save = (By.XPATH,"//button[normalize-space()='Save']")
    inv_btn_prod_cancel = (By.XPATH,"//button[@class='btn btn-outline-primary btn-sm sc-eqUAAy kJGDIg']")
    inv_txt_sub_total = (By.XPATH,"//h5[1]//span[1]")
    inv_txt_tax = (By.XPATH,"//h5[2]//span[1]")
    inv_txt_amount_received = (By.XPATH,"//h5[3]//span[1]")
    inv_txt_balance = (By.XPATH, "//h5[4]//span[1]")
    inv_inp_message_on_invoice = (By.XPATH,"//div[@class='createInvoiceMessageTour']//textarea[@aria-label='With textarea']")
    inv_btn_save_close = (By.XPATH,"//button[@id='zoom-primary-cancel-btn']")
    inv_btn_save_new = (By.XPATH,"//button[normalize-space()='Save and New']")
    inv_btn_cancel = (By.XPATH,"//div[@class='expense-footer-btns']//div[1]//button[1]")
    inv_btn_clear = (By.XPATH,"//div[@class='expense-footer-btns']//div[1]//button[2]")
    inv_m_btn_x = (By.XPATH,"//div[contains(@class, 'toast') and contains(@class, 'show')]//button[contains(@class, 'btn-close')]")

    #product and service list
    inv_added_productservice_list = (By.XPATH,"//*[@id='root']//table/tbody/tr/td[2]")
    inv_added_productservice_qty =(By.XPATH,"//*[@id='root']//table/tbody/tr/td[3]")
    inv_added_productservice_rate=(By.XPATH,"//*[@id='root']//table/tbody/tr/td[4]")
    inv_added_productservice_amount=(By.XPATH,"//*[@id='root']//table/tbody/tr/td[5]")
    inv_added_productservice_tax=(By.XPATH,"//*[@id='root']//table/tbody/tr/td[6]")
    inv_added_productservice_total=(By.XPATH,"//*[@id='root']//table/tbody/tr/td[7]")


    # invoice list
    inv_list_invno = (By.XPATH,"//table//td[3]")
    btn_nxt_customerlist = (By.XPATH,"//a[normalize-space()='>']")

    #total_sum = 0.0

    #if want to access each line items then add number after tr tag e.g tr[1]


    #   Create product ete flow
    def inv_submod_Sales(self):
        self.actions.wait_for_element(self.inv_btn_submod_Sales)
        self.actions.click(self.inv_btn_submod_Sales)


    def inv_submod_invoice(self):
        self.actions.wait_for_element(self.inv_btn_submod_invoice)
        self.actions.click(self.inv_btn_submod_invoice)
        time.sleep(2)

    def inv_create_invoice(self):
        self.actions.wait_for_element(self.inv_btn_create_invoice)
        self.actions.click(self.inv_btn_create_invoice)
        time.sleep(2)

    def inv_select_customer(self, create_invoice_test_data):
        self.actions.scroll_to_the_element(self.inv_dd_customer)
        self.actions.wait_for_element(self.inv_dd_customer)
        self.actions.dropdown_equals(self.inv_dd_customer, self.inv_options_customer,create_invoice_test_data["customer_name"])

    def inv_select_credit_terms(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_dd_credit_terms)
        self.actions.scroll_to_the_element(self.inv_dd_credit_terms)
        self.actions.dropdown_equals(self.inv_dd_credit_terms, self.inv_options_credit_terms, create_invoice_test_data[""])

    def inv_get_invoice_no(self):
        self.actions.wait_for_element(self.inv_invoice_no)
        self.actions.scroll_to_the_element(self.inv_invoice_no)
        self.invoice_no = self.actions.get_attribute(self.inv_invoice_no)
        print("invoice:",self.invoice_no)

    def inv_location_of_sale(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_dd_location_of_sale)
        self.actions.scroll_to_the_element(self.inv_dd_location_of_sale)
        self.actions.dropdown_contains(self.inv_dd_location_of_sale, self.inv_options_location_of_sale, create_invoice_test_data[""])

    def inv_shippingvia(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_dd_shipvia)
        self.actions.scroll_to_the_element(self.inv_dd_shipvia)
        self.actions.dropdown_contains(self.inv_dd_shipvia, self.inv_options_shipvia,create_invoice_test_data[""])

    def inv_shipping_to(self,create_invoice_test_data ):
        self.actions.wait_for_element(self.inv_dd_shipping_to)
        self.actions.scroll_to_the_element(self.inv_dd_shipping_to)
        self.actions.dropdown_contains(self.inv_dd_shipping_to, self.inv_options_shipping_to,create_invoice_test_data[""])

    def inv_invoice_date(self,create_invoice_test_data):
        self.actions.wait_for_element(self.inv_datep_invoice_date)
        self.actions.scroll_to_the_element(self.inv_datep_invoice_date)
        self.actions.select_date(self.inv_datep_invoice_date, self.inv_datepicker_month_class, self.inv_next_btn_class, self.inv_prev_btn_class, create_invoice_test_data["invoice_date"])

    def inv_shipping_date(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_datep_shipping_date)
        self.actions.scroll_to_the_element(self.inv_datep_shipping_date)
        self.actions.select_date(self.inv_datep_shipping_date, self.inv_datepicker_month_class, self.inv_next_btn_class, self.inv_prev_btn_class, create_invoice_test_data["shipping_date"])

    def inv_due_date(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_datep_due_date)
        self.actions.scroll_to_the_element(self.inv_datep_due_date)
        self.actions.select_date(self.inv_datep_due_date, self.inv_datepicker_month_class, self.inv_next_btn_class, self.inv_prev_btn_class, create_invoice_test_data["due_date"])

    def inv_click_additems(self):
        self.actions.wait_for_element(self.inv_btn_add_items)
        self.actions.scroll_to_the_element(self.inv_btn_add_items)
        self.actions.click(self.inv_btn_add_items)

    def inv_select_productservice(self,create_invoice_test_data ):
        self.actions.wait_for_element(self.inv_dd_select_product)
        self.actions.scroll_to_the_element(self.inv_dd_select_product)
        self.actions.dropdown_equals(self.inv_dd_select_product, self.inv_options_select_productservice, create_invoice_test_data["product_service_name"])

    def inv_select_multiple_productservice(self, create_invoice_test_data):
        product_list = create_invoice_test_data["product_service_name_multiple"]
        qty_list = create_invoice_test_data["quantity_multiple"]
        rate_list = create_invoice_test_data["rate_per_unit_multiple"]

        for index, (product, qty, rate) in enumerate(zip(product_list, qty_list, rate_list)):
            self.actions.wait_for_element(self.inv_dd_select_product)
            print("clicked")
            self.actions.scroll_to_the_element(self.inv_dd_select_product)
            self.actions.dropdown_equals(self.inv_dd_select_product, self.inv_options_select_productservice, product)

            self.actions.wait_for_element(self.inv_inp_quanitiy)
            self.actions.scroll_to_the_element(self.inv_inp_quanitiy)
            time.sleep(2)  # consider replacing this with a better wait if needed
            self.actions.clear_text(self.inv_inp_quanitiy)
            self.actions.send_keys(self.inv_inp_quanitiy, qty)

            self.actions.wait_for_element(self.inv_inp_rate_per_unit)
            self.actions.scroll_to_the_element(self.inv_inp_rate_per_unit)
            self.actions.clear_text(self.inv_inp_rate_per_unit)
            self.actions.send_keys(self.inv_inp_rate_per_unit, rate)

            self.actions.wait_for_element(self.inv_btn_prod_save)
            self.actions.scroll_to_the_element(self.inv_btn_prod_save)
            self.actions.click(self.inv_btn_prod_save)

            # Add next item if there are more
            if index < len(product_list) - 1:
                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located((By.CLASS_NAME, "modal"))
                )
                self.actions.click(self.inv_btn_add_items)
                time.sleep(1)

    def inv_select_productservice_no_rate_update(self, create_invoice_test_data):
        product_list = create_invoice_test_data["product_service_name_multiple"]
        qty_list = create_invoice_test_data["quantity_multiple"]

        for index, (product, qty) in enumerate(zip(product_list, qty_list)):
            self.actions.wait_for_element(self.inv_dd_select_product)
            print("clicked")
            self.actions.scroll_to_the_element(self.inv_dd_select_product)
            self.actions.dropdown_equals(self.inv_dd_select_product, self.inv_options_select_productservice, product)

            self.actions.wait_for_element(self.inv_inp_quanitiy)
            self.actions.scroll_to_the_element(self.inv_inp_quanitiy)
            time.sleep(2)  # consider replacing this with a better wait if needed
            self.actions.clear_text(self.inv_inp_quanitiy)
            self.actions.send_keys(self.inv_inp_quanitiy, qty)

            self.actions.wait_for_element(self.inv_btn_prod_save)
            self.actions.scroll_to_the_element(self.inv_btn_prod_save)
            self.actions.click(self.inv_btn_prod_save)

            # Add next item if there are more
            if index < len(product_list) - 1:
                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located((By.CLASS_NAME, "modal"))
                )
                self.actions.click(self.inv_btn_add_items)
                time.sleep(1)

    def inv_product_quantity(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_inp_quanitiy)
        self.actions.scroll_to_the_element(self.inv_inp_quanitiy)
        time.sleep(2)
        self.actions.clear_text(self.inv_inp_quanitiy)
        self.actions.send_keys(self.inv_inp_quanitiy, create_invoice_test_data["quantity"])

    def inv_product_rateperunit(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_inp_rate_per_unit)
        self.actions.scroll_to_the_element(self.inv_inp_rate_per_unit)
        self.actions.send_keys(self.inv_inp_rate_per_unit, create_invoice_test_data["rate_per_unit"])

    def inv_selectproduct_cancel(self):
        self.actions.wait_for_element(self.inv_btn_prod_cancel)
        self.actions.scroll_to_the_element(self.inv_btn_prod_cancel)
        self.actions.click(self.inv_btn_prod_cancel)

    def inv_selecproduct_save(self):
        self.actions.wait_for_element(self.inv_btn_prod_save)
        self.actions.scroll_to_the_element(self.inv_btn_prod_save)
        self.actions.click(self.inv_btn_prod_save)

    def inv_message_on_invoice(self, create_invoice_test_data):
        self.actions.wait_for_element(self.inv_inp_message_on_invoice)
        self.actions.scroll_to_the_element(self.inv_inp_message_on_invoice)
        self.actions.send_keys(self.inv_inp_message_on_invoice, create_invoice_test_data["message_on_invoice"])

    def inv_subtotal(self):
        self.actions.wait_for_element(self.inv_txt_sub_total)
        self.actions.scroll_to_the_element(self.inv_txt_sub_total)
        invoice_subtotal = self.actions.get_text(self.inv_txt_sub_total)
        time.sleep(2)
        print(f"subtotal: {invoice_subtotal}")

    def inv_tax(self):
        self.actions.wait_for_element(self.inv_txt_tax)
        self.actions.scroll_to_the_element(self.inv_txt_tax)
        invoice_tax = self.actions.get_text(self.inv_txt_tax)
        print(f"tax:{invoice_tax}")

    def inv_amount_received(self):
        self.actions.wait_for_element(self.inv_txt_tax)
        self.actions.scroll_to_the_element(self.inv_txt_tax)
        invoice_amount_received = self.actions.get_text(self.inv_txt_tax)
        print(f"amount received: {invoice_amount_received}")

    def inv_balance(self):
        self.actions.wait_for_element(self.inv_txt_balance)
        self.actions.scroll_to_the_element(self.inv_txt_balance)
        invoice_balance= self.actions.get_text(self.inv_txt_balance)
        print(f"balance: {invoice_balance}")

    def inv_cancel(self):
        self.actions.wait_for_element(self.inv_btn_cancel)
        self.actions.scroll_to_the_element(self.inv_btn_cancel)
        self.actions.click(self.inv_btn_cancel)

    def inv_clear(self):
        self.actions.wait_for_element(self.inv_btn_clear)
        self.actions.scroll_to_the_element(self.inv_btn_clear)
        self.actions.click(self.inv_btn_clear)

    def inv_save_and_close(self):
        self.actions.wait_for_element(self.inv_btn_save_close)
        self.actions.scroll_to_the_element(self.inv_btn_save_close)
        self.actions.click(self.inv_btn_save_close)

    def inv_save_and_new(self):
        self.actions.wait_for_element(self.inv_btn_save_new)
        self.actions.scroll_to_the_element(self.inv_btn_save_new)
        self.actions.click(self.inv_btn_save_new)


    def verify_total_matches_with_subtotal(self):
        total_sum = 0.0


        self.actions.wait_for_element(self.inv_added_productservice_total)
        total_elements = self.driver.find_elements(*self.inv_added_productservice_total)

        if total_elements:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", total_elements[0])

        for elements in total_elements:
            text = elements.text.strip()
            if text:  # Check if text is not empty
                clean_text = text.replace('₹', '').replace(',', '').strip()  # Remove currency symbol and commas
                try:
                    total_sum += float(clean_text)
                except ValueError:
                    print(f"Warning: Could not convert '{text}' to float.")


        print(f"Total Sum of the 'Total' column: ₹ {total_sum:.2f}")

        # SubTotal on UI
        self.actions.wait_for_element(self.inv_txt_sub_total)
        self.actions.scroll_to_the_element(self.inv_txt_sub_total)
        invoice_subtotal = self.actions.get_text(self.inv_txt_sub_total)
        invoice_subtotal_text = invoice_subtotal.strip()
        invoice_subtotal_clean = invoice_subtotal_text.replace('₹', '').replace(',', '').strip()

        try:
            subtotal_value = float(invoice_subtotal_clean)
        except ValueError:
            raise Exception(f"Subtotal value '{invoice_subtotal_text}' is not a valid number.")

        print(f"Subtotal shown on UI: ₹ {subtotal_value:.2f}")

        # Tax on UI
        self.actions.wait_for_element(self.inv_txt_tax)
        self.actions.scroll_to_the_element(self.inv_txt_tax)
        invoice_totaltax = self.actions.get_text(self.inv_txt_tax)
        invoice_totatax_text = invoice_totaltax.strip()
        invoice_totaltax_clean = invoice_totatax_text.replace('₹', '').replace(',', '').strip()

        try:
            totaltax_value = float(invoice_totaltax_clean)
        except ValueError:
            raise Exception(f"Subtotal value '{invoice_totatax_text}' is not a valid number.")

        print(f"TaxTotal shown on UI: ₹ {totaltax_value:.2f}")

        # subtotal + tax
        expected_total_UI = subtotal_value + totaltax_value
        print(f"TaxTotal shown on UI: ₹ {expected_total_UI:.2f}")

        # Assertion to verify Total Sum matches the displayed Subtotal
        assert abs(total_sum - expected_total_UI) < 0.01, (
            f"Mismatch: Calculated Total ₹{total_sum:.2f} != Subtotal ₹{subtotal_value:.2f} + Tax ₹{totaltax_value:.2f}"
        )


    def verify_amount_of_each_product_with_rate_and_quantity(self):
        # product quantity
        self.actions.wait_for_element(self.inv_added_productservice_qty)
        self.actions.scroll_to_the_element(self.inv_added_productservice_qty)
        product_quantity = self.actions.get_text(self.inv_added_productservice_qty)
        number_str = ''
        for char in product_quantity:
            if char.isdigit() or char == '.':  # also allow decimal
                number_str += char
            else:
                break

        if number_str:
            quantity = float(number_str)  # float in case quantity is decimal
            print(f"Quantity: {quantity:.2f}")
        else:
            raise Exception("No valid number found in the product quantity string.")

        # product rate
        self.actions.wait_for_element(self.inv_added_productservice_rate)
        self.actions.scroll_to_the_element(self.inv_added_productservice_rate)
        product_rate_UI = self.actions.get_text(self.inv_added_productservice_rate)
        product_rate_clean = product_rate_UI.replace('₹', '').replace(',', '').strip()
        try:
            product_rate_f = float(product_rate_clean)
        except ValueError:
            raise Exception(f"Product rate '{product_rate_UI}' is not a valid number.")
        print(f"Product Rate: ₹{product_rate_f:.2f}")

        # Calculated product amount
        calculated_product_amount = quantity * product_rate_f

        # product amount on UI
        self.actions.wait_for_element(self.inv_added_productservice_amount)
        self.actions.scroll_to_the_element(self.inv_added_productservice_amount)
        product_amount_UI = self.actions.get_text(self.inv_added_productservice_amount)
        product_amount_clean = product_amount_UI.replace('₹', '').replace(',', '').strip()
        try:
            product_amount_f = float(product_amount_clean)
        except ValueError:
            raise Exception(f"Product amount '{product_amount_UI}' is not a valid number.")

        # Final assertion
        assert abs(calculated_product_amount - product_amount_f) < 0.01, (
            f"Mismatch: Calculated = ₹{calculated_product_amount:.2f}, "
            f"UI = ₹{product_amount_f:.2f}, Qty = {quantity:.2f}, Rate = ₹{product_rate_f:.2f}"
        )

    def verify_total_matches_with_sum_of_productamount_and_tax(self):
        # product amount on UI
        self.actions.wait_for_element(self.inv_added_productservice_amount)
        self.actions.scroll_to_the_element(self.inv_added_productservice_amount)
        product_amount_UI = self.actions.get_text(self.inv_added_productservice_amount)
        product_amount_clean = product_amount_UI.replace('₹', '').replace(',', '').strip()
        try:
            product_amount_f = float(product_amount_clean)
        except ValueError:
            raise Exception(f"Product amount '{product_amount_UI}' is not a valid number.")

        print(f"Product Amount {product_amount_f}")

        # product tax on UI
        self.actions.wait_for_element(self.inv_added_productservice_tax)
        self.actions.scroll_to_the_element(self.inv_added_productservice_tax)
        product_tax_UI = self.actions.get_text(self.inv_added_productservice_tax)
        product_tax_clean = product_tax_UI.replace('₹', '').replace(',', '').strip()
        try:
            product_tax_f = float(product_tax_clean)
        except ValueError:
            raise Exception(f"Product tax '{product_tax_UI}' is not a valid number.")

        print(f"Product Amount: {product_tax_f}")

        # total on UI
        self.actions.wait_for_element(self.inv_added_productservice_total)
        self.actions.scroll_to_the_element(self.inv_added_productservice_total)
        product_total_UI = self.actions.get_text(self.inv_added_productservice_total)
        product_total_clean = product_total_UI.replace('₹', '').replace(',', '').strip()
        try:
            product_total_f = float(product_total_clean)
        except ValueError:
            raise Exception(f"Product tax '{product_total_UI}' is not a valid number.")

        print(f"Tax: {product_total_f}")

        #calculate sum of product amount and tax
        total = product_amount_f + product_tax_f
        print(f"Total Amount: {product_total_f}")

        assert abs(product_total_f - total) < 0.01, (
            f"Mismatch: Calculated Total ₹{total:.2f} != Product amount ₹{product_amount_f:.2f} + Tax ₹{product_tax_f:.2f}"
        )


    def verify_created_invoice_displayed_in_invoice_list(self):
        #self.actions.wait_for_element(self.inv_invoice_no)
        #self.actions.scroll_to_the_element(self.inv_invoice_no)
        #invoice_no = self.actions.get_text(self.inv_invoice_no)

        name_found = False
        while True:
            # Wait until the customer list is visible
            #wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']//table/tbody//a")))
            self.actions.wait_for_element(self.inv_list_invno)
            # Get list of customer elements
            invoice_no_list = self.driver.find_elements(*self.inv_list_invno)

            # Scroll to each customer entry
            for invoiceNo in invoice_no_list:
                #scroll_to_element(driver, customer)
                if invoiceNo.text.strip().lower() == self.invoice_no.strip().lower():
                    print(f"Match found: {self.invoice_no}")
                    name_found = True
                    break

            if name_found:
                break

            # Try to find the Next button
            #wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='>']")))
            self.actions.wait_for_element(self.btn_nxt_customerlist)
            next_buttons = self.driver.find_elements(*self.btn_nxt_customerlist)

            if next_buttons:
                #scroll_to_element(driver, next_buttons[0])
                next_buttons[0].click()
                time.sleep(2)  # Give time for next page to load
            else:
                print("Name not found in any pages.")
                break

    def inv_x_button(self):
        self.actions.wait_for_element(self.inv_m_btn_x)
        self.actions.scroll_to_the_element(self.inv_m_btn_x)
        self.actions.click(self.inv_m_btn_x)
