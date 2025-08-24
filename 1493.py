# 1493. Longest Subarray of 1's After Deleting One Element
# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        prev = 0
        total_zeros = 0
        i = 0
        nums.append(0)
        while i < len(nums):
            ones = zeros = 0
            while i < len(nums) and nums[i] == 1:
                ones += 1
                i += 1
            max_len = max(max_len, ones + prev)
            while i < len(nums) and nums[i] == 0:
                zeros += 1
                i += 1
            total_zeros += zeros
            prev = 0 if zeros > 1 else ones
        nums.pop()
        return max_len if total_zeros > 1 else max_len - 1

s = Solution()
print(s.longestSubarray([1, 1, 1, 0, 0, 1, 1]))
print(s.longestSubarray([1, 1, 1, 0, 1, 1]))