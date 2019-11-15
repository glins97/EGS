from src.system import bd, display
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
            print('Descadastro concluído.')
            return True
        elif (len(user_lifts)):
            print('Falha ao descadastrar: usuário possui {} caronas'.format(len(user_lifts)))
        elif (len(user_reservations)):
            print('Falha ao descadastrar: usuário possui {} reservas'.format(len(user_reservations)))

        return False

    def request_state_menu(self):
        menus = {
            STATE_NOT_AUTHED: {
                'Mostrar caronas': lambda: display._print_list(self.tables['lifts'], 'Caronas disponíveis:'),
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
                'Mostrar caronas': lambda: display._print_list(self.tables['lifts'], 'Caronas disponíveis:'),
                'Pesquisar carona': lambda: display._print_list(
                    bd.select(
                        display.request_details(['city_origin', 'state_origin', 'city_destination', 'state_destination']), self.tables['lifts']
                    ),
                    'Caronas encontradas:'
                ),
                'Registrar carona': lambda: print('@RegistrarCarona'),
                'Retirar carona': lambda: print('@RetirarCarona'),
                'Registrar reserva': lambda: print('@RegistrarReserva'),
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