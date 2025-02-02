# 1752. Check if Array Is Sorted and Rotated
# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
# There may be duplicates in the original array.
# Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        start_idx = -1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if start_idx != -1:
                    return False
                start_idx = i
        if start_idx == -1:
            return True
        if nums[-1] > nums[0]:
            return False
        return True
    
s = Solution()
print(s.check([3,4,5,1,2]))
print(s.check([1,2,3,4,5,1]))
print(s.check([7,9,1,1,1,3]))
print(s.check([7,7,7]))
print(s.check([2,1]))
print(s.check([1,3,2]))