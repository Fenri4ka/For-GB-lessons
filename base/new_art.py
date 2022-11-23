import time
import easygui


def add_art():
    field_names = ['Артикул', 'Наименование', 'Код номенклатурной групппы', 'Наименование номенклатурной группы', 'Цена(руб)']
    new_art = easygui.multenterbox("Заполните информацию об артикуле:", "Новый артикул", field_names)
    for i in range(len(new_art)):
        if new_art[i] == "":
            err_msg = 'Заполните ВСЕ поля!'
            new_art = easygui.multenterbox(err_msg, "Новый артикул", field_names)
    else:
        with open('Base.csv', 'a', encoding='utf-8') as f:
            f.write(f'{new_art[0]},{new_art[1]},{new_art[2]},{new_art[3]},{new_art[4]},0,0,0,0,0,0\n')
        easygui.msgbox(f'Артикул {new_art[0]} успешно внесён в базу', ok_button="Вернуться в меню")
        with open('Log.txt', "a", encoding="utf-8") as data:
            data.write(f'Добавление артикула {new_art[0]};{new_art[1]};{new_art[2]};{new_art[3]};{time.asctime()}\n')
