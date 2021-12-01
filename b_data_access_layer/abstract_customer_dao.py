from abc import ABC, abstractmethod
from a_entities.customer import Customer


class CustomerDAO(ABC):

    # The abstract method to create a customer.
    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass

    # The abstract method to view all the information associated with the customer.
    @abstractmethod
    def get_customer_information(self, customer_id: int) -> Customer:
        pass

    # The abstract method to update customer information.
    @abstractmethod
    def update_customer_information(self, customer: Customer) -> Customer:
        pass

    # The abstract method to view all customers.
    @abstractmethod
    def view_all_customers(self) -> list[Customer]:
        pass

    # The abstract method to delete a customer from the system.
    @abstractmethod
    def delete_customer(self, customer_id: int) -> bool:
        pass
