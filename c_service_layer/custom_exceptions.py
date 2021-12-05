
class WrongInformationException(Exception):
    def __init__(self, message: str):
        self.message = message



class DeletionErrorException(Exception):
    def __init__(self, message: str):
        self.message = message



class InsufficientFundsException(Exception):
    def __init__(self, message: str):
        self.message = message