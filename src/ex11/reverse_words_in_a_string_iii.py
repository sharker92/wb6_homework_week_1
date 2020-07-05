
def reverse_words(s: str) -> str:
    result = s.split()
    result = [w[::-1] for w in result]
    result = " ".join(result)
    return result
