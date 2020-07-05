import re


def reverse_vowels(s: str) -> str:
    regex_nv = re.compile("[^aeiouAEIOU]")
    vowels = re.sub(regex_nv, "", s)
    reverse_vowels = vowels[::-1]
    result = list(s)
    last_v = 0
    for i in range(len(vowels)):
        last_v = s.find(vowels[i], last_v)
        result[last_v] = reverse_vowels[i]
        last_v += 1
    result = "".join(result)
    return result
