import time
contact = []


def new_contact():
    last_name = input("Введите фамилию: ")
    contact.append(last_name)
    name = input("Введите имя: ")
    contact.append(name)
    phone_number = ""
    flag = False
    while not flag:
        phone_number = input("Введите номер телефона: ")
        if len(phone_number) != 11 or not phone_number.isdigit():
            print("Номер телефона должен содержать 11 цифр")
        else:
            flag = True
    contact.append(phone_number)
    description = input("Введите описание: ")
    contact.append(description)
    return contact


def writing_csv():
    f = "Phonebook.csv"
    with open (f, 'a', encoding="utf-8") as data:
        data.write(f'{contact[0]},{contact[1]},{contact[2]},{contact[3]}\n')


def writing_txt():
    f = "Phonebook.txt"
    with open (f, "a", encoding="utf-8") as data:
        data.write(f'Фамилия: {contact[0]}\nИмя: {contact[1]}\nНомер телефона: {contact[2]}\nОписание: {contact[3]}\n\n')


def writing_log():
    f = "Log.txt"
    with open (f, "a", encoding="utf-8") as data:
        data.write(f'{contact[0]};{contact[1]};{contact[2]};{contact[3]}; {time.asctime()}\n')