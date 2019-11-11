from src.system import bd, display

class System(object):
    def __init__(self):
        self.tables = {}

    def load(self):
        for name in ['users', 'lifts', 'reservations', 'accounts']:
            self.tables[name] = bd.load(name)

    def run(self):
        if self.tables == {}:
            self.load()

        funcs = {
            0: lambda: print('quitting'),
            1: lambda: display._print_list(self.tables['users'], 'Registered users:'),
            2: lambda: display._print_list(self.tables['accounts'], 'Registered accounts:'),
            3: lambda: display._print_list(self.tables['lifts'], 'Registered lifts:'),
            4: lambda: display._print_list(self.tables['reservations'], 'Registered reservations:'),
        }
        choice = display.request_main_menu_choice()
        while choice != 0:
            funcs[choice]()
            choice = display.request_main_menu_choice()