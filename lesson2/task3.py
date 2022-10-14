"""
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
"""

n = int(input('Введите число:'))
mylst = []
summa = 0
for i in range(1, n+1):
    summa = (1+1/i)**i
    mylst.append(summa)
print('Сумма чисел последовательности:',round(sum(mylst),3))
