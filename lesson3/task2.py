"""
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""
mylst = [int(i) for i in input("Введите числа через пробел:").split()]
nlst = []
if len(mylst)%2 == 0:
    l = len(mylst)//2
else:
    l = len(mylst)//2+1
for j in range(l):
    nlst.append(mylst[j]*mylst[len(mylst)-1-j])
print("Произведение пар чисел списка:",nlst)