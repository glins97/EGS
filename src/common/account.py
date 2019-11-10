from .base_class import BaseClass

class Account(BaseClass):
    def __init__(self, code, bank, agency, number):
        self.code = code
        self.bank = bank
        self.agency = agency
        self.number = number
