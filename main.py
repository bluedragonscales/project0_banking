from flask import Flask, request, jsonify
from a_entities.customer import Customer
from b_data_access_layer.imp_customer_dao import CustomerDAOImp
from c_service_layer.custom_exceptions import *
from c_service_layer.imp_customer_service import CustomerServiceImp

# Created the Flask object to use flask environment. Also created the DAO and the Service layer instances so that all
# of the information for both layers are available here.
app = Flask(__name__)
customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)
# Passed in the customer's DAO layer so everything that happens in the service layer goes to the DAO layer and vise
# versa.



# The route to create a customer.
@app.post("/customer")
def create_customer():
    # Creating a request to create a customer and storing the information in a variable "customer_to_return" so we can
    # return this requested information back to the user on the API side (Postman in this case). However, in our service
    # layer, this method might throw an exception (we even tested it) so this request/response code should go into a
    # try/except block.
    try:
        # We retrieve the request that the API sent to this server.
        customer_data = request.get_json()
        # We format the data so that it is read correctly by the server.
        new_customer = Customer(customer_data["firstName"],
                                customer_data["lastName"],
                                customer_data["customerId"],
                                customer_data["accountId"])
        # We pass this retrieved and formatted data into our service layer (leading to DAO layer) method.
        customer_to_return = customer_service.service_create_customer(new_customer)
        # The object that is crunched by the DAO and service layers are then passed back to the server and this turns it
        # into a dictionary.
        customer_as_dictionary = customer_to_return.customer_dictionary()
        # Converting the customer dictionary into a JSON.
        customer_as_json = jsonify(customer_as_dictionary)
        # Sending the jsonified dictionary to the user (Postman).
        return customer_as_json
    except DuplicateCustomerIdException as e:
        exception_dictionary = {"message" : str(e)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception



# The route to view all the information associated with the customer.
@app.get("/customer/<customer_id>")
def get_customer_information(customer_id: str):
    result = customer_service.service_get_customer_information(int(customer_id))
    result_as_dictionary = result.customer_dictionary()
    result_as_json = jsonify(result_as_dictionary)
    return result_as_json



# The route to update customer information.
@app.patch("/customer/<customer_id>")
def update_customer_information(customer_id: str):
    try:
        customer_data = request.get_json()
        new_customer = Customer(customer_data["firstName"],
                                customer_data["lastName"],
                                int(customer_id),
                                customer_data["accountId"])
        update_customer = customer_service.service_update_customer_information(new_customer)
        return "Hooray! Customer information updated successfully."
    except DuplicateBankAccountException as e:
        exception_dictionary = {"message": str(e)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception



# The route to view all customers.
@app.get("/customer")
def view_all_customers():
    all_customers = customer_service.service_view_all_customers()
    customers_as_dictionaries = []
    for cust in all_customers:
        dictionary_customers = cust.customer_dictionary()
        customers_as_dictionaries.append(dictionary_customers)
    return jsonify(customers_as_dictionaries)



# The route to delete a customer from the system.
@app.delete("/customer/<customer_id>")
def delete_customer_information(customer_id: str):
    try:
        result = customer_service.service_delete_customer(int(customer_id))
        return "Customer with id {} has been deleted.".format(customer_id)
    except AlreadyDeletedException as e:
        return str(e)


app.run()