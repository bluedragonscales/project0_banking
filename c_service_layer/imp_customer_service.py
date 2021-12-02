# Module for all the implemented customer methods for the service layer.

from a_entities.customer import Customer
from b_data_access_layer.imp_customer_dao import CustomerDAOImp
from c_service_layer.abstract_customer_service import CustomerService
from c_service_layer.custom_exceptions import *


class CustomerServiceImp(CustomerService):

    # This function is responsible for connecting everything from the DAO layer, basically everything from the class
    # "CustomerDAOImp", into the service layer. It is called dependency injection. Because the DAO layer is now
    # injected into to the service layer, the service layer will forward the request from the API to the DAO layer, and
    # then forward requests to the API from the DAO layer.
    def __init__(self, customer_dao):
        self.customer_dao: CustomerDAOImp = customer_dao


    def service_create_customer(self, customer: Customer) -> Customer:
        # Business logic for create customer: if user provides an incorrect data type for the parameters then throw a
        # custom exception.
        for cust in self.customer_dao.customer_list:
            if cust.customer_id == customer.customer_id:
                raise DuplicateCustomerException("This customer was already created.")
        if isinstance(customer.first_name, str) and isinstance(customer.last_name, str) and \
                isinstance(customer.customer_id, int):
            return self.customer_dao.create_customer(customer)
        else:
            raise WrongInformationException("Incorrect information entered from front end.")


    def service_get_customer_information(self, customer_id: int) -> Customer:
        return self.customer_dao.get_customer_information(customer_id)


    def service_update_customer_information(self, customer: Customer) -> Customer:
        # Business logic for updating a customer: going down the list of customers, if the account id of the updated
        # information passed into this method matches one of the already created customers, then the update will not
        # happen and a custom exception will be raised.
        for cust in self.customer_dao.customer_list:
            if cust.customer_id == customer.customer_id:
                if cust.first_name == customer.first_name and cust.last_name == customer.last_name:
                    raise DuplicateInformationException("This information is already the same.")
                # elif cust.last_name == customer.last_name:
                #     raise DuplicateInformationException("The last name is already the same.")
                else:
                    return self.customer_dao.update_customer_information(customer)
            else:
                raise AlreadyDeletedException("This customer doesn't exist!")


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