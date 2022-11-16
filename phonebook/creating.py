def creating_csv():
    f = "Phonebook.csv"
    with open(f, "w", encoding="utf-8") as data:
        data.write(f'Фамилия,Имя,Номер телефона,Описание\n')