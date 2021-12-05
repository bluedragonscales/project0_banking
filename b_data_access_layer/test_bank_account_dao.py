# Module for testing the bank account DAO methods.

from a_entities.bank_account import BankAccount
from b_data_access_layer.postgres_bank_account_dao import BankAccountPostgresDAO

# Created instance of BankAccountPostgresDAO to be able to use those methods.
postgres_bank_account_dao = BankAccountPostgresDAO()

create_bank_one = BankAccount(0, 2, 15)



def test_create_bank_account_happy():
    # Pass in bank account object.
    created_account = postgres_bank_account_dao.create_bank_account(create_bank_one)
    assert created_account.account_id != 0



def test_view_account_info_happy():
    # Pass in a bank account id.
    account_balance = postgres_bank_account_dao.view_bank_account(2)
    assert account_balance.account_id == 2



def test_deposit_happy():
    # Pass in a money amount and a bank account object.
    update_bank = BankAccount(8, 2, 35)
    update_balance = postgres_bank_account_dao.deposit(20, update_bank)
    assert update_balance > 35



def test_withdraw_happy():
    withdraw_account = BankAccount(10, 4, 500)
    update_balance = postgres_bank_account_dao.withdraw(10, withdraw_account)
    assert update_balance < 500



def test_transfer_funds_happy():
    transfer_one = BankAccount(6, 6, 200)
    transfer_two = BankAccount(11, 5, 10)
    customer_accounts_transfer = postgres_bank_account_dao.transfer_funds(6, transfer_one, transfer_two)
    assert customer_accounts_transfer > 10
# works but doesn't show well.




def test_view_all_accounts_happy():
    accounts = postgres_bank_account_dao.view_all_bank_accounts()
    assert len(accounts) > 1



def test_delete_bank_account_happy():
    # Passed in a bank account number.
    # account_to_delete = BankAccount(0, 7, 0)
    account_to_delete = postgres_bank_account_dao.delete_bank_account(12)
    assert account_to_delete