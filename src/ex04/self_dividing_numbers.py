from typing import List


def self_dividing_numbers(left: int, right: int) -> List[int]:
    result = [*range(left, right + 1)]
    for num in range(left, right + 1):
        if num < 10:
            continue
        else:
            for digit in [int(d) for d in str(num)]:
                if digit == 0 or num % digit != 0:
                    result.remove(num)
                    break
    return result
