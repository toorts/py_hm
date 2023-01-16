
# ? Создайте программу для игры с конфетами человек против бота.
# ? Условие задачи: На столе лежит 120 конфет. Играют два игрока делая ход друг после друга.
# ? Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# ? Победитель - тот, кто оставил на столе 0 конфет.

# 120 конф >>> user 21 --> 99 >>> бот 4 --> 95 .... 29 >>> бот 27 --> 2 >>> user 2 --> 0 конф >>> winner - user!

# * Подумайте как наделить бота "интеллектом" (Теория игр)


from random import randint


def start():
    
    print('There are 120 candies on the table. Two players (User vs Bot), the course of events from a friend after a friend.')
    print('The first one is made by the User. In one turn, you can pick up no more than 28 candies.')
    print('The winner is the one who left 0 candies on the table.')


def user_turn():

    global candy
    global max_candy

    print()
    print(f'{candy} candies left.')

    user_candy = int(input('How many will you take?: '))
    while (0 > user_candy) or (user_candy > max_candy) or (user_candy > candy):
        user_candy = int(input('Wrong amount of candy! Try again: '))

    candy -= user_candy

    if candy > 0:
        bot_turn()
    else:
        print('You Win!')


def bot_turn():

    global candy
    global max_candy

    print()
    print(f'{candy} candies left.')

    # bot_candy = randint(1, max_candy)     # regular bot
    bot_candy = candy % (max_candy + 1) if candy % (max_candy + 1) != 0 else randint(1, max_candy)    # smart bot
    print(f'Bot takes {bot_candy} candies.')

    candy -= bot_candy

    if candy > 0:
        user_turn()
    else:
        print('Bot Win!')


candy = 120
max_candy = 28

start()
user_turn()
