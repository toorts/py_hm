
#? Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21, 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Input a number: '))

fibonacci = []
for i in range(0, n):
    if i == 0 or i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append((fibonacci[i - 1]) + (fibonacci[i - 2]))

negafibonacci = []
for i in range(0, n + 1):
    if i == 0:
        negafibonacci.append(0)
    elif i == 1:
        negafibonacci.append(1)
    elif i == 2:
        negafibonacci.append(-1)
    else:
        negafibonacci.append(negafibonacci[i - 2] - negafibonacci[i - 1])

negafibonacci.reverse()
negafibonacci.extend(fibonacci)

print(negafibonacci)
