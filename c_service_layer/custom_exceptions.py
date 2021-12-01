class WrongInformationException(Exception):
    def __init__(self, message: str):
        self.message = message



class AlreadyDeletedException(Exception):
    def __init__(self, message: str):
        self.message = message



class DuplicateInformationException(Exception):
    def __init__(self, message: str):
        self.message = message


class DuplicateCustomerException(Exception):
    def __init__(self, message: str):
        self.message = message