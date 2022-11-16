import csv


def search_names():
    print("1. Поиск по имени")
    print("2. Поиск по фамилии")
    print("3. Поиск по номеру телефона")
    print("4. Возврат в меню")
    choise = input("Выберите опцию поиска: ")
    if choise == "1":
        s_name = input("Введите имя для поиска контакта: ")
        with open ("Phonebook.csv", encoding="utf-8") as f:
            f_reader = csv.reader(f, delimiter=",")
            for row in f_reader:
                if row[1] == s_name:
                    print(f'{row[0]} {row[1]} {row[2]} {row[3]}')
        search_names()
    if choise == "2":
        s_name = input("Введите Фамилию для поиска контакта: ")
        with open ("Phonebook.csv", encoding="utf-8") as f:
            f_reader = csv.reader(f, delimiter=",")
            for row in f_reader:
                if row[0] == s_name:
                    print(f'{row[0]} {row[1]} {row[2]} {row[3]}')
        search_names()
    if choise == "3":
        s_name = input("Введите номер телефона для поиска контакта: ")
        with open ("Phonebook.csv", encoding="utf-8") as f:
            f_reader = csv.reader(f, delimiter=",")
            for row in f_reader:
                if row[2] == s_name:
                    print(f'{row[0]} {row[1]} {row[2]} {row[3]}')
        search_names()
    if choise == "4":
        pass