# 1863. Sum of All Subset XOR Totals
# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
    # For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums. 
# Note: Subsets with the same elements should be counted multiple times.
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_tot = 0

        def traverse(arr, total):
            nonlocal xor_tot
            total ^= arr[0]
            xor_tot += total
            for i in range(1, len(arr)):
                traverse(arr[i:], total)
        
        for i in range(len(nums)):
            traverse(nums[i:], 0)
        return xor_tot

s = Solution()
print(s.subsetXORSum([1,3]))
print(s.subsetXORSum([5,1,6]))
print(s.subsetXORSum([3,4,5,6,7,8]))