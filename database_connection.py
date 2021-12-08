# Here in this module we have created a connection object that supports the connection between this program and the
# cloud database (in this case postgres).

import os
from psycopg import connect, OperationalError


def create_connection():
    try:
        conn = connect(
            host=os.environ.get("HOST"),
            dbname=os.environ.get("DATABASE"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
        )
        return conn
    except OperationalError as o:
        print(str(o))

connection = create_connection()
print(connection)