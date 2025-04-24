import logging
import os
from logging import Logger

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.login_page import LoginPage
from dotenv import load_dotenv
from tests.conftest import setup, login_test_data



logger = logging.getLogger(__name__)
load_dotenv()

valid_username = os.getenv('VALIDLOGINUSERNAME').split(',')
valid_password = os.getenv('VALIDLOGINPASSWORD').split(',')
invalid_username =os.getenv('INVALIDUSERNAME').split(',')
invalid_password =os.getenv('INVALIDLOGINPASSWORD').split(',')
invalid_format_username =os.getenv('INVALIDFORMATMAIL').split(',')

#expectedmessage = login_test_data['expectederrormsg']

#test with valid credentials and validation should be displayed
@pytest.mark.parametrize("username, password", zip(valid_username, valid_password))
def test_valid_login(setup, login_test_data, username, password):
   # expectedmessage = login_test_data['expectederrormsg']
    driver = setup
    login_page = LoginPage(driver)
    logger.info("Starting the test case for valid credentials")
    login_page.enter_username(username)
    logger.info("User enters the email-id")
    login_page.enter_password(password)
    logger.info("User enters the password")
    login_page.click_loginbutton()
    logger.info("User clicks on login button")
    login_page.success_login(login_test_data)
    logger.info("The test case passed")

#test with invalid credentials and validation should be displayed
@pytest.mark.parametrize("username", zip(invalid_username))
def test_invalid_email_login(setup, login_test_data,username):
    driver= setup
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    #login_page.enter_password(password)
    login_page.click_loginbutton()
    login_page.incorrect_email_validation(login_test_data)

@pytest.mark.parametrize("username, password", zip(valid_username, invalid_password))
def test_invalid_password_login(setup, login_test_data,username, password ):
    driver = setup
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_loginbutton()
    login_page.failed_login(login_test_data)


#test with blank username and click on login button
def test_blank_username_validation(setup, login_test_data):
    driver = setup
    login_page = LoginPage(driver)
    #login_page.enter_password(valid_password[0])
    login_page.click_username()
    login_page.click_loginbutton()
    login_page.username_blank_validation(login_test_data)

#test with blank password and click on login button
def test_blank_password_validation(setup,login_test_data):
    driver = setup
    login_page = LoginPage(driver)
    login_page.enter_username(valid_username[0])
    login_page.click_password()
    login_page.click_loginbutton()
    login_page.password_blank_validation(login_test_data)

#test with blank user and password and click on login button
def test_blank_usernamepassword_validation(setup,login_test_data):
    driver = setup
    login_page = LoginPage(driver)
    login_page.click_loginbutton()
    login_page.username_blank_validation(login_test_data)
    login_page.password_blank_validation(login_test_data)

@pytest.mark.parametrize("username", zip(invalid_format_username))
def test_invalid_email_validation(setup, login_test_data, username):
    driver = setup
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.click_loginbutton()
    login_page.invalid_email_validation(login_test_data)

















