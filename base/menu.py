import easygui
from see_all import see_all
from search_smth import search_smth
from new_art import add_art
from change_smth import change_price
from delete_smth import del_art


def main_menu():
    out = easygui.buttonbox('Добро пожаловать!', 'Меню', ('Просмотреть все артикулы', 'Добавить артикул', 'Найти артикул', 'Изменить цену', 'Удалить артикул'))
    if out == 'Просмотреть все артикулы':
        see_all()
        main_menu()
    if out == 'Добавить артикул':
        add_art()
        main_menu()
    if out == 'Найти артикул':
        search_smth()
        main_menu()
    if out == 'Изменить цену':
        change_price()
        main_menu()
    if out == 'Удалить артикул':
        del_art()
        main_menu()


main_menu()