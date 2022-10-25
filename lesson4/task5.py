"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
"""
from task4 import create_f
create_f(int(input("Введите желаемую степень: ")),"file2.txt")

with open ("file1.txt", "r") as f1:
    s1 = f1.read()
with open ("file2.txt", "r") as f2:
    s2 = f2.read()
print("Первое уровнение: ",s1)
print("Второе уравнение: ",s2)
def get_pol(s):
    s = s.replace("=0", "")
    s = s.split("+")
    s = [i for i in s]
    for i in range(len(s)):
        if s[i] == 'x':
            s[i] == '1'
    s = s[::-1]
    return s
lst1 = get_pol(s1)
lst2 = get_pol(s2)
for i in range(len(lst1)):
        lst1[i] = lst1[i].split("*")
for j in range(len(lst2)):
        lst2[j] = lst2[j].split("*")
lst1 = lst1[::-1]
lst2 = lst2[::-1]
with open("file3.txt", "w") as f:
    if len(lst1) == len(lst2):
        for i in range(len(lst1)):
            if len(lst1[i])==2:
                f.write(str(int(lst1[i][0]) + int(lst2[i][0]))+"*"+str(lst1[i][1]))
                f.write("+")
            else:
                f.write(str(int(lst1[i][0]) + int(lst2[i][0])))
                f.write("=0")
    if len(lst1) > len(lst2):
        k = len(lst1)-len(lst2)
        for j in range(k):
            f.write(str(lst1[j][0] + "*" + str(lst1[j][1])))
            f.write("+")
        for i in range(k,len(lst1)):
            if len(lst1[i])==2:
                f.write(str(int(lst1[i][0]) + int(lst2[i-k][0]))+"*"+str(lst1[i][1]))
                f.write("+")
            else:
                f.write(str(int(lst1[i][0]) + int(lst2[i-k][0])))
                f.write("=0")
    if len(lst1) < len(lst2):
        k = len(lst2)-len(lst1)
        for j in range(k):
            f.write(str(lst2[j][0] + "*" + str(lst2[j][1])))
            f.write("+")
        for i in range(k,len(lst2)):
            if len(lst2[i])==2:
                f.write(str(int(lst1[i-k][0]) + int(lst2[i][0]))+"*"+str(lst1[i-k][1]))
                f.write("+")
            else:
                f.write(str(int(lst1[i-k][0]) + int(lst2[i][0])))
                f.write("=0")
with open("file3.txt", "r") as f3:
    s3 = f3.read()
print("Результат их сложения: ",s3)