"""
Создайте программу для игры в ""Крестики-нолики"".
"""
import random

print("Добро пожаловать в игру Крестики-нолики!")
field = list(range(1, 10))
print("*" * 13)


def build_field():
    for i in range(3):
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print("*" * 13)


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


def check_victory(field):
    victory = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in victory:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return True
    return False


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
            while not choice.isdigit() or int(choice) < 1 or int(choice) > 9 or (str(field[int(choice) - 1]) in 'XO'):
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
    if step == 0:
        print(f"{second} победил(а)!")
