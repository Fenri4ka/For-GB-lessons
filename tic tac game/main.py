from game import game
from write_resoults import see_ladder

def main_menu():
    print('Добро пожаловать в игру "Крестики-нолики"')
    print('1. Новая игра')
    print('2. Посмотреть доску почета')
    print('3. Выход')
    choice = input('Выберете пункт меню: ')
    if choice == '1':
        game()
        main_menu()
    if choice == '2':
        see_ladder()
        main_menu()
    if choice == '3':
        print('Отлично сыграно! Хорошего дня!')


main_menu()