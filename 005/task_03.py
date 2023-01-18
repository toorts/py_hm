
#? Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#? Входные данные хранятся в отдельных текстовых файлах.

# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"


import re

def compress(string):
    compressed = ""
    count = 1
    for i in range(len(string)):
        if i+1 < len(string) and string[i] == string[i+1]:
            count += 1
        else:
            compressed += str(count) + string[i]
            count = 1
    return compressed

def decompress(string):
    decompressed = ""
    pattern = re.compile(r"(\d+)(\D)")
    matches = pattern.finditer(string)
    for match in matches:
        count = int(match.group(1))
        char = match.group(2)
        decompressed += char * count
    return decompressed

# Reading the input string from a file
with open("005\input.txt", "r") as file:
    string = file.read()

compressed = compress(string)

# Writing the compressed string to a file
with open("005\compressed.txt", "w") as file:
    file.write(compressed)

# Reading the compressed string from a file
with open("005\compressed.txt", "r") as file:
    compressed = file.read()

decompressed = decompress(compressed)

# Writing the decompressed string to a file
with open("005\decompressed.txt", "w") as file:
    file.write(decompressed)
