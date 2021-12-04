from a_entities.bank_account import BankAccount
from b_data_access_layer.postgres_bank_account_dao import BankAccountPostgresDAO
from c_service_layer.custom_exceptions import *
from c_service_layer.postgres_bank_account_service import BankAccountPostgresService

postgres_bank_account_dao = BankAccountPostgresDAO()
postgres_bank_account_service = BankAccountPostgresService(postgres_bank_account_dao)


unable_to_create = BankAccount(0, 20, 10)
bad_withdrawal = BankAccount(2, 2, 5)
transfer_test = BankAccount(8, 2, 15)


def test_validate_create_bank_account_sad():
    try:
        postgres_bank_account_service.service_create_bank_account(unable_to_create)
    except DoesNotExistException as d:
        assert str(d) == "Bank account cannot be created for nonexistent customer."


def test_validate_view_account_sad():
    try:
        postgres_bank_account_service.service_view_bank_account(20)
    except DoesNotExistException as d:
        assert str(d) == "Bank account has not been created."



def test_validate_withdraw_sad():
    try:
        postgres_bank_account_service.service_withdraw(20, bad_withdrawal)
    except InsufficientFundsException as i:
        assert str(i) == "Insufficient funds to make this withdrawal."


def test_validate_transfer_funds_sad():
    try:
        postgres_bank_account_service.service_transfer_funds(20, bad_withdrawal, transfer_test)
    except InsufficientFundsException as i:
        assert str(i) == "First account has insufficient funds to transfer."


def test_validate_delete_account_sad():
    try:
        postgres_bank_account_service.service_delete_bank_account(20)
    except DoesNotExistException as d:
        assert str(d) == "Bank account does not exist."