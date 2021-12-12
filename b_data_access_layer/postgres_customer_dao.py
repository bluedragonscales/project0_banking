# This module contains the implemented DAO layer class, and it provides the main functionality for the program. It is
# used to pass the Customer object through methods that do specific tasks the program needs for its interface.

# This import contains the blueprint we created for the Customer object.
from a_entities.customer import Customer
# This import contains the abstract class so this implementing class can inherit the needed methods.
from b_data_access_layer.abstract_customer_dao import CustomerDAO
# This import contains the connection object that was created so these implemented methods can react with the cloud
# database. In this program, we connect with a postgres database through Amazon Web Services (AWS).
from database_connection import connection



class CustomerPostgresDAO(CustomerDAO):

    # This is the implementation to create a customer object. It has two parameters: "self" to connect it with this
    # class and "customer" which is a new object that comes from the API. This method is activated when the API sends a
    # dictionary of correct information to match the customer object blueprint. After it comes to the server, it goes
    # through the service layer to catch any API user errors, and then makes it to this method which passes it to the
    # database.
    def create_customer(self, customer: Customer) -> Customer:
        # Because we are connected to the postgres database and want to interact with it, we need to send it commands it
        # knows how to read. The below sql statement is exactly what it would use to create a customer, using the "%s"
        # in the places where we pass information to. "%s" is a type of place holder for the "first_name" and the
        # "last_name" variables that are given as arguments to the customer object parameters before they end up here.
        # The "default" is used as the third argument, "customer_id", because postgres will auto create this value.
        # Finally, once argument values are passed to this statement, it is stored in the variable container "sql".
        sql = 'insert into "project0".customer values(%s, %s, default) returning customer_id'
        # We use our connection object (imported above) to call the "cursor()" function. This cursor function allows us
        # to submit sql statements in the form of strings and have it interact properly with our database. We've stored
        # this cursor functionality in a variable named "cursor" which we do for each method because each method will
        # have different use for the cursor variable. Some methods will need to close it and some will need to leave it
        # running.
        cursor = connection.cursor()
        # We use our variable called "cursor" to call the "execute()" function, through which we pass the sql statement
        # that will be used in postgres, and we also pass in the arguments we need to finish the statement, that will
        # complete out all the instances of "%s". If there is only one instance of "%s" then we should pass it in the
        # form of a list, if there are more than one then we pass it in the form of a tuple. The "execute()" function
        # takes in these arguments and turns it into a viable statement for postgres to execute. The arguments should be
        # passed in the same order as the sql statement needs them.
        cursor.execute(sql, (customer.first_name, customer.last_name))
        # Our DAO test for this method requires that we know what this new customer's id is so we have to isolate and
        # store that information. Calling the "fetchone()" method with our cursor object will fetch one piece of
        # information from postgres in an iterable data structure. Since we're returning just one piece of information
        # in our sql statement we will fetch the first index, index 0. This stores that fetched value into the variable
        # container called "customers_id". The requested index is outside of the function parentheses. We call the
        # function and THEN we specify the index of the value we want.
        customers_id = cursor.fetchone()[0]
        # Since the postgre database is in charge of assigning the value to the customer_id field, it is not yet
        # assigned in the object this method creates so the returning customer object for this method will not have
        # access to the id value until it is assigned here by taking the fetched id value above and assigning it to the
        # customer object's customer_id field.
        customer.customer_id = customers_id
        # When using insert, update, or delete sql statements we need to call the "commit()" function with the
        # connection object so that those changes to the tables will be saved, and also the cursor object will close
        # out so it doesn't interact with anything further than what it's supposed to.
        connection.commit()
        # Because the API expects to receive all the information necessary to create the customer, the whole customer
        # must be returned from the method even though our test only specifies that it needs the customer_id value. The
        # new customer object is returned to the database (not to the API because the request was only to create, not to
        # view the creation).
        return customer



    # This is the DAO method to retrieve information about a specific customer. It contains the "self" parameter and an
    # integer parameter, which we have named "customer_id" for readability because the customer id is what is sent from
    # the API so the server knows which customer information to look up.
    def get_customer_information(self, customer_id: int) -> Customer:
        # This is the exact PostgreSQL statement needed in the postgres database to retrieve specific information. The
        # integer argument named "customer_id" is passed into the method through the parameter and fills in the
        # placeholder "%s".
        sql = 'select * from "project0".customer where customer_id = %s'
        # We've now opened up a cursor with our connection object to channel strings to the database.
        cursor = connection.cursor()
        # The execute function is taking in the stored sql statement and the single piece of information needed to fill
        # the "%s" placeholder. It's just one piece of information so we use a list instead of a tuple.
        cursor.execute(sql, [customer_id])
        # We use the "fetchone()" function because we are fetching one row of information, but we need all the columns
        # in this one row so we do not specify an index position. We store this tuple of information inside the variable
        # container called "customer_record".
        customer_record = cursor.fetchone()
        # We pass the tuple stored inside "customer_record" through the customer object blueprint. Because the tuple
        # that was fetched is in the correct order of information needed by the customer object blueprint parameters,
        # the parameters are assigned one by one into the created customer object called "cust_info".
        cust_info = Customer(*customer_record)
        # The created customer object called "cust_info" is then returned to the front end API via the RESTful web
        # service as a jsonified dictionary.
        return cust_info



    # This is the implementation method to update the information of a customer that has already been created. The API
    # user sends the server a PATCH request with a body of new information. It has the "self" parameter to refer to the
    # class itself, and it has the parameter of object to pass in a customer object.
    def update_customer_information(self, customer: Customer) -> Customer:
        # This is the postgres statement to update information in a table. All variables of the customer object can be
        # changed (in this case there are only two variables) where the id of the passed in customer object matches the
        # database table row.
        sql = 'update "project0".customer set first_name = %s, last_name = %s where customer_id = %s'
        cursor = connection.cursor()
        # The execute function channels the sql statement along with the information from the API request body to fill
        # it out into the database to make the changes.
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.customer_id))
        # This commits the changes and closes the connection so it doesn't interfere with any other information.
        connection.commit()
        # The customer object with the new information is passed to the database (not to the API because the API only
        # requested a change, not the ability to view that change).
        return customer



    # This is the implementation method to view the whole list of customers that is listed in the database. It needs no
    # parameters except for the "self" parameter because all the information is being returned with no constraints on
    # how it is ordered or grouped. The API user sends the server a request that has no body of information.
    def view_all_customers(self) -> list[Customer]:
        # This statement does not need any information passed into it and it does not receive any body information from
        # the API front end so the execute function only takes the sql statement as an argument.
        sql = 'select * from "project0".customer'
        cursor = connection.cursor()
        cursor.execute(sql)
        # We use the "fetchall()" method for the cursor object because we are fetching all the information instead of
        # just information that matches the sql statement.
        customer_records = cursor.fetchall()
        # We start a list so that all the customer objects can be entered into a list.
        customer_list = []
        # One by one, each customer row in the database is turned into a tuple and then passed into "Customer(*cust)" as
        # a full object that is then appended to the customer object list. Then the next row/customer information tuple
        # is passed in and appended.
        for cust in customer_records:
            customer_list.append(Customer(*cust))
        # The list with all of the appended customer objects is returned to the front end API.
        return customer_list



    # This is the implemented method to delete a customer. It contains the "self" parameter and an integer parameter we
    # have named "customer_id" for readability because the API request will specify which customer to delete based on
    # which defined customer_id is included in the request.
    def delete_customer(self, customer_id: int) -> bool:
        # The request includes the id information and it gets passed into the sql statement and the execute method. WHY
        # IS THERE NO BODY BUT THE METHOD STILL KNOWS WHAT CUSTOMER TO DELETE BY THE SIGNAL FROM THE FRONT END?
        sql = 'delete from "project0".customer where customer_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        # No information needs to be returned so we just return True to notify the API that the deletion has been done.
        return True