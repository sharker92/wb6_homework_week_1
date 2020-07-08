
def is_power_of_two(n: int) -> bool:
    return n > 0 and not n & (n - 1)
