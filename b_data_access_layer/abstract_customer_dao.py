# Module to hold the abstract class and methods for the data access layer of the customer object so that these method
# skeletons will be ready for the implementation class.

from abc import ABC, abstractmethod
from a_entities.customer import Customer


class CustomerDAO(ABC):

    # The abstract method to create a customer. In the parameters, we're passing in the object from the "Customer"
    # class in the entities module to enter that customer into the postgres database. The return type is the object
    # so that all of the customer information can be returned to the front end.
    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass

    # The abstract method to view the information associated with the customer. We pass the unique customer_id into the
    # method so all the information associated with that particular customer will be returned to the front end.
    @abstractmethod
    def get_customer_information(self, customer_id: int) -> Customer:
        pass

    # The abstract method to update customer information. We pass in the whole customer object so that all their info
    # has the ability to be updated and then the updated information returned to the front end.
    @abstractmethod
    def update_customer_information(self, customer: Customer) -> Customer:
        pass

    # The abstract method to view all customers. We don't pass anything into this method because we're just getting a
    # list of all the customers in the database, no special argument needed. The whole list will be returned to the
    # front end.
    @abstractmethod
    def view_all_customers(self) -> list[Customer]:
        pass

    # The abstract method to delete a customer from the system. We pass in the unique customer id so any customer
    # associated with that id will be deleted from the system, including all of their information. A true/false outcome
    # will be returned to the front end.
    @abstractmethod
    def delete_customer(self, customer_id: int) -> bool:
        pass
