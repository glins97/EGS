from .base_class import BaseClass

class Reservation(BaseClass):
    pks = ['reservation_code']
    
    def __init__(self, reservation_code, lift_code, user_cpf, seat, bagage):
        self.reservation_code = reservation_code
        self.lift_code = lift_code
        self.user_cpf = user_cpf
        self.seat = seat
        self.bagage = bagage
