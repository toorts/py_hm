
# ? Напишите программу, которая принимает на вход число N
# ? и выдает набор произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда [1, 2, 6, 24] -> (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(n):
    list = []
    count = 1
    for num in range(1, n+1):
        count *= num
        list.append(count)
    return list

number = int(input('Input a number: '))
result = factorial(number)

print(result)
