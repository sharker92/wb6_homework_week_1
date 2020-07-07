from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    result = list()
    for i, n in enumerate(nums):
        temp_index = i
        finding = target - n
        exists = nums.count(finding)
        if exists == 0:
            continue
        else:
            temp_index2 = nums.index(finding)
            if temp_index2 == temp_index:
                continue
            else:
                result.append(temp_index)
                result.append(temp_index2)
                break
    return result
