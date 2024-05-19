# 747. Largest Number At Least Twice of Others
# You are given an integer array nums where the largest integer is unique.
# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = [0, nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > largest[1]:
                largest[0] = i
                largest[1] = nums[i]
        for i in range(len(nums)):
            if i != largest[0] and (nums[i] * 2) > largest[1]:
                return -1
        return largest[0]

s = Solution()
print(s.dominantIndex([3,6,1,0]))
print(s.dominantIndex([1,2,3,4]))