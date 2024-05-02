# 2441. Largest Positive Integer That Exists With Its Negative
# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
# Return the positive integer k. If there is no such integer, return -1.

from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        pos_nums = set()
        neg_nums = set()
        for num in nums:
            if num > 0:
                pos_nums.add(num)
            else:
                neg_nums.add(num)
        short_set = pos_nums if len(pos_nums) < len(neg_nums) else neg_nums
        long_set = neg_nums if len(pos_nums) < len(neg_nums) else pos_nums
        largest = -1
        for num in short_set:
            if (num * -1) in long_set and abs(num) > largest:
                largest = abs(num)
        return largest

s = Solution()
print(s.findMaxK([-1,2,-3,3]))
print(s.findMaxK([-1,10,6,7,-7,1]))
print(s.findMaxK([-10,8,6,7,-2,-3]))