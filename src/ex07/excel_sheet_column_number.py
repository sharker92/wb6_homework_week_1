
def title_to_number(s: str) -> int:
    result = 0
    for ch, ind in enumerate(reversed(range(len(s)))):
        result += (ord(s[ch]) - 64) * pow(26, ind)
    return result
