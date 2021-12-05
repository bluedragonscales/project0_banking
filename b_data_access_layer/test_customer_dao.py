# Module for all the tests of the customer dao methods.

from a_entities.customer import Customer
from b_data_access_layer.postgres_customer_dao import CustomerPostgresDAO

# Created an instance of "CustomerPostgresDAO" to use the methods defined inside each module.
postgres_customer_dao = CustomerPostgresDAO()

# Created customer objects for testing.
customer_postgres = Customer("Dean", "Winchester", 0)
update_info_cust = Customer("Changed by", "update customer.", 7)



# Tests when you create a new customer, the customer_id will no longer be 0 because the database updates it.
def test_create_customer_happy():
    created_customer = postgres_customer_dao.create_customer(customer_postgres)
    assert created_customer.customer_id != 0



# Tests that when you pull up a customer's information, the correct information (the customer_id in this case) comes up.
def test_get_customer_information_happy():
    customer_info = postgres_customer_dao.get_customer_information(2)
    assert customer_info.customer_id == 2



# Tests that an attempt to update an already created customer's information will succeed.
def test_update_customer_information_happy():
    updated_customer = postgres_customer_dao.update_customer_information(update_info_cust)
    assert updated_customer.last_name == "update customer."



# Tests that list of all the created customers will appear when requested.
def test_view_all_customers_happy():
    get_customer_list = postgres_customer_dao.view_all_customers()
    assert len(get_customer_list) >= 1



# Tests that a customer will be deleted successfully when requested.
def test_delete_customer_happy():
    deleted_customer = postgres_customer_dao.delete_customer(17)
    assert deleted_customer