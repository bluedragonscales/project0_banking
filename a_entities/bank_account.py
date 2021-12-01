
class BankAccount:
    def __init__(self, account_id: int, balance: int):
        self.account_id = account_id
        self.balance = balance

    def bank_account_dictionary(self):
        return {
            "accountId" : self.account_id,
            "balance" : self.balance
        }
