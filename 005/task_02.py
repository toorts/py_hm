
#? Создайте программу для игры в ""Крестики-нолики"" человек vs человек.


board = list(range(1, 10))

def print_board():
    row1 = f'| {board[0]} | {board[1]} | {board[2]} |'
    row2 = f'| {board[3]} | {board[4]} | {board[5]} |'
    row3 = f'| {board[6]} | {board[7]} | {board[8]} |'

    print()
    print('-------------')
    print(row1)
    print('-------------')
    print(row2)
    print('-------------')
    print(row3)
    print('-------------')
    print()


def player_move(icon):
    print(f'Your turn player {icon}')
    while True:
        choice = input("Enter your move (1-9): ")
        if not (choice in '123456789'):
            print('Error input. Try again.')
            continue
        choice = int(choice)
        if str(board[choice - 1]) in 'XO':
            print("That space is taken!")
            continue
        board[choice - 1] = icon
        break


def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False


def is_draw():
    for i in range(1, 10):
        if i in board:
            return False
    return not is_victory("X") and not is_victory("O")


def main():
    while True:
        print_board()
        player_move("X")
        print_board()
        if is_victory("X"):
            print("X wins! Congratulations!")
            break
        elif is_victory("O"):
            print("O wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break
        player_move("O")
        print_board()
        if is_victory("X"):
            print("X wins! Congratulations!")
            break
        elif is_victory("O"):
            print("O wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break


main()
