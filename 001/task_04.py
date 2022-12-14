
#? Напишите программу, которая по заданному номеру четверти,
#? показывает диапазон возможных координат точек в этой четверти (x и y).

quart = int(input('Input a number of quart: '))

if 0 < quart < 5:
    if quart == 1: print('x > 0 and y > 0')
    elif quart == 2: print('x < 0 and y > 0')
    elif quart == 3: print('x < 0 and y < 0')
    else: print('x > 0 and y < 0')
else:
    print('Wrong number!')