from student_database import set_student, set_rating


def add_student():
    # получение данных ученика от учителя и их передача для записи
    metric = input('\nВведите данные (фамилия, имя, класс) через пробел: ').split(' ')
    set_student(metric)


def put_rating():
    # получение данных оценки от учителя и их передача для записи
    last_name = input('Введите фамилию ученика: ')
    lesson = input('Введите название урока: ')
    rating = input('Введите оценку/оценки через пробел: ')
    set_rating(last_name, lesson, rating)

