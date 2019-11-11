
def request_main_menu_choice():
    options = [
        'Show all users',
        'Show all accounts',
        'Show all lifts',
        'Show all reservations',
    ]
    return request_choice(options)

def request_choice(options):
    mi = 1
    ma = len(options)
    print('Please choose one of the following:')
    print('  0. Return')
    for index, option in enumerate(options):
        print('  {}. {}'.format(index + 1, option))

    choice = int(input('Your choice: '))
    while choice < mi or choice > ma:
        if choice == 0:
            return choice
        choice = int(input('Invalid choice. Try again: '))
    print()
    return choice 

def _print_list(l, title=''):
    print(title)
    for index, item in enumerate(l):
        print('  {}. {}'.format(index + 1, item))
    print()