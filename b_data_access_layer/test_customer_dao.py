# Module for all the tests of the customer dao methods.

from a_entities.customer import Customer
from b_data_access_layer.imp_customer_dao import CustomerDAOImp
from b_data_access_layer.postgres_customer_dao import CustomerPostgresDAO

# Created instances of classes "CustomerDAOImp" and "CustomerPostgresDAO" to use the methods defined inside each module.
imp_customer_dao = CustomerDAOImp()
postgres_customer_dao = CustomerPostgresDAO()

# Created a customer through the "Customer" class, passing in the arguments needed. The customer id is set for zero
# right now so that it can be turned into a unique identifier later.
customer_dao = Customer("Dean", "Winchester", 3)
customer_postgres = Customer("John", "Winchester", 0)


def test_create_customer_happy():
    # Stored the information retrieved from the "create_customer" method.
    created_customer = postgres_customer_dao.create_customer(customer_postgres)
    # Asserts that, out of the customer information retrieved and stored in "created_one" the customer_id variable
    # is not at 0.
    assert created_customer.customer_id != 0


def test_get_customer_information_happy():
    # Using the "customer_imp" object to use the class method "get_customer_information". Passed in our premade customer
    # which is at customer id of 1 to see if our test works.
    customer_info = postgres_customer_dao.get_customer_information(2)
    assert customer_info.customer_id == 2


def test_update_customer_information_happy():
    update_info_cust = Customer("Changed by", "update customer method.", 2)
    updated_customer = postgres_customer_dao.update_customer_information(2)
    assert updated_customer.last_name == "update customer method."


def test_view_all_customers_happy():
    get_customer_list = imp_customer_dao.view_all_customers()
    assert len(get_customer_list) >= 1


def test_delete_customer_happy():
    deleted_customer = imp_customer_dao.delete_customer(1)
    assert deleted_customer


# These are unit tests because they test the behavior of a single method.