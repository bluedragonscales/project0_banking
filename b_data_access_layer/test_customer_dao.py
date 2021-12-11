# We use the DAO layer tests to test the implemented methods are working properly when they are passed in the correct
# information. These are called "happy-path" tests.

# This import gives us access to the customer object blue print which we use to create some test objects.
from a_entities.customer import Customer
# This import gives us access to the implemented DAO methods so that we can call them and test them.
from b_data_access_layer.postgres_customer_dao import CustomerPostgresDAO

# Created an instance of the class "CustomerPostgresDAO" and stored it in a variable called "postgres_customer_dao" to
# be able to call the methods defined inside the postgres_customer_dao module which was imported above. These methods
# require an instance of the class to be called because they are not static methods.
postgres_customer_dao = CustomerPostgresDAO()


# Created customer objects for testing purposes.
customer_postgres = Customer("Dean", "Winchester", 0)
update_info_cust = Customer("Changed by", "update method", 7)



# This is the happy path test for creating a new customer. The instance called "postgres_customer_dao" is used to call
# the "create_customer()" method and passes in the customer object argument like the method asks for. The returned
# customer object is then stored in a variable called "created_cust" and the test asserts that the customer object
# stored inside has a customer_id value that is no longer at zero (because postgres changes it to the default serial
# number).
def test_create_customer_happy():
    created_cust = postgres_customer_dao.create_customer(customer_postgres)
    assert created_cust.customer_id != 0



# This is the happy path test for looking up a specific customer's information. The instance "postgres_customer_dao" is
# used to call the "get_customer_information()" method and one of the customer's id numbers is passed into the parameter
# as required. The customer object that is returned is stored in the variable container "customer_info". Then the test
# asserts that the customer_id that was passed into the method is the same as the customer_id that gets spat out.
def test_get_customer_information_happy():
    customer_info = postgres_customer_dao.get_customer_information(2)
    assert customer_info.customer_id == 2



# Tests that an attempt to update an already created customer's information will succeed.
def test_update_customer_information_happy():
    updated_customer = postgres_customer_dao.update_customer_information(update_info_cust)
    assert updated_customer.last_name == "update method"



# Tests that list of all the created customers will appear when requested.
def test_view_all_customers_happy():
    get_customer_list = postgres_customer_dao.view_all_customers()
    assert len(get_customer_list) >= 1



# Tests that a customer will be deleted successfully when requested.
def test_delete_customer_happy():
    deleted_customer = postgres_customer_dao.delete_customer(1)
    assert deleted_customer