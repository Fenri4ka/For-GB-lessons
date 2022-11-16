from new_contact import *
from see_all import see_all
from os.path import exists
from creating import creating_csv
from search_names import search_names
path = "Phonebook.csv"
flag = exists(path)
if not flag:
    creating_csv()


def main_menu():
    print("Добро пожаловать в телефонный справочник!")
    print("1. Поиск контакта")
    print("2. Посмотреть все контакты")
    print("3. Запись нового контакта")
    print("4. Выход")
    choise = input("Выберите пукт меню: ")
    if choise == "1":
        search_names()
        main_menu()
    if choise == "2":
        see_all()
        main_menu()
    if choise == "3":
        new_contact()
        writing_csv()
        writing_txt()
        writing_log()
        main_menu()
    if choise == "4":
        print("Спасибо за использование телефонного справочника. Хорошего дня!")

main_menu()