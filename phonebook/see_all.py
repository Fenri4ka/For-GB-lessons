import csv


def see_all():
    with open("Phonebook.csv", encoding="utf-8") as f:
        read_f = csv.reader(f, delimiter=",")
        for row in read_f:
            print(f'{row[0]} {row[1]} {row[2]} {row[3]}')