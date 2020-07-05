from typing import List


def transpose(A: List[List[int]]) -> List[List[int]]:
    row = len(A)
    col = len(A[0])
    print(row, col)
    result = list()
    for c in range(col):
        temp = list()
        for r in range(row):
            temp.append(A[r][c])
        result.append(temp)
    return result
