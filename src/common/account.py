from .base_class import BaseClass

class Account(BaseClass):
    def __init__(self, bank, agency, number):
        self.pks = ['bank', 'agency', 'number']
        self.bank = bank
        self.agency = agency
        self.number = number
