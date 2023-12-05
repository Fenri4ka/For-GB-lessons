# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

my_path = "C:/Vanya/Desktop/GreekBrains/УЧУ_ПИТОН/Python_advanced/Seminar5/seminar.py"


def get_tuple(file_path: str) -> tuple:
    path, filename = os.path.split(file_path)
    name, extension = filename.split('.')
    return path, name, extension


print(f'Путь к файлу: {my_path} \nКортеж из пути: {get_tuple(my_path)}')


# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ['Alina', 'Zena', 'Vasya']
salaries = [45000, 50000, 75000]
bonuses = ['10.25%', '15.75%', '9.05%']

print({name: salary * float(bonus[:-1]) / 100 for name, salary, bonus in zip(names, salaries, bonuses)})

# Создайте функцию генератор чисел Фибоначчи

n = int(input('Введите количество чисел Фибоначчи: '))


def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


for fib in fibonacci(n):
    print(fib, end=' ')
