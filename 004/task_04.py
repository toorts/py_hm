
#? Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#? многочлена и вывести многочлен степени k.

# Пример:
# k = 2 => 2*x² + 4*x + 5
# k = 6 => ix^6 + ax^5 + bx^4 + cx^3 + dx^2 + ex + h
# a, b, c, d, e, h - рандом

from random import randint


def polynom(lst):

    result = []
    for i in range(len(lst)):
        if i == 0:
            result.append(f'{lst[i]}')
        elif i == 1:
            result.append(f'{lst[i]}x')
        else:
            result.append(f'{lst[i]}x^{i}')

    return ' + '.join(result[::-1])


k = int(input('Input power: '))
factors = [randint(0, 100) for _ in range(k+1)]

print(polynom(factors))
