# 2148. Count Elements With Strictly Smaller and Greater Elements 
# Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.

from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        sml = min(nums)
        big = max(nums)
        count = 0
        for num in nums:
            if num > sml and num < big:
                count += 1
        return count

s = Solution()
print(s.countElements([11,7,2,15]))