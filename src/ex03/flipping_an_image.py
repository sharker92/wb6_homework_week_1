from typing import List


def flip_and_invert_image(A: List[List[int]]) -> List[List[int]]:
    return [[1 if num == 0 else 0 for num in row[::-1]] for row in A]
