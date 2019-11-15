from .base_class import BaseClass

class User(BaseClass):
    pks = ['user_cpf']
    
    def __init__(self, user_cpf, name, telephone, email, password, access_level):
        self.user_cpf = user_cpf
        self.name = name
        self.telephone = telephone
        self.email = email
        self.password = password
        self.access_level = access_level
