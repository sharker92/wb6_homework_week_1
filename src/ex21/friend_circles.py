from typing import List


def find_circle_num(M: List[List[int]]) -> int:
    result = list()
    num_students = len(M)
    for x, students in enumerate(M):
        if students.count(1) == 1:
            result.append(x)
    for i, students in enumerate(M):
        if i in result:
            continue
        union = list()
        for j, friend in enumerate(students):
            if i == j:
                continue
            else:
                if friend == 1:
                    M[i][j] = 0
                    M[j][i] = 0
                    union.append(i)
                    union.extend(is_friend(M, j))
        if union:
            result.append(union)
    return len(result)


def is_friend(M: List[List[int]], i: int) -> List[int]:
    circle = list()
    circle.append(i)
    for j, friend in enumerate(M[i]):
        if i == j:
            continue
        else:
            if friend == 1:
                M[i][j] = 0
                M[j][i] = 0
                circle.extend(is_friend(M, j))
    return circle
