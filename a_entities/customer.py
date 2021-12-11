# This is the class that is the blueprint for all customer objects. Its "__init__" method acts as a constructor and
# assigns these values every time a Customer object is created. There are four parameters in its constructor method
# that must be fulfilled.

# The "self" parameter requires no arguments upon object creation. It only acts as a label to say that it is connected
# to the specific blueprint. The last three parameters do require arguments. The "first_name" and "last_name" are type
# annotated as strings, so strings are expected and you will throw an error if you pass any other data type to them. The
# last parameter is type annotated as an int so an int argument should be passed to it.

# Once these parameter arguments are fulfilled correctly, the Customer object will be created and will carry these
# values that are now stored in their memory address.

class Customer:
    def __init__(self, first_name: str, last_name: str, customer_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.customer_id = customer_id

    def customer_dictionary(self):
        return {
            "firstName" : self.first_name,
            "lastName" : self.last_name,
            "customerId" : self.customer_id
        }


# Inside this blueprint for Customer objects, is a method to make a dictionary out of the values that the Customer
# object was initialized with. The most common way to pass information from server to web and back is via JSON.
# JavaScript Object Notations can hold strings, ints, and boolean data types, but to pass them back and forth between
# web and server they must be in the form of strings, dictionaries, or tuples while they're being passed.

# Here in this Customer object blueprint the dictionary that can be passed between web and server will contain both
# strings and integers. Because a JSON is based on the front end web language called JavaScript, we put the dictionary
# keys in "camel case" which is common convention for JavaScript.