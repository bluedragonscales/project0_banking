# Module for the DAO layer methods for the bank account object.

from a_entities.bank_account import BankAccount
from b_data_access_layer.abstract_bank_account_dao import BankAccountDAO
from database_connection import connection


class BankAccountPostgresDAO(BankAccountDAO):

    def create_bank_account(self, bank_account: BankAccount) -> BankAccount:
        sql = 'insert into "project0".bank_account values (default, %s, %s) returning account_id'
        cursor = connection.cursor()
        cursor.execute(sql, (bank_account.customer_id, bank_account.balance))
        bank_account_id = cursor.fetchone()[0]
        bank_account.account_id = bank_account_id
        connection.commit()
        return bank_account



    def view_bank_account_balance(self, account_id: int):
        sql = 'select balance from "project0".bank_account where account_id = %s'
        cursor = connection.cursor()
        # Passing only one argument into the sql so using a list instead of a tuple.
        cursor.execute(sql, [account_id])
        bank_record = cursor.fetchone()[0]
        bank_account_balance = bank_record
        return bank_account_balance



    def deposit(self, deposit: int, bank_account: BankAccount):
        sql = 'update "project0".bank_account set balance = balance + %s where account_id = %s returning balance'
        cursor = connection.cursor()
        cursor.execute(sql, (deposit, bank_account.account_id))
        account_balance = cursor.fetchone()[0]
        connection.commit()
        return account_balance



    def withdraw(self, withdraw: int, bank_account: BankAccount):
        sql = 'update "project0".bank_account set balance = balance - %s where account_id = %s returning balance'
        cursor = connection.cursor()
        cursor.execute(sql, (withdraw, bank_account.account_id))
        account_balance = cursor.fetchone()[0]
        connection.commit()
        return account_balance



    def transfer_funds(self, balance: int, bank_account_one: BankAccount, bank_account_two: BankAccount):
        sql = 'update "project0".bank_account set balance = balance - %s where account_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (balance, bank_account_one.account_id))
        sql2 = 'update "project0".bank_account set balance = balance + %s where account_id = %s returning balance'
        cursor.execute(sql2, (balance, bank_account_two.account_id))
        bank_account_two.balance = cursor.fetchone()[0]
        connection.commit()
        return bank_account_two.balance



    def view_all_accounts_per_customer(self, customer_id: int) -> list[BankAccount]:
        sql = 'select * from "project0".bank_account where customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        account_records_per_cust = cursor.fetchall()
        customers = BankAccountPostgresDAO.view_all_bank_accounts(self)
        for cust in customers:
            if cust.customer_id == customer_id:
                customer_account_list = []
                for record in account_records_per_cust:
                    customer_account_list.append(BankAccount(*record))
                return customer_account_list



    def view_all_bank_accounts(self) -> list[BankAccount]:
        sql = 'select * from "project0".bank_account'
        cursor = connection.cursor()
        cursor.execute(sql)
        # We use the "fetchall()" method for the cursor object because we are fetching all the information instead of
        # just information that matches.
        account_records = cursor.fetchall()
        bank_account_list = []
        for bank in account_records:
            bank_account_list.append(BankAccount(*bank))
        return bank_account_list



    def delete_bank_account(self, account_id: int) -> bool:
        sql = 'delete from "project0".bank_account where account_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        return True