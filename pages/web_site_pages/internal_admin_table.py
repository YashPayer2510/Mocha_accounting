import time

from selenium.webdriver.common.by import By

from actions.actions import Actions
from pages.web_site_pages.book_demo_page import Book_Demo_Flow

class InternalAdminTable:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)

    internal_admin_demo_login_email = (By.XPATH,"//input[@type = 'email']")
    internal_admin_demo_login_password  = (By.XPATH,"//input[@type = 'password']")
    internal_admin_demo_login_sign_in_btn = (By.XPATH,"//button[normalize-space()='Sign In']")
    internal_admin_demo_table_table_rows = (By.XPATH, "//table//tbody//tr")
    internal_admin_demo_table_sno_column = (By.XPATH, "//table//tr//td[1]")
    internal_admin_demo_table_email_column = (By.XPATH, "//table//tr//td[3]")
    internal_admin_demo_table_contact_column = (By.XPATH, "//table//tr//td[4]")
    internal_admin_demo_table_date_column = (By.XPATH, "//table//tr//td[5]")
    internal_admin_demo_table_time_column = (By.XPATH, "//table//tr//td[6]")
    internal_admin_demo_table_msg_column = (By.XPATH, "//table//tr//td[7]")
    internal_admin_demo_table_link_column = (By.XPATH, "//table//tr//td[8]")
    internal_admin_demo_table_status_column = (By.XPATH, "//table//tr//td[9]")
    internal_admin_demo_table_user_type_column = (By.XPATH, "//table//tr//td[10]")
    internal_admin_demo_table_reason_column = (By.XPATH, "//table//tr//td[11]")



    def internal_admin_demo_enter_enter_url(self, url):
        self.actions.navigate_to_url(url)


    def internal_admin_demo_enter_username(self,username):
        self.actions.wait_for_element(self.internal_admin_demo_login_email)
        self.actions.send_keys(self.internal_admin_demo_login_email,username)

    def internal_admin_demo_enter_password(self, password):
        self.actions.wait_for_element(self.internal_admin_demo_login_password)
        self.actions.send_keys(self.internal_admin_demo_login_password, password)

    def internal_admin_demo_click_sign_in_btn(self):
        self.actions.wait_for_element(self.internal_admin_demo_login_sign_in_btn)
        self.actions.click(self.internal_admin_demo_login_sign_in_btn)

    def verify_email_in_table(self, expected_email):
        self.actions.wait_for_element(self.internal_admin_demo_table_table_rows)

        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            rows = self.driver.find_elements(*self.internal_admin_demo_table_table_rows)

            for row in rows:
                email_text = row.find_element(By.XPATH, "./td[3]").text.strip()
                if expected_email == email_text:
                    print("Email found in admin table")
                    return

            # scroll window to load more rows
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break  # no more rows loading
            last_height = new_height

        raise AssertionError(f"Email '{expected_email}' not found in admin table after full scroll.")





