from src.system import bd
from src.common.user import User
from src.common.account import Account
from src.common.reservation import Reservation
from src.common.lift import Lift

import datetime

user = User('111.111.111-11', 'Gabriel', '(61) 99964-0993', 'gabriel.lins97@gmail.com', '1234')
account = Account('BRB', '1111-1x', 141516)
reservation = Reservation(1, 'Front2', False)
lift = Lift(1, 'BSB', 'DF', 'RJ', 'RJ', str(datetime.datetime.now()), '60', 4, 159.9)
print(user.serialyze())
print(account.serialyze())
print(reservation.serialyze())
print(lift.serialyze())

user2 = User('111.111.111-11', 'Gabriel', '(61) 99964-0993', 'gabriel.lins97@gmail.com', '1234')
print(user == user2)

users = bd.load('users')
accounts = bd.load('accounts')
lifts = bd.load('lifts')
reservations = bd.load('reservations')
bd.append(user, users)
bd.append(account, accounts)
bd.append(lift, lifts)
bd.append(reservation, reservations)