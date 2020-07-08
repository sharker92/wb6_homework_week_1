from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    result = ""
    if strs:
        for i in range(min(map(len, strs))):
            temp = strs[0][i]
            for j in range(1, len(strs)):
                if temp == strs[j][i]:
                    continue
                else:
                    temp = ""
                    break
            if temp == "":
                break
            result += temp
    return result
