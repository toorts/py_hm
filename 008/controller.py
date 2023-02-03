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

