# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def check_triangle(side_a, side_b, side_c):
    if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
        return True
    else:
        return False


side_a, side_b, side_c = float(input("Сторона А = ")), float(input("Сторона B = ")), float(input("Сторона C = "))

if not check_triangle(side_a, side_b, side_c):
    print('Такого треугольника не существует')
else:
    if side_a == side_b == side_c:
        print('Треугольник равносторонний')
    elif side_a == side_b and side_b != side_c or side_a == side_c and side_a != side_b or side_b == side_c and side_b != side_a:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')


# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def check_number(num: int):
    if num < 0 or num > 100000:
        return False
    else:
        return True


num = int(input("Введите число. Оно должно быть больше нуля, но меньше 100 тыс "))

if not check_number(num):
    print('Введенное число не соответсвует условию')
else:
    if num > 1:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                print(num, 'не простое число')
                break
        else:
            print(num, 'простое число')
    else:
        print(num, 'не простое число')

# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
COUNTER_LIMIT = 10

number = randint(LOWER_LIMIT, UPPER_LIMIT)

counter = 1
while counter <= COUNTER_LIMIT:
    print(f'Попытка №{counter}. Попробуйте угадать число, которое загадал великий Рандом!')
    input_number = int(input('Число '))
    if input_number == number:
        print('Надо же, угадал!')
        break
    elif number > input_number:
        print('Близко! Но меньше, чем нужно.')
    else:
        print('Почти! Но больше, чем нужно.')
    counter += 1
else:
    print(f'Попытки всё. Великий Рандом загадывал число {number}')
