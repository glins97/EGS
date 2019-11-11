from src.system import bd, display

CHOICE_QUIT = 0
STATE_NOT_AUTHED = 0
STATE_AUTHED = 1



class System(object):
    def __init__(self):
        self.tables = {}
        self.authed = False
        self.state = STATE_NOT_AUTHED 

    def load(self):
        for name in ['users', 'lifts', 'reservations', 'accounts']:
            self.tables[name] = bd.load(name)

    def do_login(self):
        retries = 3
        for _ in range(retries):
            self.authed = bd.auth(*display.request_login(), self.tables['users'])
            if self.authed:
                self.state = STATE_AUTHED
                print('Login bem sucedido.\n')
                break
            else:
                print('Login mal sucedido.\n')

    def request_state_menu(self):
        menus = {
            STATE_NOT_AUTHED: {
                'Mostrar caronas disponíveis': lambda: display._print_list(self.tables['lifts'], 'Caronas disponíveis:'),
                'Pesquisar carona disponível': lambda: print('SYSTEM::SEARCH AVAILABLE LIFTS'),
                'Login': self.do_login,
            },
            STATE_AUTHED: {
            },

        }

        return menus[self.state]


    def run(self):
        if self.tables == {}:
            self.load()

        choice = 1
        while choice != CHOICE_QUIT:
            choice = display.process_menu_choice(
                self.request_state_menu()
            )