from src.system import bd
from src.common.user import User
from src.common.account import Account
from src.common.reservation import Reservation
from src.common.lift import Lift

import datetime

users = bd.load('users')
accounts = bd.load('accounts')
lifts = bd.load('lifts')
reservations = bd.load('reservations')

user = User('111.111.111-11', 'Gabriel', '(61) 99964-0993', 'gabriel.lins97@gmail.com', '1234', 'admin')
user2 = User('lublinde', 'Luisa', '(61) 99964-0993', '', '1234', 'user')
account = Account('BRB', '1111-1x', 141516)
lift = Lift(1, user.user_cpf, 'BSB', 'DF', 'RJ', 'RJ', str(datetime.datetime.now()), '60', 4, 159.9)
reservation = Reservation(1, lift.lift_code, user2.user_cpf, 'Front2', False)

bd.append(user, users)
bd.append(user2, users)
bd.append(account, accounts)
bd.append(lift, lifts)
bd.append(reservation, reservations)