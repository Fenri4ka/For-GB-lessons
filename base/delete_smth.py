import pandas as pd
import easygui


def del_art():
    art = easygui.enterbox("Пожалуйста, введите артикул:", "Изменение цены")
    df = pd.read_csv("Base.csv", encoding='utf-8', index_col='Артикул')
    df = df.drop(int(art))
    df.to_csv("Base.csv", encoding='utf-8')
    easygui.msgbox('Артикул успешно удален из базы!', ok_button="Вернуться в меню")