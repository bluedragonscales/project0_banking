from a_entities.bank_account import BankAccount
from b_data_access_layer.postgres_bank_account_dao import BankAccountPostgresDAO
from b_data_access_layer.postgres_customer_dao import CustomerPostgresDAO
from c_service_layer.abstract_bank_account_service import BankAccountService
from c_service_layer.custom_exceptions import *


class BankAccountPostgresService(BankAccountService):

    def __init__(self, bank_account_dao):
        self.bank_account_dao: BankAccountPostgresDAO = bank_account_dao


    def service_create_bank_account(self, bank_account: BankAccount) -> BankAccount:
        # Business logic: a bank account cannot be created if the customer id does not exist.
        customer_list = CustomerPostgresDAO.view_all_customers(self)
        for cust in customer_list:
            if cust.customer_id != bank_account.customer_id:
                raise DoesNotExistException("Bank account cannot be created for nonexistent customer.")
            else:
                return self.bank_account_dao.create_bank_account(bank_account)


    def service_view_bank_account(self, account_id: int) -> BankAccount:
        # Business logic: a bank account cannot be viewed if the id doesn't exist.
        account_list = self.bank_account_dao.view_all_bank_accounts()
        for account in account_list:
            if account.account_id == account_id:
                return self.bank_account_dao.view_bank_account(account_id)
            else:
                raise DoesNotExistException("Bank account has not been created.")



    def service_deposit(self, deposit: int, bank_account: BankAccount) -> BankAccount:
        return self.bank_account_dao.deposit(deposit, bank_account)


    def service_withdraw(self, withdraw: int, bank_account: BankAccount) -> BankAccount:
        # Business logic: money in an account cannot go beneath 0.
        if bank_account.balance < withdraw:
            raise InsufficientFundsException("Insufficient funds to make this withdrawal.")
        else:
            return self.bank_account_dao.withdraw(withdraw, bank_account)


    def service_transfer_funds(self, balance: int, bank_account_one: BankAccount, bank_account_two: BankAccount):
        # Business logic: money in an account cannot be transferred if the balance will go beneath 0.
        if bank_account_one.balance < balance:
            raise InsufficientFundsException("First account has insufficient funds to transfer.")
        else:
            return self.bank_account_dao.transfer_funds(balance, bank_account_one, bank_account_two)


    def service_view_all_accounts_per_customer(self, customer_id: int) -> list[BankAccount]:
        return self.bank_account_dao.view_all_accounts_per_customer(customer_id)


    def service_view_all_bank_accounts(self) -> list[BankAccount]:
        return self.bank_account_dao.view_all_bank_accounts()


    def service_delete_bank_account(self, account_id: int) -> bool:
        # Business logic: account cannot be deleted if the account id does not exist.
        account_list = self.bank_account_dao.view_all_bank_accounts()
        for account in account_list:
            if account.account_id == account_id:
                return self.bank_account_dao.delete_bank_account(account_id)
            else:
                raise DoesNotExistException("Bank account does not exist.")