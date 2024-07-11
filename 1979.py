# 1979. Find Greatest Common Divisor of Array
# Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        divisor = smallest
        while (largest % divisor != 0) or (smallest % divisor != 0):
            divisor -= 1
        return divisor

s = Solution()
print(s.findGCD([10, 11, 12, 13, 14, 15]))
print(s.findGCD([999, 500]))