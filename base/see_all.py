import easygui
import os
import csv

file_path = "Base.csv"


def see_all():
    with open(file_path, encoding='utf-8') as f:
        read_f = csv.reader(f, delimiter=",")
        title = os.path.basename(file_path)
        msg = "База самых лучших товаров"
        text = ''
        for row in read_f:
            text += f'Артикул: {row[0]}\nНаименование: {row[1]}\nКод номенклатурной группы: {row[2]}\nНоменклатурная группа: {row[3]}\nЦена(руб): {row[4]}\n\n'
        easygui.textbox(msg, title, text[155:])
