# This is the abstract class/methods for the bank account objects.

from abc import ABC, abstractmethod
from a_entities.bank_account import BankAccount


class BankAccountDAO(ABC):

    # The abstract method for creating a bank account. We pass in the bank account object so the create method has
    # access to all of the bank account information, and we also pass in the customer_id to reference the customer that
    # is opening the account.
    @abstractmethod
    def create_bank_account(self, bank_account: BankAccount, customer_id: int) -> BankAccount:
        pass


    # The abstract method to view the current bank account balance. We pass in the full bank account object so that the
    # method has access to both the bank account id and the actual balance.
    @abstractmethod
    def view_bank_account_balance(self, bank_account: BankAccount) -> BankAccount:
        pass


    # The abstract method to deposit and withdraw in a bank account. We pass in an int (positive for a deposit and
    # negative for a withdrawal) to update the balance. Then we also pass in the bank account object so that only one
    # person can update their own bank account since their ids are tied.
    @abstractmethod
    def update_bank_account(self, funds: int, bank_account: BankAccount) -> BankAccount:
        pass


    # The abstract method to transfer funds from one bank account to another. The customer who owns the bank account
    # can give money to someone but they cannot take it from someone else's bank account. We pass in multiple bank
    # accounts so multiple bank accounts can interact.
    @abstractmethod
    def transfer_funds(self, *bank_account: BankAccount) -> BankAccount:
        pass


    # The abstract method to view all of the created bank accounts. No arguments to pass because it's just a list of
    # everything.
    @abstractmethod
    def view_all_bank_accounts(self) -> list[BankAccount]:
        pass


    # The abstract method to delete a bank account. Only an account id needs to be passed in to get a true/false
    # statement that the bank account has been deleted.
    @abstractmethod
    def delete_bank_account(self, account_id: int) -> bool:
        pass