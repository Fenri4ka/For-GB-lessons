"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
Реализуйте алгоритм перемешивания списка.
"""
import random
n = int(input('Введите число:'))
mylst = [random.randint(-n,n) for _ in range(n)]
indlst = []
mult = 1
newlst = []
print(f"Список из {n} элементов:", mylst)
f = open('file.txt','r+')
for i in range(len(mylst)):
    f.writelines(str(random.randint(0,len(mylst)-1)))
f.close()
with open('file.txt','r') as f:
    for line in f:
        for num in line:
            indlst.append(num)
for j in indlst:
    mult *= mylst[int(j)]
print("Произведение чисел из списка на позициях из файла:",mult)
for k in range(len(mylst)):
    el = mylst.pop(random.randint(0,len(mylst)-1))
    newlst.append(el)
print("Перемешанный список:",newlst)
