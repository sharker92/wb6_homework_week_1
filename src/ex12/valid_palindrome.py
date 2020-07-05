import re


def is_palindrome(s: str) -> bool:
    regex = re.compile("[^0-9a-zA-Z]")
    word = re.sub(regex, "", s).lower()
    rev_word = word[::-1]
    print(word)
    if word == rev_word:
        return True
    return False
