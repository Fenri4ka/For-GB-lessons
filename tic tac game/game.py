import random
from build_field import build_field
from check_victory import check_victory
from write_resoults import *
import csv


def game():
    print("Добро пожаловать в игру Крестики-нолики!")
    build_field()
    name_1 = input("Как зовут первого игрока? ")
    name_2 = input("Какое имя второго игрока? ")
    m = random.randint(1, 101)
    step = 0
    counter = 0

    if m % 2 == 0:
        first = name_1
        second = name_2
    else:
        first = name_2
        second = name_1
    print(f"Сегодня удача на твоей стороне, {first}! Ты ходишь первым!")
    check_victory(field)
    while not check_victory(field):
        if step == 0 and counter != 9:
            counter += 1
            choice = input(f"Введите ячейку для хода, {first}: ")
            while not choice.isdigit() or int(choice) < 1 or int(choice) > 9 or (str(field[int(choice) - 1]) in 'XO'):
                choice = input(f"Введите корректный номер ячейки, {first}: ")
            else:
                field[int(choice) - 1] = "X"
                build_field()
                step = 1
        if check_victory(field):
            pass
        else:
            if step == 1 and counter != 9:
                counter += 1
                choice = input(f"Введите ячейку для хода, {second}: ")
                while not choice.isdigit() or int(choice) < 1 or int(choice) > 9 or (
                        str(field[int(choice) - 1]) in 'XO'):
                    choice = input(f"Введите корректный номер ячейки, {second}: ")
                else:
                    field[int(choice) - 1] = "O"
                    build_field()
                    step = 0
        if counter == 9:
            if not check_victory(field):
                print("Победила дружба!")
                break
    if check_victory(field):
        if step == 1:
            print(f"{first} победил(а)!")
            flag = False
            with open('Ladder.csv', encoding='utf-8') as f:
                f_reader = csv.reader(f, delimiter=",")
                for row in f_reader:
                    if row[0] == first:
                        write_ladder(first)
                        flag = True
                if not flag:
                    with open('Ladder.csv', 'a', encoding='utf-8') as data:
                        data.write(f'{first},1\n')              
        if step == 0:
            print(f"{second} победил(а)!")
            flag = False
            with open('Ladder.csv', encoding='utf-8') as f:
                f_reader = csv.reader(f, delimiter=",")
                for row in f_reader:
                    if row[0] == second:
                        write_ladder(second)
                        flag = True
                if not flag:
                    with open('Ladder.csv', 'a', encoding='utf-8') as data:
                        data.write(f'{second},1\n')