"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
"""
k = int(input("Введите число:"))
fib = [1,1]
nfib = [1,-1]
for i in range(2,k):
    fib.append(fib[i-1]+fib[i-2])
    nfib.append(nfib[i-2]-nfib[i-1])
nfib.reverse()
nfib.append(0)
print(nfib+fib)