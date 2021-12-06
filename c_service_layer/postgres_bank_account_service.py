from a_entities.bank_account import BankAccount
from b_data_access_layer.postgres_bank_account_dao import BankAccountPostgresDAO
from c_service_layer.abstract_bank_account_service import BankAccountService
from c_service_layer.custom_exceptions import *


class BankAccountPostgresService(BankAccountService):

    def __init__(self, bank_account_dao):
        self.bank_account_dao: BankAccountPostgresDAO = bank_account_dao


    def service_create_bank_account(self, bank_account: BankAccount) -> BankAccount:
        return self.bank_account_dao.create_bank_account(bank_account)



    def service_view_bank_account(self, account_id: int) -> BankAccount:
        return self.bank_account_dao.view_bank_account(account_id)



    def service_deposit(self, deposit: int, bank_account: BankAccount) -> BankAccount:
        return self.bank_account_dao.deposit(deposit, bank_account)



    def service_withdraw(self, account_id: int, withdraw: float):
        # Business logic: money in an account cannot go beneath 0.
        bank_account = self.bank_account_dao.view_bank_account(account_id)
        if bank_account.balance < withdraw:
            raise InsufficientFundsException("Insufficient funds to make this withdrawal.")
        elif withdraw < 0:
            raise InsufficientFundsException("Insufficient funds to make this withdrawal.")
        else:
            return self.bank_account_dao.withdraw(account_id, withdraw)



    def service_transfer_funds(self, balance: int, bank_account_one: BankAccount, bank_account_two: BankAccount):
        # Business logic: money in an account cannot be transferred if the balance will go beneath 0.
        if bank_account_one.balance < balance:
            raise InsufficientFundsException("First account has insufficient funds to transfer.")
        else:
            return self.bank_account_dao.transfer_funds(balance, bank_account_one, bank_account_two)



    def service_view_all_bank_accounts(self) -> list[BankAccount]:
        return self.bank_account_dao.view_all_bank_accounts()



    def service_delete_bank_account(self, account_id: int) -> bool:
        return self.bank_account_dao.delete_bank_account(account_id)