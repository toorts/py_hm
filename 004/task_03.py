
# ? Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Ввод:
# 3 1 2 3
# Вывод:
# 1 2

def find_uniques(lst):

    sign = []
    result = []

    for el in lst:
        if el not in sign:
            sign.append(el)
            result.append(el)
        else:
            if el in result:
                i = result.index(el)
                del result[i]

    return result


nums = input('Введите числа через пробел: ').split()
nums = [int(i) for i in nums]

print(*find_uniques(nums))
