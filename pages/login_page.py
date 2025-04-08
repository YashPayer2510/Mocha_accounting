from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

from actions.actions import Actions
from tests.confest2 import test_data


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)


    login_username = (By.XPATH,"//input[@id='email']")
    login_password = (By.XPATH,"//input[@placeholder='12**********']" )
    login_button = (By.XPATH,"//button[@type='submit']")
    success_msg = (By.XPATH,"//li[@class='breadcrumb-item active text-zoom']")
    failed_msg = (By.XPATH,"//div[@class='toast-body sc-iNGGcK fMdlTo']")
    logged_out_profile = (By.XPATH,"//a[@class='nav-link py-0']//img[@class='avatar-img']")
    logged_out_button =(By.XPATH,"//a[normalize-space()='Logout']")
    username_validation =(By.XPATH,"//div[normalize-space()='Email is required.']")
    password_validation=(By.XPATH,"//div[normalize-space()='Password is required']")

    def enter_username(self,username):
        self.actions.wait_for_element(self.login_username)
        self.actions.send_keys(self.login_username,username)


    def enter_password(self, password):
        self.actions.wait_for_element(self.login_password)
        self.actions.send_keys(self.login_password, password)

    def click_loginbutton(self):
        self.actions.wait_for_element(self.login_button)
        self.actions.click(self.login_button)

    def success_login(self,test_data):
         self.actions.wait_for_element(self.success_msg)
         s_e_msg = test_data["successflow"]
         s_a_msg = self.actions.get_text(self.success_msg)
         assert s_e_msg == s_a_msg , "login failed"

    def failed_login(self, test_data):
        self.actions.wait_for_element(self.failed_msg)
        f_e_msg = test_data["expectederrormsg"]
        f_a_msg = self.actions.get_text(self.failed_msg)
        assert f_e_msg == f_a_msg, "login failed"

    def click_logged_out_profile(self):
        self.actions.wait_for_element(self.logged_out_profile)
        self.actions.click(self.logged_out_profile)

    def click_logged_out_button(self):
        self.actions.wait_for_element(self.logged_out_button)
        self.actions.click(self.logged_out_button)

    def username_blank_validation(self, test_data):
        self.actions.wait_for_element(self.username_validation)
        expected_u_validation= test_data["expected_username_validation"]
        actual_u_validation= self.actions.get_text(self.username_validation)
        assert expected_u_validation == actual_u_validation, "login failed"

    def password_blank_validation(self, test_data):
        self.actions.wait_for_element(self.password_validation)
        expected_p_validation = test_data["expected_password_validation"]
        actual_p_validation = self.actions.get_text(self.password_validation)
        assert expected_p_validation == actual_p_validation, "login failed"

