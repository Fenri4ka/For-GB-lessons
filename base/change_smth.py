import pandas as pd
import easygui


def change_price():
    art = easygui.enterbox("Пожалуйста, введите артикул:", "Изменение цены")
    price = easygui.enterbox("Пожалуйста, введите новую цену:", "Изменение цены")
    df = pd.read_csv("Base.csv", encoding='utf-8', index_col='Артикул')
    df.loc[int(art), 'Цена(руб)'] = price
    df.to_csv("Base.csv", encoding='utf-8')
    easygui.msgbox('Цена успешно изменена!', ok_button="Вернуться в меню")
