"""
Given an array of integers, return indices of the two numbers such
that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    result = []
    for index_x, x in enumerate(nums):
        for index_y, y in enumerate(nums):
            if x + y == target and index_x != index_y:
                result.append(index_x)
                result.append(index_y)
                return result

    return result


if __name__ == "__main__":
    print(two_sum([3, 2, 4], 6))
