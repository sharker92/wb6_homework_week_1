from typing import List


def fizz_buzz(n: int) -> List[str]:
    result = list()
    ran = range(1, n + 1)
    for num in ran:
        print(num)
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(num))
    return result
