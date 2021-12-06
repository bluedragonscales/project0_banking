from flask import Flask, request, jsonify

from a_entities.bank_account import BankAccount
from a_entities.customer import Customer
from b_data_access_layer.postgres_bank_account_dao import BankAccountPostgresDAO
from b_data_access_layer.postgres_customer_dao import CustomerPostgresDAO
from c_service_layer.postgres_bank_account_service import BankAccountPostgresService
from c_service_layer.postgres_customer_service import CustomerPostgresService
from c_service_layer.custom_exceptions import *
import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

# Created the Flask object to use flask environment. Also created the DAO and the Service layer instances so that all
# of the information for both layers are available here.
app = Flask(__name__)
customer_dao = CustomerPostgresDAO()
customer_service = CustomerPostgresService(customer_dao)
bank_account_dao = BankAccountPostgresDAO()
bank_account_service = BankAccountPostgresService(bank_account_dao)




@app.post("/customer")
def create_customer():
    try:
        # We retrieve the request that the API sent to this server.
        customer_data = request.get_json()
        # We format the data so that it is read correctly by the server.
        new_customer = Customer(customer_data["firstName"], customer_data["lastName"], customer_data["customerId"])
        # We pass this retrieved and formatted data into our service layer.
        customer_to_return = customer_service.service_create_customer(new_customer)
        # The objects crunched by the DAO and service layers are passed back to the server and turned into a dictionary.
        customer_as_dictionary = customer_to_return.customer_dictionary()
        # Converting the dictionary into a JSON.
        customer_as_json = jsonify(customer_as_dictionary)
        # Sending the jsonified dictionary to the user (Postman).
        return customer_as_json
    except WrongInformationException as w:
        exception_dictionary = {"Message" : str(w)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception



@app.post("/account")
def create_bank_account():
    account_data = request.get_json()
    new_account = BankAccount(account_data["accountId"], account_data["customerId"], account_data["balance"])
    account_to_return = bank_account_service.service_create_bank_account(new_account)
    account_as_dictionary = account_to_return.bank_account_dictionary()
    account_as_json = jsonify(account_as_dictionary)
    return account_as_json




@app.get("/customer/<customer_id>")
def get_customer_information(customer_id: str):
    result = customer_service.service_get_customer_information(int(customer_id))
    result_as_dictionary = result.customer_dictionary()
    result_as_json = jsonify(result_as_dictionary)
    return result_as_json




@app.get("/account/<account_id>")
def get_account_information(account_id: str):
    account_info = bank_account_service.service_view_bank_account(int(account_id))
    info_as_dictionary = account_info.bank_account_dictionary()
    info_as_json = jsonify(info_as_dictionary)
    return info_as_json



@app.patch("/customer/<customer_id>")
def update_customer_information(customer_id: str):
    customer_data = request.get_json()
    new_customer = Customer(customer_data["firstName"],
                            customer_data["lastName"],
                            int(customer_id))
    customer_service.service_update_customer_information(new_customer)
    return "Hooray! Customer with id {} updated successfully.".format(customer_id)




@app.patch("/account/deposit/<account_id>/<balance>")
def deposit(account_id: str, balance: str):
    money_data = request.get_json()
    new_balance = BankAccount(int(account_id), money_data["customerId"], money_data["balance"])
    bank_account_service.service_deposit(int(balance), new_balance)
    return "The balance in account {} has been updated.".format(account_id)



# Database, Postman not catching the insufficient funds exception!!!!
@app.patch("/account/withdraw/<account_id>/<balance>")
def withdraw(account_id: str, balance: str):
    try:
        # money_data = request.get_json()
        # new_balance = BankAccount(int(account_id), money_data["customerId"], int(balance))
        bank_account_service.service_withdraw(int(account_id), float(balance))
        return "The balance in account {} has been updated.".format(account_id)
    except InsufficientFundsException as i:
        exception_dictionary = {"Message": str(i)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception




@app.patch("/account/<account_one>/<account_two>/<balance>")
def transfer_funds(account_one: str, account_two: str, balance: str):
    try:
        transfer_data = request.get_json()
        transfer_one = BankAccount(int(account_one), transfer_data["customerId"], transfer_data["balance"])
        transfer_two = BankAccount(int(account_two), transfer_data["customerId"], transfer_data["balance"])
        bank_account_service.service_transfer_funds(int(balance), transfer_one, transfer_two)
        return "The transfer of ${} has been completed.".format(balance)
    except InsufficientFundsException as i:
        exception_dictionary = {"Message" : str(i)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception




@app.get("/customer")
def view_all_customers():
    all_customers = customer_service.service_view_all_customers()
    customers_as_dictionaries = []
    for cust in all_customers:
        dictionary_customers = cust.customer_dictionary()
        customers_as_dictionaries.append(dictionary_customers)
    return jsonify(customers_as_dictionaries)




@app.get("/account")
def view_all_bank_accounts():
    all_accounts = bank_account_service.service_view_all_bank_accounts()
    accounts_as_dictionaries = []
    for account in all_accounts:
        dictionary_accounts = account.bank_account_dictionary()
        accounts_as_dictionaries.append(dictionary_accounts)
    return jsonify(accounts_as_dictionaries)





@app.delete("/customer/<customer_id>")
def delete_customer(customer_id: str):
    try:
        customer_service.service_delete_customer(int(customer_id))
        return "Customer with id {} has been deleted.".format(customer_id)
    except DeletionErrorException as d:
        exception_dictionary = {"Message" : str(d)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception





@app.delete("/account/<account_id>")
def delete_bank_account(account_id: str):
    bank_account_service.service_delete_bank_account(int(account_id))
    return "Bank account with id {} has been deleted.".format(account_id)




app.run()