from .base_class import BaseClass

class Account(BaseClass):
    pks = ['bank', 'agency', 'number']
    
    def __init__(self, bank, agency, number, user_cpf):
        self.bank = bank
        self.agency = agency
        self.number = number
        self.user_cpf = user_cpf
