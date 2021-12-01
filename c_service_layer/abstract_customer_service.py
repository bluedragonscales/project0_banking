from abc import ABC, abstractmethod
from a_entities.customer import Customer


class CustomerService(ABC):
    # The abstract method to create a customer.
    @abstractmethod
    def service_create_customer(self, customer: Customer) -> Customer:
        pass

    # The abstract method to view all the information associated with the customer.
    @abstractmethod
    def service_get_customer_information(self, customer_id: int) -> Customer:
        pass

    # The abstract method to update customer information.
    @abstractmethod
    def service_update_customer_information(self, customer: Customer) -> Customer:
        pass

    # The abstract method to view all customers.
    @abstractmethod
    def service_view_all_customers(self) -> list[Customer]:
        pass

    # The abstract method to delete a customer from the system.
    @abstractmethod
    def service_delete_customer(self, customer_id: int) -> bool:
        pass