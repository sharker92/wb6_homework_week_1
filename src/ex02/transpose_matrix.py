from typing import List


def transpose(A: List[List[int]]) -> List[List[int]]:
    result = list()
    row = len(A)
    col = len(A[0])
    for c in range(col):
        temp = list()
        for r in range(row):
            temp.append(A[r][c])
        result.append(temp)
    return result
