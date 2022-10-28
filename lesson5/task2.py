"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
"""
import random
print("Добро пожаловать в копитал-шоу Сундук конфет! "
      "\nПравила игры: в сундуке лежат конфеты, чьё количество задано игроками. "
      "\nИгроки ходят по очереди, право первого хода определяется жеребьёвкой. "
      "\nОдин игрок за раз может взять из сундука не меньше 1 и не больше 28 конфет. "
      "\nСделавшему последний ход достаются все конфеты =)")
print()
n = input("Введите количество конфет в сундуке: ")
max_candies = 28
while not n.isdigit() or int(n) < max_candies + 2:
    n = input(f"Мы столько не разыграем =( Введи число хотя бы от {max_candies+2}: ")
else:
    n = int(n)
    print(f"Отлично! В сундуке {n} конфет. Теперь введите имена игроков.")
name_1 = input("Как зовут первого игрока? ")
name_2 = input("Какое имя второго игрока? ")
m = random.randint(1,101)
flag = 0
if m % 2 == 0:
    first = name_1
    second = name_2
else:
    first = name_2
    second = name_1
print(f"Сегодня удача на твоей стороне, {first}! Ты ходишь первым!")
while n > max_candies:
    if flag == 0:
        take = input(f"Сколько конфет возьмешь из сундука, {first}? ")
        while not take.isdigit() or int(take) > max_candies or int(take) < 1:
            take = input(f"Хитро, но нет. Можно взять не менее 1 и не более {max_candies} конфет. Твой ход: ")
        else:
            n -= int(take)
    if n > max_candies:
        print(f"В сундуке осталось {n} конфет.")
        flag = 1
    if flag == 1:
        take = input(f"Сколько конфет возьмешь из сундука, {second}? ")
        while not take.isdigit() or int(take) > max_candies or int(take) < 1:
            take = input(f"Хитро, но нет. Можно взять не менее 1 и не более {max_candies} конфет. Твой ход: ")
        else:
            n -= int(take)
    if n > max_candies:
        print(f"В сундуке осталось {n} конфет.")
        flag = 0
if flag == 1:
    print(f"Конфеты всё =( {first} забирает все конфеты!")
if flag == 0:
    print(f"Конфеты всё =( {second} забирает все конфеты!")
