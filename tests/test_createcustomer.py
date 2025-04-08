import os
from pages.create_customer import CreateCustomer
#from dotenv import load_dotenv
from tests.conftest import setup, test_data


def test_ete_create_customer(setup, test_data):
    driver = setup
    create_customer = CreateCustomer(driver)

    create_customer.cust_submodsales()
    create_customer.cust_submodCustomer()
    create_customer.cust_newCustomer()
    create_customer.cust_title(test_data)
    create_customer.cust_firstname(test_data)
    create_customer.cust_middlename(test_data)
    create_customer.cust_lastname(test_data)
    #create_customer.cust_companyname(test_data)
    #create_customer.cust_displayname(test_data)
    create_customer.cust_storedisplayname()
    create_customer.cust_email(test_data)
    create_customer.cust_phonenumcountry(test_data)
    create_customer.cust_phonenumber(test_data)
    create_customer.cust_mobilenumber(test_data)
    create_customer.cust_fax(test_data)
    create_customer.cust_other(test_data)
    create_customer.cust_nametoprintoncheck(test_data)
    create_customer.cust_gsttreatment(test_data)
    create_customer.cust_gstnumber(test_data)
    create_customer.cust_billing(test_data)
    #create_customer.cust_billingcountry(test_data)
    #create_customer.cust_billingstate(test_data)
    #create_customer.cust_billingcity(test_data)
    #create_customer.cust_billingzip(test_data)
    create_customer.cust_shipping(test_data)
    #create_customer.cust_shippingcountry(test_data)
    #create_customer.cust_shippingstate(test_data)
    #create_customer.cust_shippingcity(test_data)
    #create_customer.cust_shippingzip(test_data)
    create_customer.cust_note(test_data)
    create_customer.cust_customertype(test_data)
    create_customer.cust_preferreddeliverymethod(test_data)
    create_customer.cust_preferredpaymentmethod(test_data)
    create_customer.cust_creditterms(test_data)
    create_customer.cust_saveandclose()
    create_customer.cust_customer_saved_successfully(driver)





