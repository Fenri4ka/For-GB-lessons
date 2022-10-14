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
print(f"Список из {n} элементов:", mylst)
f = open('file.txt','r+')
for i in range(len(mylst)):
    f.writelines(str(random.randint(0,len(mylst)-1))+'\n')
f.close()
with open('file.txt','r') as f:
    for line in f:
        indlst.append(line.replace('\n',''))
for j in indlst:
    mult *= mylst[int(j)]
print("Произведение чисел из списка на позициях из файла:",mult)
for k in range(len(mylst)):
    el = mylst.pop(random.randint(0,len(mylst)-1))
    mylst.append(el)
print("Перемешанный список:",mylst)
