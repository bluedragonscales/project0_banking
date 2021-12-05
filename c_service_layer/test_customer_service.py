from a_entities.customer import Customer
from b_data_access_layer.postgres_customer_dao import CustomerPostgresDAO
from c_service_layer.custom_exceptions import *
from c_service_layer.postgres_customer_service import CustomerPostgresService


# Created the postgres DAO and postgres service objects. Injected the DAO into the service layer.
postgres_customer_dao = CustomerPostgresDAO()
postgres_customer_service = CustomerPostgresService(postgres_customer_dao)


# Objects for testing:
duplicate_customer = Customer("Sam", "Winchester", 7)
update_customer = Customer("Dean", "Winchester", 20)



# Test to make sure someone on the front end API doesn't accidentally enter a string where a number is required or vise
# versa. Also testing to make sure this customer is not already created.
def test_validate_create_customer_sad():
    try:
        wrong_cust_info = Customer(10, "Henderson", "10")
        postgres_customer_service.service_create_customer(wrong_cust_info)
    except WrongInformationException as w:
        assert str(w) == "Incorrect information entered from front end."




def test_validate_delete_customer_with_bank_account_sad():
    try:
        postgres_customer_service.service_delete_customer(5)
    except DeletionErrorException as d:
        assert str(d) == "Please delete the bank account before deleting your information."
