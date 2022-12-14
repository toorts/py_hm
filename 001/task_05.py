
#? Напишите программу, которая принимает на вход координаты двух точек
#? и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float(input('Enter X1 coordinate: '))
y1 = float(input('Enter Y1 coordinate: '))
x2 = float(input('Enter X2 coordinate: '))
y2 = float(input('Enter Y2 coordinate: '))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f'Distance is {distance:.2f}')