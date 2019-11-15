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

user = User('admin', 'Gabriel', '(61) 99964-0993', 'gabriel.lins97@gmail.com', '', 'admin')
user2 = User('user', 'Luisa', '(61) 99964-0993', '', '', 'user')
account = Account('BRB', '1111-1x', 141516, user.user_cpf)
account2 = Account('BRB', '1111-2x', 171819, user.user_cpf)
lift = Lift(1, user.user_cpf, 'BSB', 'DF', 'RJ', 'RJ', str(datetime.datetime.now()), 60, 4, 159.9)
reservation = Reservation(1, lift.lift_code, user2.user_cpf, 'Front2', False)

bd.append(user, users)
bd.append(user2, users)
bd.append(account, accounts)
bd.append(account2, accounts)
bd.append(lift, lifts)
bd.append(reservation, reservations)