
def find_complement(num: int) -> int:
    bits = len(bin(num)) - 2
    one_complement = ~num
    result = one_complement & (2**bits - 1)
    return result
