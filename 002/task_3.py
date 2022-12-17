
#? Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
#? Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

from random import randint
from math import prod

n = int(input("Enter the number: "))

orig_list = [x for x in range(-n, n+1)]
print(orig_list)

index_list = [randint(0, len(orig_list) - 1) for _ in range(5)]
print(f'Index list -> {index_list}')

element_list = [orig_list[index_list[i]] for i in range(5)]
print(f'Element list -> {element_list}')

print(f'Product of elements is {prod(element_list)}')
