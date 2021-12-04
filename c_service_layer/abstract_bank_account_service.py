from abc import ABC, abstractmethod
from a_entities.bank_account import BankAccount


class BankAccountService(ABC):

    @abstractmethod
    def service_create_bank_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def service_view_bank_account(self, account_id: int) -> BankAccount:
        pass

    @abstractmethod
    def service_deposit(self, deposit: int, bank_account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def service_withdraw(self, withdraw: int, bank_account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def service_transfer_funds(self, balance: int, bank_account_one: BankAccount, bank_account_two: BankAccount):
        pass

    @abstractmethod
    def service_view_all_accounts_per_customer(self, customer_id: int) -> list[BankAccount]:
        pass

    @abstractmethod
    def service_view_all_bank_accounts(self) -> list[BankAccount]:
        pass

    @abstractmethod
    def service_delete_bank_account(self, account_id: int) -> bool:
        pass