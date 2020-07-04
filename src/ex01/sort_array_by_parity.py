from typing import List


def sort_array_by_parity(A: List[int]) -> List[int]:
    result = list()
    odd = list()
    for num in A:
        if num % 2 == 0:
            result.append(num)
        else:
            odd.append(num)
    result.extend(odd)
    return result
