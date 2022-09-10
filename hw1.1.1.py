"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""

print("Введите значения: ")
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
def logic_function (x,y,z):
    return (not (x or y or z)) == (not x and not y and not z)
print(f'{logic_function(x,y,z)}')

