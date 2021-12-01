from a_entities.customer import Customer
from b_data_access_layer.imp_customer_dao import CustomerDAOImp

# Created an instance of the class "CustomerDAOImp" and "CustomerPostgresDAO" to be able to use the methods defined
# inside each module.
customer_imp = CustomerDAOImp()
# customer_postgres_dao = CustomerPostgresDAO()

# Create test customer objects until they can be handled through a database.
# Created a customer through the "Customer" class, passing in the arguments needed. The customer id is set for zero
# right now so that it can be turned into a unique identifier later.
customer_postgres = Customer("Jody", "Mills", 0, 0)


def test_create_customer_happy():
    # Stored the information retrieved from the "create_customer" method.
    created_customer = customer_imp.create_customer(customer_postgres)
    # Asserts that, out of the customer information retrieved and stored in "created_one" the customer_id variable
    # is not at 0.
    assert created_customer.customer_id != 0


def test_get_customer_information_happy():
    # Using the "customer_imp" object to use the class method "get_customer_information". Passed in our premade customer
    # which is at customer id of 1 to see if our test works.
    customer_info: Customer = customer_imp.get_customer_information(1)
    assert customer_info.customer_id == 1


def test_update_customer_information_happy():
    update_info_cust = Customer("Changed by", "update customer method.", 1, 2)
    updated_customer: Customer = customer_imp.update_customer_information(update_info_cust)
    assert updated_customer.last_name == "update customer method."


def test_view_all_customers_happy():
    get_customer_list = customer_imp.view_all_customers()
    assert len(get_customer_list) >= 1


def test_delete_customer_happy():
    deleted_customer = customer_imp.delete_customer(1)
    assert deleted_customer


# These are unit tests because they test the behavior of a single method.