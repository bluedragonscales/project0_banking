class WrongInformationException(Exception):
    def __init__(self, message: str):
        self.message = message



class DoesNotExistException(Exception):
    def __init__(self, message: str):
        self.message = message



class DuplicateInformationException(Exception):
    def __init__(self, message: str):
        self.message = message


class DuplicateCustomerException(Exception):
    def __init__(self, message: str):
        self.message = message


class InsufficientFundsException(Exception):
    def __init__(self, message: str):
        self.message = message