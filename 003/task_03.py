
#? Задайте список из вещественных чисел. Напишите программу, 
#? которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import random
from math import floor

num = int(input('Enter the number of elements: '))

lst = [round(random() * 100, 2) for _ in range(num)]
print(lst)

lst_out = [round(x - floor(x), 2) for x in lst]

result = max(lst_out) - min(lst_out)
print(f'Difference between max and min of fractions is {round(result, 2)}')
