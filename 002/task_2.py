
#? Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5

n = int(input('Input a number: '))

for item in range(2, n+1):
    if n % item == 0:
        print(f'Smallest divisor of {n} is {item}')
        break

