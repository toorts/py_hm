
#? Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# N = 6 | 12        | 32                | 13 | 9     | 18        | 21
# 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3 * 7

def find_factor(n):
    
    factor_lst = []
    d = 2

    while d * d <= n:
        if n % d == 0:
            factor_lst.append(d)
            n //= d
        else:
            d += 1

    if n > 1:
        factor_lst.append(n)

    return factor_lst

num = int(input('Input a number: '))
print(find_factor(num))