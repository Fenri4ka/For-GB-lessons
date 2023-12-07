# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

from random import randint

__all__ = ['set_queens', 'is_safe', 'get_success_cases']

QUEENS = 8
x, y = [0] * QUEENS, [0] * QUEENS
CASES = 4


def set_queens(n=QUEENS):
    for i in range(n):
        x[i], y[i] = randint(1, QUEENS), randint(1, QUEENS)
    return x, y


def is_safe(n=QUEENS):
    set_queens(n)
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
            else:
                return True


def get_success_cases(cases=CASES):
    success_cases = []
    while cases > 0:
        if is_safe():
            success_cases.append([*zip(x, y)])
            cases -= 1
    return success_cases


if __name__ == '__main__':
    for i, cases_list in enumerate(get_success_cases(), start=1):
        print(f'Успешный вариант расстановки №{i}: {cases_list}')
