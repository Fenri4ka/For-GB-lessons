"""
Задайте последовательность чисел.
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
"""
import random
mylst = [random.randint(0,5) for _ in range(11)]
print(mylst)
nlst = []
for i in mylst:
  if mylst.count(i)==1:
    nlst.append(i)
print(nlst)
