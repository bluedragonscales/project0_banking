# This is the beginning of the Data Access Object layer, often referred to as the DAO layer. This class contains the
# skeleton for the methods that will actually be implemented. This skeleton is called the abstract class and inside are
# the abstract methods that MUST be implemented in the following subclass that inherits them. But since these methods
# are not the ones being implemented we just use the keyword "pass".

# This import comes from the parent abstract class, what all abstract classes are subclassed from. Lower case "abc" is
# the package that contains the parent abstract class, and "ABC" is the module containing the actual parent abstract
# class that my "CustomerDAO" abstract class is inheriting. The additional module being imported, "abstractmethod", will
# give the abstract label "@abstractmethod" implementation to label the methods as abstract.
from abc import ABC, abstractmethod

# This import comes from my package "a_entities" and narrows it down to the module "customer". I am importing the
# Customer Object blueprint class so that it can be passed on up through the layers and interact with the cloud
# database, server, and front end (Postman).
from a_entities.customer import Customer


class CustomerDAO(ABC):

    # The abstract method to create a customer. We pass in the whole customer object that was imported at the top of
    # this module so we have access to all the info for that customer. The return type is also annotated as the whole
    # object so that when the information returns to the database and the API, all the information will be available.
    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass


    # The abstract method to view information associated with the customer. We pass the unique customer_id into the
    # method so all the information associated with that particular id will be found in the database. The return type is
    # the whole customer object because the API user wants to see all of that information.
    @abstractmethod
    def get_customer_information(self, customer_id: int) -> Customer:
        pass


    # The abstract method to update customer information. We pass in the whole customer object so that all their info
    # has the ability to be updated. We return the whole customer object to show it was updated.
    @abstractmethod
    def update_customer_information(self, customer: Customer) -> Customer:
        pass


    # The abstract method to view all customers. We don't pass anything into this method because we're just getting a
    # list of all the customers in the database. A list of the objects are returned.
    @abstractmethod
    def view_all_customers(self) -> list[Customer]:
        pass


    # The abstract method to delete a customer from the system. We pass in the unique customer id so any customer
    # associated with that id will be deleted from the system. A true/false outcome will be returned to the front end.
    @abstractmethod
    def delete_customer(self, customer_id: int) -> bool:
        pass
