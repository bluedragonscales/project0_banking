# This is the abstract class/methods for the bank account objects.

from abc import ABC, abstractmethod
from a_entities.bank_account import BankAccount


class BankAccountDAO(ABC):

    # The abstract method for creating a bank account. We pass in the bank account object so the create method has
    # access to all of the bank account information. The return type is the entire bank account object.
    @abstractmethod
    def create_bank_account(self, bank_account: BankAccount) -> BankAccount:
        pass


    # The abstract method to view the bank account information. We pass in the account id to view all that id's
    # information such as the balance.
    @abstractmethod
    def view_bank_account(self, account_id: int):
        pass


    # The abstract method to deposit money into a bank account. We pass in an int to update the balance. Then we also
    # pass in the bank account object so that only one person can update their own bank account.
    @abstractmethod
    def deposit(self, deposit: int, bank_account: BankAccount):
        pass


    # The abstract method to withdraw money from a bank account. We pass in an int to withdraw. Then we also pass in the
    # bank account object so that only one person can update their own bank account.
    @abstractmethod
    def withdraw(self, withdraw: int, bank_account: BankAccount):
        pass


    # The abstract method to transfer funds from one bank account to another. We pass in an amount to transfer in the
    # form of an int. Then we pass in multiple bank accounts to transfer between each other.
    @abstractmethod
    def transfer_funds(self, balance: int, bank_account_one: BankAccount, bank_account_two: BankAccount):
        pass



    # The abstract method to view all of the created bank accounts. No arguments to pass because it's just a list of
    # everything. What's returned is a list.
    @abstractmethod
    def view_all_bank_accounts(self) -> list[BankAccount]:
        pass


    # The abstract method to delete a bank account. Only an account id needs to be passed. Then we get a true/false
    # statement returned.
    @abstractmethod
    def delete_bank_account(self, account_id: int) -> bool:
        pass