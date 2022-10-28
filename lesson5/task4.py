"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
"""
import random
with open("file.txt", "w") as f:
    f.write(random.randint(1, 20)*"F")
    f.write(random.randint(1, 20)*"Z")
    f.write(random.randint(1, 20)*"N")
with open("file.txt", "r") as f:
    s = f.readline()
print(s)
with open("file2.txt", "w") as f:
    for i in range(len(s)):
        if s[i] != s[i-1]:
            f.write(str(s.count(s[i])))
            f.write(s[i])
with open("file2.txt", "r") as f:
    s2 = f.readline()
print(s2)