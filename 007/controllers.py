from models import *
from checker import check_menu


def menu_action():

    print("\nДействия со справочником: \n"
          "1 - Просмотр контактов \n"
          "2 - Добавить контакт \n"
          "3 - Удалить все контакты \n")

    lst_num = ['1', '2', '3']
    num_menu = input(f'Введите номер необходимого действия ==> ')

    if check_menu(num_menu, lst_num) is True:

        if num_menu == '1':
            menu_view()
            menu_action()
        elif num_menu == '2':
            menu_add()
            menu_action()
        elif num_menu == '3':
            delete_data()
            menu_action

    else:
        print(f" \nВы ввели не корректное значение: {num_menu}  \n")
        menu_action()


def menu_view():
    print('\nТелефонная книга:\n')
    lst_tel = view_entry()
    if lst_tel == 1:
        print('В телефонной книге нет записей!')
    else:
        for el in lst_tel:
            print(*el)


def menu_add():
    add_str = (input(f'\nВведите имя => ') + ' ' +
               input(f'Введите фамилию => ') + ' ' +
               input(f'Введите номер => ') + ' ' +
               input(f'Введите примечание => ') + '\n')
    add_str = add_str.split()
    
    add_entry(add_str)
    add_entry2(add_str)
