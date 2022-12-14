
#? Напишите программу, которая принимает на вход цифру,
#? обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Enter the day of the week: '))

if 0 < day < 8:

    if day < 6:
        print("No. It's a work day")
    else:
        print("Yes! It's weekend day")

else:
    print("It's not a day of the week")