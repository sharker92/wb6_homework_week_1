import re


def binary_gap(N: int) -> int:
    result = 0
    start = 0
    eaten_string = bin(N)[2:]
    while True:
        eaten_string = eaten_string[start:]
        match = re.search("10*1", eaten_string)
        if match is None:
            break
        start = match.end() - 1
        lenght = len(match.group(0)) - 1
        if lenght > result:
            result = lenght
    return result
