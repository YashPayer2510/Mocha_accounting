import time
import datetime

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.actions import Actions


class CreateProdouct_Service:
    def __init__(self, driver):
        self.expected_name = None
        self.driver = driver
        self.actions = Actions(driver)
        self.wait = WebDriverWait(driver, 4)

    create_prod_serv_items_module = (By.XPATH,"//img[@src='/svgs/items.svg']")
    create_prod_serv_product_and_service_sub_module = (By.XPATH,"//a[normalize-space()='Products and Services']")
    create_prod_serv_new_product = (By.XPATH,"//button[normalize-space()='New']")
    create_prod_serv_product_name_inp = (By.XPATH,"//input[@name='name']")
    create_prod_serv_product_type_dd = (By.XPATH,"//label[text()='Type *']/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    create_prod_serv_options_product_type = (By.XPATH,"//div[contains(@id, 'option')]")
    create_prod_serv_sku_inp = (By.XPATH,"//input[@name='sku']")
    create_prod_serv_base_unit_dd = (By.XPATH,"//label[text()='Base Unit']/following-sibling::div//input[contains(@id, 'react-select')]")
    create_prod_serv_options_base_unit = (By.XPATH, "//div[contains(@id, 'option')]")
    create_prod_serv_secondary_unit_hyperlink = (By.XPATH,"//span[normalize-space()='Add Secondary Unit']")
    create_prod_serv_secondary_unit_dd = (By.XPATH,"//label[text()='Secondary Unit *']/ancestor::div[contains(@class, 'mb-3')]//input[contains(@id, 'react-select')]")
    create_prod_serv_options_secondary_unit = (By.XPATH, "//div[contains(@id, 'option')]")
    create_prod_serv_conversion_rates = (By.XPATH,"//input[@class='col-2 form-control common-form-input w-auto d-inline no-spinner']")
    create_prod_serv_close_btn_unit_conversion= (By.XPATH,"//div[@class='modal-header sc-kOHTFB ivaBOY']//button[@aria-label='Close']")
    create_prod_serv_save_btn_unit_conversion= (By.XPATH,"//button[@type='secondary']")
    create_prod_serv_hsnsac_dd = (By.XPATH,"//label[contains(text(), 'HSN/SAC')]/following-sibling::div//input[contains(@id, 'react-select') and @type='text']")
    create_prod_serv_options_hsnsac = (By.XPATH,"//div[contains(@id, 'option')]")
    create_prod_serv_category_dd = (By.XPATH,"//label[text()='Category']/following-sibling::div//input[contains(@id, 'react-select')]")
    create_prod_serv_options_category = (By.XPATH,"//div[contains(@id, 'option')]")
    create_prod_serv_description_inp = (By.XPATH,"//textarea[@name='description']")
    create_prod_serv_inventory_account_dd = (By.XPATH, "//label[text()='Inventory Account *']/following-sibling::div//input[contains(@id, 'react-select')]")
    create_prod_serv_options_inventory_account = (By.XPATH, "//div[contains(@id, 'option')]")
    create_prod_serv_initial_qty_onhand_inp = (By.XPATH,"//input[@name='quantity']")
    create_prod_serv_recorder_point_inp = (By.XPATH, "//input[@name='reorder_point']")
    create_prod_serv_opening_stock_price_inp= (By.XPATH,"//input[@name='opening_stock_price']")
    create_prod_serv_as_of_date = (By.XPATH, "//input[@name='as_of_date']")
    create_prod_serv_datepicker_current_month_class = (By.CLASS_NAME, "react-datepicker__current-month")
    create_prod_serv_next_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--next")
    create_prod_serv_prev_btn_class = (By.CLASS_NAME, "react-datepicker__navigation--previous")
    create_prod_serv_sale_info_chk_bx=(By.XPATH,"//input[@name='sales_info']")
    create_prod_serv_income_account_dd = (By.XPATH,"//label[contains(text(),'Income Account')]/following-sibling::div//input[contains(@id, 'react-select')]")
    create_prod_serv_options_income_account = (By.XPATH, "//div[contains(@id, 'option')]")
    create_prod_serv_sale_price_inp= (By.XPATH,"//input[@name='price']")
    create_prod_serv_purchase_info_chk_bx = (By.XPATH, "//input[@name='purchase_info']")
    create_prod_serv_expense_account_dd = (By.XPATH, "//label[contains(text(),'Expense Account')]/following-sibling::div//input[contains(@id, 'react-select')]")
    create_prod_serv_options_expense_account = (By.XPATH, "//div[contains(@id, 'option')]")
    create_prod_serv_cost_price_inp= (By.XPATH,"//input[@name='cost_price']")
    create_prod_serv_btn_save_close = (By.XPATH, "//button[normalize-space()='Save and Close']")
    create_prod_serv_btn_save_new = (By.XPATH, "//button[normalize-space()='Save and New']")
    create_prod_serv_btn_cancel = (By.XPATH, "//div[@class='d-flex justify-content-between align-items-center flex-wrap']//div[1]//button[1]")
    create_prod_serv_btn_clear = (By.XPATH, "//div[@class='d-flex justify-content-between align-items-center flex-wrap']//div[1]//button[2]")
    create_prod_serv_m_btn_x = (By.XPATH, "//div[contains(@class, 'toast') and contains(@class, 'show')]//button[contains(@class, 'btn-close')]")

    create_prod_serv_product_list = (By.XPATH,"//table//tr//td[1]//td")
    create_prod_serv_btn_nxt_product_list = (By.XPATH, "//a[normalize-space()='>']")


    def create_product_service_sales_module(self):
        self.actions.wait_for_element(self.create_prod_serv_items_module)
        self.actions.click(self.create_prod_serv_items_module)

    def create_product_service_submodule(self):
        self.actions.wait_for_element(self.create_prod_serv_product_and_service_sub_module)
        self.actions.click(self.create_prod_serv_product_and_service_sub_module)

    def create_product_service_new_btn(self):
        self.actions.wait_for_element(self.create_prod_serv_new_product)
        self.actions.click(self.create_prod_serv_new_product)

    def create_product_service_name(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_product_name_inp)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")  # e.g., 20250709_154500
        self.unique_product_name = f"{create_product_service_test_data['product/service_name']}_PN_{timestamp}"
        self.actions.send_keys(self.create_prod_serv_product_name_inp, self.unique_product_name)
        return self.unique_product_name

    def create_product_service_type_dd(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_product_type_dd)
        self.actions.scroll_to_the_element(self.create_prod_serv_product_type_dd)
        self.actions.dropdown_equals(self.create_prod_serv_product_type_dd, self.create_prod_serv_options_product_type, create_product_service_test_data["product/service_type"])

    def create_product_service_sku(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_sku_inp)
        self.actions.send_keys(self.create_prod_serv_sku_inp, create_product_service_test_data["product/service_name"])

    def create_product_service_base_unit_dd(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_base_unit_dd)
        self.actions.scroll_to_the_element(self.create_prod_serv_base_unit_dd)
        self.actions.click(self.create_prod_serv_base_unit_dd)
        self.actions.dropdown_contains(self.create_prod_serv_base_unit_dd, self.create_prod_serv_options_base_unit, create_product_service_test_data["product/service_base_unit"])

    def create_product_service_secondary_unit_dd(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_secondary_unit_dd)
        self.actions.scroll_to_the_element(self.create_prod_serv_secondary_unit_dd)
        self.actions.click(self.create_prod_serv_secondary_unit_dd)
        self.actions.dropdown_contains(self.create_prod_serv_secondary_unit_dd, self.create_prod_serv_options_secondary_unit, create_product_service_test_data["product/service_secondary_unit"])

    def create_product_service_add_secondary_unit_hyperlink(self):
        self.actions.wait_for_element(self.create_prod_serv_secondary_unit_hyperlink)
        self.actions.scroll_to_the_element(self.create_prod_serv_secondary_unit_hyperlink)
        self.actions.click(self.create_prod_serv_secondary_unit_hyperlink)

    def create_product_service_conversion_rate(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_conversion_rates)
        self.actions.send_keys(self.create_prod_serv_conversion_rates, create_product_service_test_data["product/service_conversion_rate"])

    def create_product_service_save_unit_conversion(self):
        self.actions.wait_for_element(self.create_prod_serv_save_btn_unit_conversion)
        self.actions.scroll_to_the_element(self.create_prod_serv_save_btn_unit_conversion)
        self.actions.click(self.create_prod_serv_save_btn_unit_conversion)

    def create_product_service_close_unit_conversion(self):
        self.actions.wait_for_element(self.create_prod_serv_close_btn_unit_conversion)
        self.actions.scroll_to_the_element(self.create_prod_serv_close_btn_unit_conversion)
        self.actions.click(self.create_prod_serv_save_btn_unit_conversion)


    def create_product_service_hsn_sac_dd(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_hsnsac_dd)
        self.actions.scroll_to_the_element(self.create_prod_serv_hsnsac_dd)
        self.actions.dropdown_contains(self.create_prod_serv_hsnsac_dd, self.create_prod_serv_options_hsnsac, create_product_service_test_data["product/service_base_unit"])

    def create_product_service_category_dd(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_category_dd)
        self.actions.scroll_to_the_element(self.create_prod_serv_category_dd)
        self.actions.dropdown_equals(self.create_prod_serv_category_dd, self.create_prod_serv_options_category, create_product_service_test_data["product/service_category"])

    def create_product_service_description(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_description_inp)
        self.actions.send_keys(self.create_prod_serv_description_inp, create_product_service_test_data["product/service_description"])

    def create_product_service_inventory_account_dd(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_inventory_account_dd)
        self.actions.scroll_to_the_element(self.create_prod_serv_inventory_account_dd)
        self.actions.dropdown_contains(self.create_prod_serv_inventory_account_dd, self.create_prod_serv_options_inventory_account, create_product_service_test_data["product/service_inventory_account"])

    def create_product_service_qty_on_hand(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_initial_qty_onhand_inp)
        self.actions.scroll_to_the_element(self.create_prod_serv_initial_qty_onhand_inp)
        self.actions.send_keys(self.create_prod_serv_initial_qty_onhand_inp, create_product_service_test_data["product/service_qty_on_hand"])

    def create_product_service_recorder_point(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_recorder_point_inp)
        self.actions.scroll_to_the_element(self.create_prod_serv_recorder_point_inp)
        self.actions.send_keys(self.create_prod_serv_recorder_point_inp, create_product_service_test_data["product/service_recorder_point"])

    def create_product_service_opening_stock_price(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_opening_stock_price_inp)
        self.actions.scroll_to_the_element(self.create_prod_serv_recorder_point_inp)
        self.actions.send_keys(self.create_prod_serv_opening_stock_price_inp, create_product_service_test_data["product/service_opening_stock_price"])

    def create_product_service_as_of_date(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_as_of_date)
        self.actions.scroll_to_the_element(self.create_prod_serv_as_of_date)
        self.actions.select_date(self.create_prod_serv_as_of_date,self.create_prod_serv_datepicker_current_month_class, self.create_prod_serv_next_btn_class, self.create_prod_serv_prev_btn_class, create_product_service_test_data["product/service_as_of_date"])

    def create_product_service_sale_info_chk_bx(self):
        self.actions.wait_for_element(self.create_prod_serv_sale_info_chk_bx)
        self.actions.scroll_to_the_element(self.create_prod_serv_sale_info_chk_bx)
        self.actions.click(self.create_prod_serv_sale_info_chk_bx)

    def create_product_service_income_account_dd(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_income_account_dd)
        self.actions.scroll_to_the_element(self.create_prod_serv_income_account_dd)
        self.actions.dropdown_contains(self.create_prod_serv_income_account_dd, self.create_prod_serv_options_income_account, create_product_service_test_data["product/service_income_account"])

    def create_product_service_sale_price(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_sale_price_inp)
        self.actions.scroll_to_the_element(self.create_prod_serv_sale_price_inp)
        self.actions.send_keys(self.create_prod_serv_sale_price_inp,create_product_service_test_data["product/service_sale_price"])

    def create_product_service_purchase_info_chk_bx(self):
        self.actions.wait_for_element(self.create_prod_serv_purchase_info_chk_bx)
        self.actions.scroll_to_the_element(self.create_prod_serv_purchase_info_chk_bx)
        self.actions.click(self.create_prod_serv_purchase_info_chk_bx)

    def create_product_service_expense_account_dd(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_expense_account_dd)
        self.actions.scroll_to_the_element(self.create_prod_serv_expense_account_dd)
        self.actions.dropdown_contains(self.create_prod_serv_expense_account_dd, self.create_prod_serv_options_expense_account, create_product_service_test_data["product/service_expense_account"])

    def create_product_service_cost_price(self, create_product_service_test_data):
        self.actions.wait_for_element(self.create_prod_serv_cost_price_inp)
        self.actions.scroll_to_the_element(self.create_prod_serv_cost_price_inp)
        self.actions.send_keys(self.create_prod_serv_cost_price_inp,create_product_service_test_data["product/service_cost_price"])


    def create_product_service_cancel(self):
        self.actions.scroll_to_the_element(self.create_prod_serv_btn_cancel)
        self.actions.wait_for_element(self.create_prod_serv_btn_cancel)
        self.actions.click(self.create_prod_serv_btn_cancel)

    def create_product_service_clear(self):
        self.actions.scroll_to_the_element(self.create_prod_serv_btn_clear)
        self.actions.wait_for_element(self.create_prod_serv_btn_clear)
        self.actions.click(self.create_prod_serv_btn_clear)


    def create_product_service_store_name(self):
        self.actions.wait_for_element(self.create_prod_serv_product_name_inp)
        self.expected_name = self.actions.get_attribute(self.create_prod_serv_product_name_inp)
        print(self.expected_name)
        time.sleep(2)

    def create_product_service_saveandclose(self):
        self.actions.scroll_to_the_element(self.create_prod_serv_btn_save_close)
        self.actions.wait_for_element(self.create_prod_serv_btn_save_close)
        self.actions.click(self.create_prod_serv_btn_save_close)
        time.sleep(3)

    def create_product_service_saveandnew(self):
        self.actions.scroll_to_the_element(self.create_prod_serv_btn_save_new)
        self.actions.wait_for_element(self.create_prod_serv_btn_save_new)
        self.actions.click(self.create_prod_serv_btn_save_new)
        time.sleep(3)

    def create_product_saved_successfully(self, create_product_service_test_data):
        expected_product = self.unique_product_name
        name_found = False

        while True:
            # Wait for the product list to be visible
            self.actions.wait_for_element(self.create_prod_serv_product_list)
            product_list = self.driver.find_elements(*self.create_prod_serv_product_list)

            # Loop through product names on current page
            for product in product_list:
                if product.text.strip().lower() == expected_product.strip().lower():
                    print(f"✅ Match found: {expected_product}")
                    name_found = True
                    break

            if name_found:
                break

            # Handle pagination
            try:
                self.actions.scroll_to_the_element(self.create_prod_serv_next_btn_class)
                next_btn = self.driver.find_element(*self.create_prod_serv_next_btn_class)
                class_attr = next_btn.get_attribute("class") or ""

                if "disabled" in class_attr or not next_btn.is_enabled():
                    print(f"ℹ️ Reached end of pagination. '{next_btn}' not found.")
                    break

                next_btn.click()

                # Wait until new content loads
                self.wait.until(EC.staleness_of(product_list[0]))
                self.wait.until(EC.presence_of_all_elements_located(self.create_prod_serv_product_list))

            except NoSuchElementException:
                print("✅ No 'Next' button found — assumed end of pagination.")
                break

            except Exception as e:
                print(f"❌ Unexpected error during pagination: {e}")
                break

        if not name_found:
            print(f"❌ Product '{expected_product}' not found.")


