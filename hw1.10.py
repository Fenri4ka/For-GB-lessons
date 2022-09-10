"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""

print("Введите координаты точки А: ")
x_a = float(input("x = "))
y_a = float(input("y = "))
print("Введите координаты точки B: ")
x_b = float(input("x = "))
y_b = float(input("y = "))

from math import sqrt
from math import *
num1 = round(sqrt((x_a - x_b)**2 + (y_a - y_b)**2)) 

print("Расстояние между точками : ", num1)
