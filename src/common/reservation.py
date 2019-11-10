from .base_class import BaseClass

class Reservation(BaseClass):
    def __init__(self, code, seat, bagage):
        self.code = code
        self.seat = seat
        self.bagage = bagage
