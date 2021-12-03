# Module for the DAO layer methods for the bank account object.
from a_entities.bank_account import BankAccount
from b_data_access_layer.abstract_bank_account_dao import BankAccountDAO


class BankAccountPostgresDAO(BankAccountDAO):

    def create_bank_account(self, bank_account: BankAccount, customer_id: int) -> BankAccount:
        pass


    def view_bank_account_balance(self, bank_account: BankAccount) -> BankAccount:
        pass


    def update_bank_account(self, funds: int, bank_account: BankAccount) -> BankAccount:
        pass


    def transfer_funds(self, *bank_account: BankAccount) -> BankAccount:
        pass


    def view_all_bank_accounts(self) -> list[BankAccount]:
        pass


    def delete_bank_account(self, account_id: int) -> bool:
        pass