
#? Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

num = int(input('Enter the number of elements: '))

lst = [randint(1, 9) for _ in range(num)]
print(lst)

prod_lst = []

for i in range(len(lst) // 2 + len(lst) % 2):
    prod_lst.append(lst[i] * lst[-(i + 1)])

print(prod_lst)
