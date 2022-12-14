
#? 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
#?    причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#?    в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Input X: '))
y = int(input('Input Y: '))

if x == 0 and y == 0: print("It's the center of coordinates")
elif x == 0: print('The point is on the Y-axis')
elif y == 0: print('The point is on the X-axis')
elif x > 0 and y > 0: print('Quart is 1')
elif x < 0 and y > 0: print('Quart is 2')
elif x < 0 and y < 0: print('Quart is 3')
else: print('Quart is 4')