#! /usr/bin/env python3

'''
    Project: Part 8 - Tic-Tac-Toe game
'''

import random

def check_for_possible_win(board, actor):
    ''' Check for possible winning moves, either to block an actor,
        or to capture the win for the actor.
    '''
    for row in range(3):
        count = 0
        for col in range(3):
            if board[row][col] == actor:
                count += 1
        if count == 2:
            for col in range(3):
                if board[row][col] == ' ':
                    return (row, col)

    for col in range(3):
        count = 0
        for row in range(3):
            if board[row][col] == actor:
                count += 1
        if count == 2:
            for row in range(3):
                if board[row][col] == ' ':
                    return (row, col)

    count = 0
    for diag in range(3):
        if board[diag][diag] == actor:
            count += 1
    if count == 2:
        for diag in range(3):
            if board[diag][diag] == ' ':
                return (diag, diag)

    count = 0
    for diag in range(3):
        if board[diag][2-diag] == actor:
            count += 1
    if count == 2:
        for diag in range(3):
            if board[diag][2-diag] == ' ':
                return (diag, 2-diag)

    return (None, None)


def get_computer_move(board):
    ''' Choose a square for the computer to put an X in. Return the
        square as a list with two elements: (row, column)
    '''

    # Win, if possible
    row, col = check_for_possible_win(board, 'X')
    if row is not None:
        return (row, col)

    # If no viable win, block, if possible
    row, col = check_for_possible_win(board, 'O')
    if row is not None:
        return (row, col)

    # If we can't win or block, generate a random move
    row = random.randint(0, 2)
    col = random.randint(0, 2)

    while board[row][col] != ' ':
        row = random.randint(0, 2)
        col = random.randint(0, 2)

    return (row, col)

def check_win(board):
    ''' Check if anyone has won.
    '''
    # check if any of the rows have three of the same symbol in a row
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            return True
    # check if any of the columns have three of the same symbol
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True
    # check the diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[2][0] == board[1][1] == board[0][2] != ' ':
        return True
    # if none of the three checks yielded a winner, return False
    return False

def print_board(board):
    for row in range(3):
        print(f"     {board[row][0]}|{board[row][1]}|{board[row][2]}")
        if row < 2:
            print("    ", "-" * 5)


board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
num_moves = 0

print("Let's play Tic-Tac-Toe! I will play 'X' and you can play 'O'")
print_board(board)

while True:
    # make the computer move
    print("I'm thinking...")
    square = get_computer_move(board)
    board[square[0]][square[1]] = 'X'
    num_moves += 1
    print_board(board)

    # Check for a win or draw
    if check_win(board):
        print("I win!")
        break
    if num_moves == 9:
        print("Draw; Good game.")
        break

    # get the player's move
    print("your turn:")
    try:
        row = int(input("Choose a row (0-2): "))
        col = int(input("Choose a column (0-2): "))
    except ValueError as e:
        print(f"Bad row or column: {e}")
        exit(1)

    if 0 <= row <= 2 and 0 <= col <= 2:
        if board[row][col] != ' ':
            print("That spot is already taken. You default!")
            exit()
        board[row][col] = "O"
        num_moves += 1
        print_board(board)

        if check_win(board):
            print("You Win!")
            exit()
    else:
        print("That's off the board!")
        exit()
