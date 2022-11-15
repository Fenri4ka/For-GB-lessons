"""
Задайте последовательность чисел.
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
"""
import random
mylst = [random.randint(0,5) for _ in range(11)]
print(mylst)
nlst = [i for i in mylst if mylst.count(i) == 1]
print(nlst)
