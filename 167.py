# 167. Two Sum II - Input Array Is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            num1 = numbers[i]
            num2 = target - num1
            flr, ceil = i + 1, len(numbers) - 1
            while flr <= ceil:
                mid_idx = (ceil + flr) // 2
                mid_num = numbers[mid_idx]
                if mid_num < num2:
                    flr = mid_idx + 1
                elif mid_num > num2:
                    ceil = mid_idx - 1
                else:
                    return [i + 1, mid_idx + 1]

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([2,3,4], 6))
print(s.twoSum([-1,0], -1))