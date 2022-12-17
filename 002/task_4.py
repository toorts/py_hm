
#? Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

n = int(input('Input a number: '))

lst = list(range(1, n+1))
print(lst)

even_nums = [x for x in lst if x % 2 == 0]
print(f'Sum of even numbers is {sum(even_nums)}')

