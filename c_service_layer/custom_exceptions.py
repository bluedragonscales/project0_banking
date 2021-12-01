class DuplicateCustomerIdException(Exception):
    def __init__(self, message: str):
        self.message = message



class AlreadyDeletedException(Exception):
    def __init__(self, message: str):
        self.message = message



class DuplicateBankAccountException(Exception):
    def __init__(self, message: str):
        self.message = message