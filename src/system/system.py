from src.system import bd, display
from src.common.account import Account
from src.common.user import User
from src.common.lift import Lift
from src.common.reservation import Reservation
import time
import os

CHOICE_QUIT = 0
STATE_NOT_AUTHED = 0
STATE_AUTHED = 1

class System(object):
    def __init__(self):
        self.tables = {}
        self.authed = False
        self.authed_user = None
        self.state = STATE_NOT_AUTHED 

    def load(self):
        for name in ['users', 'lifts', 'reservations', 'accounts']:
            self.tables[name] = bd.load(name)

    def do_login(self):
        retries = 3
        for _ in range(retries):
            user, pw = display.request_login()
            print('user', user, 'pw', pw)
            self.authed = bd.auth(user, pw, self.tables['users'])
            if self.authed:
                self.state = STATE_AUTHED
                self.authed_user = user
                print('Login bem sucedido.\n')
                break
            else:
                print('Login mal sucedido.\n')

    def do_register(self):
        obj = dict({'access_level': 'user'}, **display.request_details(['name', 'telephone', 'cpf', 'password', 'email']))
        bd.append(
            obj, self.tables['users'], 'users'
        )
    
    def do_unregister(self):
        user_lifts = bd.select({'user_cpf': self.authed_user}, self.tables['lifts'])
        user_reservations = bd.select({'user_cpf': self.authed_user}, self.tables['reservations'])
        if len(user_lifts) == 0 and len(user_reservations) == 0:
            self.state = STATE_NOT_AUTHED
            self.authed = False
            self.authed_user = None
            for user in self.tables['users']:
                if user['cpf'] == self.authed_user:
                    self.tables['users'].remove(user)

            print('Descadastro concluído.')
            return True
        elif (len(user_lifts)):
            print('Falha ao descadastrar: usuário possui {} caronas'.format(len(user_lifts)))
        elif (len(user_reservations)):
            print('Falha ao descadastrar: usuário possui {} reservas'.format(len(user_reservations)))

        return False

    def do_add_lift(self):
        details = display.request_details([
                'city_origin',
                'state_origin',
                'city_destination',
                'state_destination',
                'duration',
                'vacancies',
                'price',            
            ])
        details['price'] = float(details['price'])
        details['vacancies'] = int(details['vacancies'])
        details['duration'] = int(details['duration'])
        details[Lift.pks[0]] = self.tables['lifts'][-1][Lift.pks[0]] + 1
        
        bd.append(
            dict({'user_cpf': self.authed_user}, **details), self.tables['lifts'], 'lifts'
        )

    def do_remove_lift(self):
        user_lifts = bd.select({'user_cpf': self.authed_user}, self.tables['lifts'])
        if len(user_lifts) == 0:
            print("Sem caronas cadastradas pelo usuário.")
        
        lift_index = display.request_choice(user_lifts, title='Escolha uma carona para desregistrar:')
        if not lift_index:
            return False
        lift = user_lifts[lift_index - 1]

        reservations = bd.select({'lift_code': lift['lift_code']}, self.tables['reservations'])
        if len(reservations) > 0:
            print("Carona já tem passageiro, não pode ser removida.")
            return False

        self.tables['lifts'].remove(lift)
        bd.commit(self.tables['lifts'], 'lifts')
        return True

    def do_register_reservation(self):
        available_lifts = [lift for lift in self.tables['lifts'] if lift['vacancies'] > 0]
        choice = display.request_choice(available_lifts, "Escolha uma das caronas abaixo:")
        
        details = display.request_details(['assento', 'bagage'])
        details['bagage'] = True if details['bagage'].lower() == "sim" else False
        details['lift_code'] = available_lifts[choice - 1]['lift_code']
        details['user_cpf'] = self.authed_user
        details[Reservation.pks[0]] = self.tables['reservations'][-1][Reservation.pks[0]] + 1
        
        bd.append(details, self.tables['reservations'], 'reservations')

    def request_state_menu(self):
        menus = {
            STATE_NOT_AUTHED: {
                'Mostrar caronas': lambda: display._print_list(self.tables['lifts'], 'Caronas registradas:'),
                'Pesquisar carona': lambda: display._print_list(
                    bd.select(
                        display.request_details(['city_origin', 'state_origin', 'city_destination', 'state_destination']), self.tables['lifts']
                    ),
                    'Caronas encontradas:'
                ),
                'Login': self.do_login,
                'Cadastrar': self.do_register,
            },

            STATE_AUTHED: {
                'Descadastrar': self.do_unregister,
                'Mostrar caronas': lambda: display._print_list(self.tables['lifts'], 'Caronas registradas:'),
                'Pesquisar carona': lambda: display._print_list(
                    bd.select(
                        display.request_details(['city_origin', 'state_origin', 'city_destination', 'state_destination']), self.tables['lifts']
                    ),
                    'Caronas encontradas:'
                ),
                'Registrar carona': self.do_add_lift,
                'Retirar carona': self.do_remove_lift,
                'Registrar reserva': self.do_register_reservation,
                'Retirar reserva': lambda: print('@RetirarReserva'),
            },
        
        }

        return menus[self.state]


    def run(self):
        os.system('clear')
        if self.tables == {}:
            self.load()

        choice = 1
        while choice != CHOICE_QUIT:
            try:
                choice = display.process_menu_choice(
                    self.request_state_menu()
                )
                if choice != 0:
                    input("Pressione [ENTER] para continuar")
                    os.system('clear')
            except Exception as e:
                print(repr(e))
                continue