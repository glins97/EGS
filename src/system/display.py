from src.system import bd
import json
translations = bd.load('translations')

def request_details(attrs):
    response = {}
    for attr in attrs:
        response[attr] = input('Valor para {}: '.format(translations[attr]))
    return response

def process_menu_choice(menu):
    keys = sorted(menu.keys())
    choice = request_choice(keys)
    if choice:
        menu[keys[choice - 1]]() 

    return choice

def request_choice(options, title='Por favor, escolha uma opção:'):
    mi = 1
    ma = len(options)
    print(title)
    print('  0. Parar')
    for index, option in enumerate(options):
        print('  {}. {}'.format(index + 1, option))

    choice = int(input('Escolha: '))
    while choice < mi or choice > ma:
        if choice == 0:
            return choice
        choice = int(input('Escolha inválida. Tente novamente: '))
    print()
    return choice 

def request_login():
    print('Entre com seu CPF e sua senha.')
    return input('  CPF: '), input('  Senha: ')

def _print_list(l, title=''):
    print(title)
    for index, item in enumerate(l):
        print('  {}. {}'.format(index + 1, item))
    if len(l) == 0:
        print("  Sem resultados.")
    print()