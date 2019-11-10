from .base_class import BaseClass

class Ride(BaseClass):
    def __init__(self, code, city_origin, state_origin, city_destination, state_destination, date, duration, vacancies, price):
        self.code = code
        self.city_origin = city_origin
        self.state_origin = state_origin
        self.city_destination = city_destination
        self.state_destination = state_destination
        self.date = date
        self.duration = duration
        self.vacancies = vacancies
        self.price = price
