from a_entities.bank_account import BankAccount
from b_data_access_layer.postgres_bank_account_dao import BankAccountPostgresDAO
from c_service_layer.custom_exceptions import *
from c_service_layer.postgres_bank_account_service import BankAccountPostgresService

postgres_bank_account_dao = BankAccountPostgresDAO()
postgres_bank_account_service = BankAccountPostgresService(postgres_bank_account_dao)


bad_withdrawal = BankAccount(2, 2, 5)
transfer_test = BankAccount(8, 2, 15)





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


