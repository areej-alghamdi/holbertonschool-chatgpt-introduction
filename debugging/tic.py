#!/usr/bin/python3


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def get_valid_move(player):
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        if row not in (0, 1, 2) or col not in (0, 1, 2):
            print("Row and column must be 0, 1, or 2. Try again.")
            continue
        return row, col


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    winner_found = False

    while not winner_found and not is_board_full(board):
        print_board(board)
        row, col = get_valid_move(player)
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                winner_found = True
            else:
                player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    if winner_found:
        print("Player " + player + " wins!")
    else:
        print("It's a draw!")


tic_tac_toe()