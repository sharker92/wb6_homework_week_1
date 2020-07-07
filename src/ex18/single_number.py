from typing import List


def single_number(nums: List[int]) -> int:
    result = 0
    if len(nums) == 1:
        return nums[0]
    ordered_list = nums
    ordered_list.sort()
    lenght = range(0, len(ordered_list), 2)
    for i in lenght:
        if lenght[-1] == i:
            result = ordered_list[i]
            break
        else:
            j = i + 1
        if ordered_list[i] != ordered_list[j]:
            result = ordered_list[i]
            break
    return result
