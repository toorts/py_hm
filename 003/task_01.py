
#? Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

num = int(input('Enter the number of elements: '))

lst = [randint(0, 9) for _ in range(num)]
print(lst)

res = sum([x for x in lst[1::2]])
print(res)