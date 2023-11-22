# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
import fractions

HEX = 16
hex_digits = "0123456789abcdef"

num = int(input('Введите целое число '))
result: str = ''
print(f'Ваше число в шестнадцетиричной системе по функции hex = {hex(num)}')

while num > 0:
    frow_result = num % HEX
    hex_dig = hex_digits[frow_result]
    result = hex_dig + result
    num //= HEX

print(f'Ваше число в шестнадцетиричной системе по моим вычислениям = {result}')
print(type(result))


# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions


from fractions import Fraction
import math

fraction_1 = input('Введите первую дробь в виде a/b ')
fraction_2 = input('Введите вторую дробь в виде a/b ')


def cut_fraction(n: int, m: int):
    if n > m:
        k = n
    else:
        k = m
    while k != 1:
        if n % k == 0 and m % k == 0:
            return str(n // k) + "/" + str(m // k)
        else:
            k -= 1
    return str(n) + "/" + str(m)


def sum_fraction(fraction_1, fraction_2):
    num1 = fraction_1.split('/')
    num2 = fraction_2.split('/')
    lcm_fraction = math.lcm(int(num1[1]), int(num2[1]))
    num_fraction1 = int(lcm_fraction / int(num1[1]) * int(num1[0]))
    num_fraction2 = int(lcm_fraction / int(num2[1]) * int(num2[0]))
    return cut_fraction(num_fraction1 + num_fraction2, lcm_fraction)


def mult_fraction(fraction_1, fraction_2):
    num1 = fraction_1.split('/')
    num2 = fraction_2.split('/')
    return cut_fraction(int(num1[0]) * int(num2[0]), int(num1[1]) * int(num2[1]))


print('Расчет по функции Franction:')
print(f"{fraction_1} * {fraction_2} = {fractions.Fraction(int(fraction_1.split('/')[0]), int(fraction_1.split('/')[1])) * fractions.Fraction(int(fraction_2.split('/')[0]), int(fraction_2.split('/')[1]))}")
print(f"{fraction_1} + {fraction_2} = {fractions.Fraction(int(fraction_1.split('/')[0]), int(fraction_1.split('/')[1])) + fractions.Fraction(int(fraction_2.split('/')[0]), int(fraction_2.split('/')[1]))}")
print('Мой расчет:')
print(f'{fraction_1} * {fraction_2} = {mult_fraction(fraction_1, fraction_2)}')
print(f'{fraction_1} + {fraction_2} = {sum_fraction(fraction_1, fraction_2)}')
