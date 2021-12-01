from abc import ABC, abstractmethod
from a_entities.bank_account import BankAccount


class BankAccountDAO(ABC):

    # The abstract method for creating a bank account.
    @abstractmethod
    def create_bank_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    # The abstract method to view the bank account balance.
    @abstractmethod
    def view_bank_account(self, account_id: int) -> BankAccount:
        pass

    # The abstract method to deposit, withdraw, and transfer money into a bank account.
    @abstractmethod
    def update_bank_account(self, *bank_account: BankAccount) -> BankAccount:
        pass

    # The abstract method to view all of the created bank accounts.
    @abstractmethod
    def view_all_bank_accounts(self) -> list[BankAccount]:
        pass

    # The abstract method to delete a bank account.
    @abstractmethod
    def delete_bank_account(self, account_id: int) -> bool:
        pass