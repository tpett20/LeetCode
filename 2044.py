# 2044. Count Number of Maximum Bitwise-OR Subsets
# Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.
# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

from typing import List

class Solution:
    def __init__(self):
        self.max_bitwise_or = 0
        self.count = 0

    def traverse(self, arr: List[int], bitwise_or: int) -> int:
        if bitwise_or > self.max_bitwise_or:
            self.max_bitwise_or = bitwise_or
            self.count = 1
        elif bitwise_or == self.max_bitwise_or:
            self.count += 1
        for i in range(len(arr)):
            self.traverse(arr[i + 1:], bitwise_or | arr[i])

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.traverse(nums, 0)
        return self.count

s = Solution()
print(s.countMaxOrSubsets([16] * 16))