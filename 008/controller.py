# from models import *


# def menu_action():

#     print("\nДействия со справочником: \n"
#           "1 - Просмотр контактов \n"
#           "2 - Добавить контакт \n"
#           "3 - Удалить все контакты \n")

#     num_menu = input(f'Введите номер необходимого действия ==> ')

#     if num_menu == '1':
#         menu_view()
#         menu_action()
#     elif num_menu == '2':
#         menu_add()
#         menu_action()
#     elif num_menu == '3':
#         delete_data()
#         menu_action()


# def menu_view():
#     print('\nТелефонная книга:\n')
#     lst_tel = view_entry()
#     if lst_tel == 1:
#         print('В телефонной книге нет записей!')
#     else:
#         for el in lst_tel:
#             print(*el)


# def menu_add():
#     add_str = (input(f'\nВведите имя => ') + ' ' +
#                input(f'Введите фамилию => ') + ' ' +
#                input(f'Введите номер => ') + ' ' +
#                input(f'Введите примечание => ') + '\n')
#     add_str = add_str.split()

#     add_entry(add_str)
#     add_entry2(add_str)


from student_database import save_db, load_db, get_student
from teacher import add_student, put_rating


def menu_action():

    load_db()

    num_menu = input('\nКто вы?\n 1 - учитель\n 2 - ученик\nВвод: ')

    if num_menu == '1':
        flag = 1
        while flag == 1:
            act = input('\nВаши действия? \n'
                        '1 - записать ученика\n'
                        '2 - выставить оценку\n'
                        '0 - выход\n'
                        'Ввод: ')

            if act == '1':
                add_student()
            elif act == '2':
                put_rating()
            elif act == '0':
                flag = 0
            else:
                save_db()    # сохранение в db_student.json

    elif num_menu == '2':
        flag = 1
        while flag == 1:
            last_name = input('\nВведите фамилию или 0 для выхода\nВвод: ')
            if last_name == '0':
                flag = 0
            else:
                get_student(last_name)

