from a_entities.customer import Customer
from b_data_access_layer.postgres_bank_account_dao import BankAccountPostgresDAO
from b_data_access_layer.postgres_customer_dao import CustomerPostgresDAO
from c_service_layer.abstract_customer_service import CustomerService
from c_service_layer.custom_exceptions import *


class CustomerPostgresService(CustomerService):

    def __init__(self, customer_dao):
        self.customer_dao: CustomerPostgresDAO = customer_dao


    def service_create_customer(self, customer: Customer) -> Customer:
        # Business logic: if user provides an incorrect data type for the parameters then throw a custom exception. If
        # correct data is provided but there's already an id then raise another custom exception.
        if isinstance(customer.first_name, str) and isinstance(customer.last_name, str) and \
                isinstance(customer.customer_id, int):
            return self.customer_dao.create_customer(customer)
        else:
            raise WrongInformationException("Incorrect information entered from front end.")



    def service_get_customer_information(self, customer_id: int) -> Customer:
        return self.customer_dao.get_customer_information(customer_id)



    def service_update_customer_information(self, customer: Customer) -> Customer:
        return self.customer_dao.update_customer_information(customer)



    def service_view_all_customers(self) -> list[Customer]:
        return self.customer_dao.view_all_customers()



    def service_delete_customer(self, customer_id: int) -> bool:
        # Business logic: if there are bank accounts attached to the customer id then those bank accounts should be
        # deleted first (throw a custom exception).
        bank_account_list = BankAccountPostgresDAO.view_all_bank_accounts(self)
        for account in bank_account_list:
            if account.customer_id == customer_id:
                raise DeletionErrorException("Please delete the bank account before deleting your information.")
            else:
                self.customer_dao.delete_customer(customer_id)
                return True
