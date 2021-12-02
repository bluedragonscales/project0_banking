from a_entities import customer
from a_entities.customer import Customer
from b_data_access_layer.imp_customer_dao import CustomerDAOImp
from c_service_layer.custom_exceptions import *
from c_service_layer.imp_customer_service import CustomerServiceImp

# Created the DAO object to bring its implementation to these tests.
customer_imp_two = CustomerDAOImp()
# Injected the DAO object into the service object just like what happened in the "customer_service_imp"
# module.
customer_service = CustomerServiceImp(customer_imp_two)


# Objects created to use for testing purposes.
# This customer has same customer id as an already created customer, but different bank account.
another_customer = Customer("Charlie", "Bradbury", 2)
update_customer = Customer("Charlie", "Winchester", 2)
wrong_cust_info = Customer("Test", "Wrong", "6")
cust_to_delete = Customer("Mary", "Winchester", 4)
duplicate_customer = Customer("Charlie", "Bradbury", 2)


def test_validate_create_customer_sad():
    try:
        customer_service.service_create_customer(wrong_cust_info)
        assert False
    except WrongInformationException as w:
        assert str(w) == "Incorrect information entered from front end."

# We use this test to make sure a customer can't be deleted twice.
def test_cust_already_created_sad():
    try:
        customer_service.service_create_customer(duplicate_customer)
    except DuplicateCustomerException as d:
        assert str(d) == "This customer was already created."



# We use this test to make sure customers don't get duplicate bank accounts.
def test_validate_update_customer_information_sad():
    try:
        customer_service.service_update_customer_information(update_customer)
    except DuplicateInformationException as b:
        assert str(b) == "This information is already the same."



# We use this test to make sure customers can't be deleted twice.
def test_validate_already_deleted_sad():
    try:
        customer_service.service_delete_customer(cust_to_delete.customer_id)
    except AlreadyDeletedException as d:
        assert str(d) == "This customer doesn't exist!"
    # Stop deletion of customer if bank account has not been deleted.


# These are not unit tests because they use the behavior of more than one method to test the information.