
def is_power_of_two(n: int) -> bool:
    result = True
    binary = [d for d in str(bin(n))]
    if binary[2] != "1":
        return False
    for i in range(3, len(binary)):
        if binary[i] != "0":
            result = False
            break
    return result
