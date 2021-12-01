from a_entities.customer import Customer
from b_data_access_layer.imp_customer_dao import CustomerDAOImp
from c_service_layer.abstract_customer_service import CustomerService
from c_service_layer.custom_exceptions import *


class CustomerServiceImp(CustomerService):

    # This function is responsible for connecting everything from the DAO layer, basically everything from the class
    # "CustomerDAOImp", into the service layer. It is called dependency injection. Because the DAO layer is now
    # connected to the service layer, the service layer will forward the request from the API to the DAO layer, and then
    # will forward requests to the API from the DAO layer.
    def __init__(self, customer_dao):
        # The "CustomerDAOImp" is a local database object, but can easily be switched out for a cloud based DB object.
        self.customer_dao: CustomerDAOImp = customer_dao


    def service_create_customer(self, customer: Customer) -> Customer:
        # Business logic for creating a customer: going down the list of customers, if the initialized customer id
        # (cust.customer_id) matches one already in the list (customer.customer_id), a custom exception will be raised.
        # Else if there are no matching customer ids then the customer will be created.
        for cust in self.customer_dao.customer_list:
            if cust.customer_id == customer.customer_id:
                raise DuplicateCustomerIdException("This account number is already assigned!")
            else:
                return self.customer_dao.create_customer(customer)


    def service_get_customer_information(self, customer_id: int) -> Customer:
        return self.customer_dao.get_customer_information(customer_id)


    def service_update_customer_information(self, customer: Customer) -> Customer:
        # Business logic for updating a customer: going down the list of customers, if the account id of the updated
        # information passed into this method matches one of the already created customers, then the update will not
        # happen and a custom exception will be raised.
        for cust in self.customer_dao.customer_list:
            if cust.account_id == customer.account_id:
                raise DuplicateBankAccountException("A customer already has this bank account!")
            else:
                return self.customer_dao.update_customer_information(customer)

    def service_view_all_customers(self) -> list[Customer]:
        return self.customer_dao.view_all_customers()

    def service_delete_customer(self, customer_id: int) -> bool:
        # Business logic for deleting a customer: going down the list of customers, if there is a matching customer_id
        # to the one passed in as an argument, then delete that customer. If that customer_id doesn't match anything
        # found in the customer list then raise a custom exception.
        for cust in self.customer_dao.customer_list:
            if cust.customer_id == customer_id:
                return self.customer_dao.delete_customer(customer_id)
            else:
                raise AlreadyDeletedException("This customer doesn't exist!")