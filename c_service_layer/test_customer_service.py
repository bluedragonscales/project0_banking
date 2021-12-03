from a_entities.customer import Customer
from b_data_access_layer.postgres_customer_dao import CustomerPostgresDAO
from c_service_layer.custom_exceptions import *
from c_service_layer.postgres_customer_service import CustomerPostgresService

# Created the postgres DAO and postgres service objects. Injected the DAO into the service layer.
postgres_customer_dao = CustomerPostgresDAO()
postgres_customer_service = CustomerPostgresService(postgres_customer_dao)

# Objects for testing:
wrong_cust_info = Customer(10, "Henderson", "10")
duplicate_customer = Customer("Sam", "Winchester", 7)
update_customer = Customer("Dean", "Winchester", 10)


# We use this test to make sure someone on the front end API doesn't accidentally enter a string where a number is
# required or vise versa.
def test_validate_create_customer_sad():
    try:
        postgres_customer_service.service_create_customer(wrong_cust_info)
    except WrongInformationException as w:
        assert str(w) == "Incorrect information entered from front end."



    # Stop deletion of customer if bank account has not been deleted!!!!!!

