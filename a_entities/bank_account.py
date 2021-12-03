# This module holds the bank account object constructor and its ability to turn into a dictionary so that it can be
# converted and passed as JSONs to/from Postman and postgres. The customer id field will be sent when a customer opens
# a bank account with their customer_id.

class BankAccount:
    def __init__(self, account_id: int, customer_id: int, balance: int):
        self.account_id = account_id
        self.customer_id = customer_id
        self.balance = balance

    def bank_account_dictionary(self):
        return {
            "accountId" : self.account_id,
            "customerId" : self.customer_id,
            "balance" : self.balance
        }
