# import numpy

# user_move = input("Please enter your move as x,y coordinates. i.e. 1,2: ")
# print(f"You entered: {user_move}")

import numpy as np
board = np.full((3, 3), ' ')

def print_board():
    for row in board:
        print(' | '.join(row))
        print('———' * 3)

def player_move(player):
    while True:
        move = input(f"Player {player}, please move: ")
        row, col = map(int, move.split(','))
        if board[row-1][col-1] == ' ':
            board[row-1][col-1] = player
            break
        else:
            print("Invalid move.")

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

def is_full():
    return np.all(board != ' ')

def play_game():
    players = ['X', 'O']
    current_player = 0
    while True:
        print_board()
        player_move(players[current_player])
        if check_winner():
            print_board()
            print(f"Player {players[current_player]} wins!")
            break
        if is_full():
            print_board()
            print("It's a tie!")
            break
        current_player = 1 - current_player

play_game()
