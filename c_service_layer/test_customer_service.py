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
another_customer = Customer("Charlie", "Bradbury", 1, 5)
# This customer has unique customer id, but the same bank account id as an already created customer.
update_customer = Customer("Lucifer", "Morningstar", 5, 1)


# We use this test to make sure we can't get a duplicate account id with each created object.
def test_validate_create_customer_sad():
    try:
        customer_service.service_create_customer(another_customer)
        assert False
    except DuplicateCustomerIdException as e:
        assert str(e) == "This account number is already assigned!"



# We use this test to make sure customers don't get duplicate bank accounts.
def test_validate_update_customer_information_sad():
    try:
        customer_service.service_update_customer_information(update_customer)
        assert False
    except DuplicateBankAccountException as b:
        assert str(b) == "A customer already has this bank account!"



# We use this test to make sure customers can't be deleted twice.
def test_validate_already_deleted_sad():
    try:
        customer_service.service_delete_customer(update_customer)
        assert False
    except AlreadyDeletedException as d:
        assert str(d) == "This customer doesn't exist!"
    # Stop deletion of customer if bank account has not been deleted.


# These are not unit tests because they use the behavior of more than one method to test the information.