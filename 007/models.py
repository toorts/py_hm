from os.path import exists, join
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def view_entry(file_path: str = 'phone_book.txt'):

    if exists(join(BASE_DIR, file_path)):
        with open(join(BASE_DIR, file_path), 'r', encoding='utf-8') as f:
            book_data = f.readlines()

        for i in range(len(book_data)):
            book_data[i] = book_data[i].strip('\n')
            book_data[i] = book_data[i].split(' ; ')

        return book_data

    return 1


def add_entry(import_line):
    str_imp_line = ''

    for i in range(len(import_line)):
        str_imp_line += ' '.join(import_line[i].split(", ")) + '\n'

    with open("007/phone_book.txt", 'a', encoding="utf-8") as f:
        f.write(str_imp_line)
        f.write('\n')


def add_entry2(import_line):
    str_imp_line = ''

    for i in range(len(import_line)):
        if import_line[i] == '\n':
            str_imp_line += (import_line[i])
        else:
            str_imp_line += (import_line[i]) + ' ; '

    with open("007/phone_book.csv", 'a', encoding="utf-8") as f:
        f.write(str_imp_line + '\n')


def delete_data():
    with open("007/phone_book.txt", 'wb'):
        pass

    with open("007/phone_book.csv", 'wb'):
        pass

    print('\nКонтакты удалены!')
