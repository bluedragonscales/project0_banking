from a_entities.customer import Customer
from b_data_access_layer.abstract_customer_dao import CustomerDAO
from database_connection import connection

class CustomerPostgresDAO(CustomerDAO):

    def create_customer(self, customer: Customer) -> Customer:
        # We use this sql statement because this is how new information is added into a table in postgres and also how
        # the customer_id information is returned to us from postgres. The "%s" is a placeholder for information not yet
        # created. "Default" is used because the customer_id is an automatically created serial int.
        sql = 'insert into "project0".customer values(%s, %s, default) returning customer_id'
        # The cursor object allows the execution of sql from this end of the server. We import our connection object
        # that connects us to the postgres database from the module "database_connection". The "cursor()" function
        # activates the path to and from the database.
        cursor = connection.cursor()
        # Then we use that cursor object to pass in a tuple version of the customer information to pass it into the
        # database, changing it into sql language. Leave out the customer_id because that will be taken care of in
        # postgres.
        cursor.execute(sql, (customer.first_name, customer.last_name))
        # We fetch one item of data from postgres, which is the customer_id and store it in "customers_id". Because
        # the postgres command ends with "returning customer_id" that will be the first (and only) information returned
        # to us, so we can put the fetchone index to 0.
        customers_id = cursor.fetchone()[0]
        customer.customer_id = customers_id
        # When using insert, update, or delete sql statements we need to use the "commit()" function on the connection
        # object so that those statements will stick to the tables and not disappear.
        connection.commit()
        return customer


    def get_customer_information(self, customer_id: int) -> Customer:
        sql = 'select * from "project0".customer where customer_id = %s'
        cursor = connection.cursor()
        # Passing only one argument into the sql so using a list instead of a tuple.
        cursor.execute(sql, [customer_id])
        customer_record = cursor.fetchone()
        # The cursor fetches the customer information one by one and then reapplies them to the customer entity
        # constructor.
        cust_info = Customer(*customer_record)
        return cust_info


    def update_customer_information(self, customer: Customer) -> Customer:
        sql = 'update "project0".customer set first_name = %s, last_name = %s ' \
              'where customer_id = %s returning customer_id'
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.customer_id))
        customer.customer_id = cursor.fetchone()[0]
        connection.commit()
        return customer


    def view_all_customers(self) -> list[Customer]:
        sql = 'select * from "project0".customer'
        cursor = connection.cursor()
        cursor.execute(sql)
        # We use the "fetchall()" method for the cursor object because we are fetching all the information instead of
        # just information that matches.
        customer_records = cursor.fetchall()
        customer_list = []
        for cust in customer_records:
            customer_list.append(Customer(*cust))
        return customer_list


    def delete_customer(self, customer_id: int) -> bool:
        sql = 'delete from "project0".customer where customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        return True