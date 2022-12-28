
#? Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#? многочлена и вывести многочлен степени k.

# Пример:
# k = 2 => 2*x² + 4*x + 5 

# k = 6 => ix^6 + ax^5 + bx^4 + cx^3 + dx^2 + ex + h
# a, b, c, d, e, h - рандом

from random import randint

k = int(input('Input power: '))

lst = [randint(0, 100) for _ in range(k+1)]

result = []
for i in range(len(lst)):
    result.append(f'{lst[i]}x^{i}')

result = ' + '.join(result[::-1])

print(result)
