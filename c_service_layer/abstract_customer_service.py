# Module for the abstract class and methods for the customer's service layer.

from abc import ABC, abstractmethod
from a_entities.customer import Customer


class CustomerService(ABC):

    @abstractmethod
    def service_create_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_get_customer_information(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def service_update_customer_information(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_view_all_customers(self) -> list[Customer]:
        pass

    @abstractmethod
    def service_delete_customer(self, customer_id: int) -> bool:
        pass