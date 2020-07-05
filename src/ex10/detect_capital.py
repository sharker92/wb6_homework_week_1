
def detect_capital_use(word: str) -> bool:
    if word.istitle() or word.isupper() or word.islower():
        return True
    return False
