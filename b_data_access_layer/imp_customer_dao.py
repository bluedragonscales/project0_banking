

from b_data_access_layer.abstract_customer_dao import CustomerDAO
from a_entities.customer import Customer


class CustomerDAOImp(CustomerDAO):
    customer_list = []
    customer_id_generator = 0

    # We pass in an object of type "Customer" so that all of the information we created in the "Customer" class in
    # module "customer_entity" will be available right away. The return type annotation "-> Customer" means this method
    # will return the Customer object back in the database.
    def create_customer(self, customer: Customer) -> Customer:
        CustomerDAOImp.customer_id_generator += 1
        customer.customer_id = CustomerDAOImp.customer_id_generator
        CustomerDAOImp.customer_list.append(customer)
        return customer


    # We will pass in the customer's id that is created in the "Customer" class and will be associated with that
    # particular customer object (when the object is created).
    def get_customer_information(self, customer_id: int) -> Customer:
        # Scan through the "customer_list" with the temp variable "cust". When the customer id in the list matches the
        # customer id that was passed into the method as an argument, return the customer object.
        for cust in CustomerDAOImp.customer_list:
            if cust.customer_id == customer_id:
                return cust


    # Passing in the entire customer object so we have all the different pieces of information available to update, if
    # needed.
    def update_customer_information(self, customer: Customer) -> Customer:
        # Iterating through the customer list to find the matching id for the customer argument we passed through to
        # the method.
        for cust in CustomerDAOImp.customer_list:
            if cust.customer_id == customer.customer_id:
                # Finding the correct id, find and store the index of that object on the list.
                index = CustomerDAOImp.customer_list.index(cust)
                # Assign the new customer info to the index where the old one was at.
                CustomerDAOImp.customer_list[index] = customer
                return customer


    # We don't need any parameters because we can use use the database to look at all the customers.
    def view_all_customers(self) -> list[Customer]:
        return CustomerDAOImp.customer_list


    # Passing in the unique customer id so it tells the method that this particular customer will be deleted.
    def delete_customer(self, customer_id: int) -> bool:
        for cust in CustomerDAOImp.customer_list:
            if cust.customer_id == customer_id:
                index = CustomerDAOImp.customer_list.index(cust)
                del CustomerDAOImp.customer_list[index]
                return bool
