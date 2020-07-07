
def hamming_distance(x: int, y: int) -> int:
    return len([x for x in bin(x ^ y)[2::] if x == "1"])
