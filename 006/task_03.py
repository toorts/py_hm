
#? Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11


num = input('Input number: ')
print(sum([int(x) for x in num if x.isnumeric()]))