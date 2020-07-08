from typing import List


def surr_region(board: List[List[str]]) -> None:
    for i, board_row in enumerate(board):
        if i == 0 or i + 1 == len(board):
            continue
        for j, board_col in enumerate(board_row):
            if j == 0 or j + 1 == len(board[0]):
                continue
            if board_col == "O":
                print("___________")
                X = flip_board(board, i, j)
                print("_X_X_X_X_XXX____")


def flip_board(board: List[List[int]], i: int, j: int) -> None:
    jump = 0
    print(board)
    print("i:", i, "j:", j)
    print(board[i][j])

    #x = input("")

    if j + 1 < len(board[0]) and (board[i][j+1] == "X" or len(board[i][j+1]) >= 2):
        print("one")
        board[i][j] += "X"
    elif j + 1 < len(board[0]) and jump == 0:
        print("?")
        flip_board(board, i, j+1)
    else:
        return 0

    if i + 1 < len(board) and (board[i+1][j] == "X" or len(board[i+1][j]) >= 3):
        print("two")
        board[i][j] += "X"
    elif i + 1 < len(board) and jump == 0:
        print("???")
        flip_board(board, i+1, j)
    else:
        return 0

    if i - 1 >= 0 and (board[i-1][j] == "X" or len(board[i-1][j]) >= 4):
        print("three")
        board[i][j] += "X"
    elif i - 1 >= 0 and jump == 0:
        flip_board(board, i-1, j)
    else:
        return 0

    if j - 1 >= 0 and (board[i][j-1] == "X" or len(board[i][j-1]) >= 5):
        print("four")
        board[i][j] += "X"
    elif j - 1 >= 0 and jump == 0:
        flip_board(board, i, j-1)
    else:
        return 0

    board[i][j] = "X"

    return 0
