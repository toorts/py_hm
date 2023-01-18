
#? Дан список, вывести отдельно буквы и цифры.
# [12,'sadf', 5643] ---> ['sadf'], [12, 5643]


lst = [12,'sadf', 5643]
letters = list(filter(lambda x: isinstance(x, str), lst))
numbers = list(filter(lambda x: not isinstance(x, str), lst))
print(letters, numbers)
