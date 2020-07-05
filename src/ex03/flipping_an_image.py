from typing import List


def flip_and_invert_image(A: List[List[int]]) -> List[List[int]]:
    result = list()
    row = len(A)
    col = len(A[0])
    for r in range(row):
        temp = list()
        for c in reversed(range(col)):
            if A[r][c] == 1:
                temp.append(0)
            else:
                temp.append(1)
        result.append(temp)
    return result
