import logging
import os
from pages.create_customer import CreateCustomer
#from dotenv import load_dotenv
from tests.conftest import setup, createcustomer_test_data
import allure
logger = logging.getLogger(__name__)

#@allure.feature('Create Customer')
#@allure.story('The customer should be created')
def test_ete_create_customer(setup, createcustomer_test_data):
    driver = setup
    create_customer = CreateCustomer(driver)

    #with allure.step('All field should be field with customers data'):
    for createcustomer_test_data in createcustomer_test_data:
            logger.info("Test case started")
            create_customer.cust_submodsales()
            create_customer.cust_submodCustomer()
            create_customer.cust_newCustomer()
            create_customer.cust_title(createcustomer_test_data)
            logger.info("Title entered")
            create_customer.cust_firstname(createcustomer_test_data)
            logger.info("firstname entered")
            create_customer.cust_middlename(createcustomer_test_data)
            logger.info("middlename entered")
            create_customer.cust_lastname(createcustomer_test_data)
            logger.info("lastname entered")
            #create_customer.cust_companyname(createcustomer_test_data)
            #create_customer.cust_displayname(createcustomer_test_data)
            create_customer.cust_storedisplayname()
            logger.info("display name stored")
            create_customer.cust_email(createcustomer_test_data)
            logger.info("email entered")
            create_customer.cust_phonenumcountry(createcustomer_test_data)
            logger.info("phonenumcountry selected")
            create_customer.cust_phonenumber(createcustomer_test_data)
            logger.info("phonenumber entered")
            create_customer.cust_mobilenumber(createcustomer_test_data)
            logger.info("mobilenumber entered")
            create_customer.cust_fax(createcustomer_test_data)
            logger.info("fax entered")
            create_customer.cust_other(createcustomer_test_data)
            logger.info("other entered")
            create_customer.cust_nametoprintoncheck(createcustomer_test_data)
            logger.info("nametoprintoncheck entered")
            create_customer.cust_gsttreatment(createcustomer_test_data)
            logger.info("gsttreatment selected")
            create_customer.cust_gstnumber(createcustomer_test_data)
            logger.info("gstnumber entered")
            create_customer.cust_billing(createcustomer_test_data)
            logger.info("billing entered")
            #create_customer.cust_billingcountry(createcustomer_test_data)
            #create_customer.cust_billingstate(createcustomer_test_data)
            #create_customer.cust_billingcity(createcustomer_test_data)
            #create_customer.cust_billingzip(createcustomer_test_data)
            create_customer.cust_shipping(createcustomer_test_data)
            logger.info("shipping entered")
            #create_customer.cust_shippingcountry(createcustomer_test_data)
            #create_customer.cust_shippingstate(createcustomer_test_data)
            #create_customer.cust_shippingcity(createcustomer_test_data)
            #create_customer.cust_shippingzip(createcustomer_test_data)
            create_customer.cust_note(createcustomer_test_data)
            logger.info("note entered")
            create_customer.cust_customertype(createcustomer_test_data)
            logger.info("customertype selected")
            create_customer.cust_preferreddeliverymethod(createcustomer_test_data)
            logger.info("preferreddeliverymethod selected")
            create_customer.cust_preferredpaymentmethod(createcustomer_test_data)
            logger.info("preferredpaymentmethod selected")
            create_customer.cust_creditterms(createcustomer_test_data)
            logger.info("creditterms selected")
            create_customer.cust_saveandclose()
            logger.info("saveandclose clicked")
            create_customer.cust_customer_saved_successfully(driver)
            logger.info("Test Case completed")





