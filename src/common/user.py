from .base_class import BaseClass

class User(BaseClass):
    def __init__(self, cpf, name, telephone, email, password, access_level):
        self.pks = ['cpf']
        self.cpf = cpf
        self.name = name
        self.telephone = telephone
        self.email = email
        self.password = password
        self.access_level = access_level
