# Module to hold the customer object and its ability to turn into a dictionary so that it can be converted and passed
# as JSONs to and from Postman. The objects will contain a first name, last name, unique customer id, and an associated
# bank id for when the customer creates a bank account. It will remain as zero until the account is created.

class Customer:
    def __init__(self, first_name: str, last_name: str, customer_id: int, account_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.customer_id = customer_id
        self.account_id = account_id

    def customer_dictionary(self):
        return {
            "firstName" : self.first_name,
            "lastName" : self.last_name,
            "customerId" : self.customer_id,
            "accountId" : self.account_id
        }