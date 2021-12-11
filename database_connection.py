# Here in this module we have created a connection object that supports the connection between this program and the
# cloud database (in this case postgres). We used the pip install command to download a package called "psycopg[binary]"
# which allows us access to the connect object (and its custom exception called "OperationalError"). Psycopg handles a
# lot of the transactions for us back and forth from the database.

# This import gives us the "os.environ" mapping module so that we can interact with the software downloaded into our
# operating system (like DBeaver) by creating a dictionary with key/value pairs out of the environment variables used in
# the connection object.
import os
# This import gives us access to create a connection object and the keyword arguments so that we can use are environment
# variables to connect to the database.
from psycopg import connect, OperationalError


# This method creates a hard coded connection object which you use to plug in the same environment variables as you used
# with your database.
def create_connection():
    try:
        # This is the connection object creation.
        conn = connect(
            # HOST is the database link which is set inside either your computer path variables or it can be set through
            # the IDE you are using. We only use the environment variable names instead of the actual variable values
            # because then your username and password would be available to see for anyone looking at your project's
            # back end.
            host=os.environ.get("HOST"),
            # The DATABASE is the database version - in this case it is postgres.
            dbname=os.environ.get("DATABASE"),
            # The USER is your username you set up your database with.
            user=os.environ.get("USER"),
            # The PASSWORD is the password you set up your database with.
            password=os.environ.get("PASSWORD"),
            # The port is the port number the database is using. For this project, just the default 5432 was used.
            port=os.environ.get("PORT")
        )
        # If these database variables correctly connect this IDE to the database software (DBeaver) then the method will
        # return the "conn" connection object we can use in the implementing DAO layer of our project.
        return conn
    except OperationalError as o:
        # If this IDE and DBeaver are not connecting we will get the custom OperationalError exception.
        print(str(o))

# This will take the result of the method and store it into the variable container called "connection". This is what we
# reference in our DAO layer to connect with postgres and our database that will take in the variables we need to
# manipulate with the SQL language.
connection = create_connection()

# This print statement just helps us to make sure we are connecting correctly by printing out a pass or fail message.
print(connection)