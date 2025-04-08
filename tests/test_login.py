import os

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.login_page import LoginPage
from dotenv import load_dotenv
from tests.confest2 import setup, test_data


load_dotenv()

valid_username = os.getenv('VALIDLOGINUSERNAME').split(',')
valid_password = os.getenv('VALIDLOGINPASSWORD').split(',')
invalid_username =os.getenv('INVALIDUSERNAME').split(',')
invalid_password =os.getenv('INVALIDLOGINPASSWORD').split(',')

#expectedmessage = test_data['expectederrormsg']

#test with valid credentials and user should navigate to dashboard screen
@pytest.mark.parametrize("username, password", zip(valid_username, valid_password))
def test_valid_login(setup, test_data, username, password):
   # expectedmessage = test_data['expectederrormsg']
    driver = setup
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_loginbutton()
    login_page.success_login(test_data)

#test with invalid credentials and validation should be displayed
@pytest.mark.parametrize("username, password", zip(invalid_username, invalid_password))
def test_invalid_login(setup, test_data,username, password ):
    driver= setup
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_loginbutton()
    login_page.failed_login(test_data)

#test with blank username and click on login button
def test_username_validation(setup, test_data):
    driver = setup
    login_page = LoginPage(driver)
    login_page.enter_password(valid_password[0])
    login_page.click_loginbutton()
    login_page.username_blank_validation(test_data)

#test with blank password and click on login button
def test_password_validation(setup,test_data):
    driver = setup
    login_page = LoginPage(driver)
    login_page.enter_username(valid_username[0])
    login_page.click_loginbutton()
    login_page.password_blank_validation(test_data)

#test with blank user and password and click on login button
def test_usernasmepassword_validation(setup,test_data):
    driver = setup
    login_page = LoginPage(driver)
    login_page.click_loginbutton()
    login_page.username_blank_validation(test_data)
    login_page.password_blank_validation(test_data)















