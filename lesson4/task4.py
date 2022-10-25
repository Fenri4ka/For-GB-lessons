"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
import random
def create_f(k,fl):
  with open (fl, 'w') as f:
    if k == 0:
       f.write(str(random.randint(1,101))+"*x+")
    else:
       for i in range(k):
          if k - i == 1:
              f.write(str(random.randint(1,101))+"*x+")
          else:
              f.write(str(random.randint(1,101))+"*x^"+str(k-i))
              f.write("+")
    f.write(str(random.randint(1,101)))
    f.write("=0")

k = int(input("Введите желаемую степень: "))
fl = 'file1.txt'
create_f(k,fl)
