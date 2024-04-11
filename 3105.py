# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        inc_rule = True if nums[1] > nums[0] else False
        curr_len = max_len = 1
        for i in range(1, len(nums)):
            inc = True if nums[i] > nums[i - 1] else False
            if nums[i] == nums[i - 1]:
                curr_len = 1
            elif inc == inc_rule:
                curr_len += 1
            else:
                curr_len = 2
            inc_rule = inc
            max_len = max(curr_len, max_len)
        return max_len

s = Solution()
print(s.longestMonotonicSubarray([1,4,3,3,2]))
print(s.longestMonotonicSubarray([3,3,3,3]))
print(s.longestMonotonicSubarray([3,2,1]))