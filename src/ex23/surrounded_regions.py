from typing import List


def surr_region(board: List[List[str]]) -> None:
    if not board:
        return
    last_row = len(board) - 1
    last_col = len(board[0]) - 1
    print(last_row, last_col)
    for j in range(last_col + 1):
        if board[0][j] == "O":
            board[0][j] = "N"
            no_flip(board, 0, j)

        if board[last_row][j] == "O":
            board[last_row][j] = "N"
            no_flip(board, last_row, j)

    for i in range(last_row + 1):
        if board[i][0] == "O":
            board[i][0] = "N"
            no_flip(board, i, 0)

        if board[i][last_col] == "O":
            board[i][last_col] = "N"
            no_flip(board, i, last_col)

    for i in range(len(board)):
        for j in range(len(board[0])):

            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "N":
                board[i][j] = "O"

        # for i, board_row in enumerate(board):
        #     for j, board_col in enumerate(board_row):
        #         if j == 0 or j + 1 == len(board[0]) or i == 0 or i + 1 == len(board):
        #             if board_col == "O":
        #                 board[i][j] = "N"
        #             continue
        #         if board_col == "O":
        #             flip_board(board, i, j, 1)

        # for i in range(len(board)):
        #     for j in range(len(board[0])):

        #         if len(board[i][j]) > 1 or board[i][j] == "N":
        #             board[i][j] = "O"

        # for b in board:


def no_flip(board: List[List[int]], i: int, j: int):

    if j + 1 < len(board[0]) and board[i][j+1] == "O":
        board[i][j+1] = "N"

        no_flip(board, i, j+1)
    if i + 1 < len(board) and board[i+1][j] == "O":
        board[i+1][j] = "N"

        no_flip(board, i+1, j)
    if i - 1 >= 0 and board[i-1][j] == "O":
        board[i-1][j] = "N"

        no_flip(board, i-1, j)
    if j - 1 >= 0 and board[i][j-1] == "O":
        board[i][j-1] = "N"

        no_flip(board, i, j-1)


def flip_board(board: List[List[int]], i: int, j: int, found: int) -> int:
    while True:

        # x = input("")
        if board[i][j] == "X":
            return 1
        elif board[i][j] == "N":
            break
        if found == 1 and i - 1 >= 0 and i + 1 < len(board) and j - 1 >= 0 and j + 1 < len(board[0]):

            if board[i][j-1] == "X" or len(board[i][j-1]) >= 2:

                board[i][j] += "X"

                if board[i-1][j] == "X" or len(board[i-1][j]) >= 3:

                    board[i][j] += "X"
                    if board[i][j+1] == "X" or len(board[i][j+1]) >= 4:

                        board[i][j] += "X"

                        if board[i+1][j] == "X" or len(board[i+1][j]) >= 5:

                            board[i][j] = "X"
                            return 1

                        elif board[i+1][j] == "N":
                            board[i][j] = "N"

                            break
                        else:

                            found = flip_board(board, i+1, j, found)
                    elif board[i][j+1] == "N":
                        board[i][j] = "N"

                        break
                    else:

                        found = flip_board(board, i, j+1, found)
                elif board[i-1][j] == "N":
                    board[i][j] = "N"

                    break
                else:

                    found = flip_board(board, i-1, j, found)
            elif board[i][j-1] == "N":
                board[i][j] = "N"

                break
            else:

                found = flip_board(board, i, j-1, found)

            # board[i][j] = "X"
        else:
            board[i][j] = "N"
            break

    return 0
