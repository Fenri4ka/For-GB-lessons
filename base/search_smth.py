import csv
import easygui


def search_smth():
    out = easygui.buttonbox('Выберите функцию поиска', 'Меню поиска', ('Поиск по артикулу', 'Поиск по номенклатурной группе', 'Поиск по коду номенклатурной группы'))
    if out == 'Поиск по артикулу':
        art = easygui.enterbox("Пожалуйста, введите артикул для поиска:", "Поиск по артикулу")
        title = f'Артикул: {art}'
        msg = f'Данные артикула {art}'
        text = ''
        sales_money = ''
        sales_pcs = ''
        with open("Base.csv", encoding="utf-8") as f:
            f_reader = csv.reader(f, delimiter=",")
            for row in f_reader:
                if row[0] == art:
                    sales_money = (round((int(row[4])*float(row[5])+int(row[4])*float(row[6])+int(row[4])*float(row[7])+int(row[4])*float(row[8])+int(row[4])*float(row[9])+int(row[4])*float(row[10]))/6))
                    sales_pcs = (round((float(row[5])+float(row[6])+float(row[7])+float(row[8])+float(row[9])+float(row[10]))/6))
                    text = f'Артикул: {row[0]}\nНаименование: {row[1]}\nКод номеклатуры: {row[2]}\nНоменклатурная группа: {row[3]}\nЦена(руб): {row[4]}\nСредние продажи за 6 мес(руб): {sales_money}\nСредние продажи за 6 мес(шт): {sales_pcs}\n\n'
        easygui.textbox(msg, title, text)
    if out == 'Поиск по номенклатурной группе':
        art = easygui.enterbox("Пожалуйста, введите номенклатурную группу:", "Поиск по номеклатурной группе")
        title = f'Номенклатурная группа: {art}'
        msg = f'Артикулы номенклатурной группы {art}'
        text = ''
        sales_money = ''
        sales_pcs = ''
        with open("Base.csv", encoding="utf-8") as f:
            f_reader = csv.reader(f, delimiter=",")
            for row in f_reader:
                if row[3] == art:
                    sales_money = (round((int(row[4])*float(row[5])+int(row[4])*float(row[6])+int(row[4])*float(row[7])+int(row[4])*float(row[8])+int(row[4])*float(row[9])+int(row[4])*float(row[10]))/6))
                    sales_pcs = (round((float(row[5])+float(row[6])+float(row[7])+float(row[8])+float(row[9])+float(row[10]))/6))
                    text += f'Артикул: {row[0]}\nНаименование: {row[1]}\nКод номеклатуры: {row[2]}\nНоменклатурная группа: {row[3]}\nЦена(руб): {row[4]}\nСредние продажи за 6 мес(руб): {sales_money}\nСредние продажи за 6 мес(шт): {sales_pcs}\n\n'
        easygui.textbox(msg, title, text)
    if out == 'Поиск по коду номенклатурной группы':
        art = easygui.enterbox("Пожалуйста, введите код номенклатурной группы:", "Поиск по коду номеклатурной группы")
        title = f'Код номенклатурной группы: {art}'
        msg = f'Артикулы номенклатурной группы {art}'
        text = ''
        sales_money = ''
        sales_pcs = ''
        with open("Base.csv", encoding="utf-8") as f:
            f_reader = csv.reader(f, delimiter=",")
            for row in f_reader:
                if row[2] == art:
                    sales_money = (round((int(row[4])*float(row[5])+int(row[4])*float(row[6])+int(row[4])*float(row[7])+int(row[4])*float(row[8])+int(row[4])*float(row[9])+int(row[4])*float(row[10]))/6))
                    sales_pcs = (round((float(row[5])+float(row[6])+float(row[7])+float(row[8])+float(row[9])+float(row[10]))/6))
                    text += f'Артикул: {row[0]}\nНаименование: {row[1]}\nКод номеклатуры: {row[2]}\nНоменклатурная группа: {row[3]}\nЦена(руб): {row[4]}\nСредние продажи за 6 мес(руб): {sales_money}\nСредние продажи за 6 мес(шт): {sales_pcs}\n\n'
        easygui.textbox(msg, title, text)