# 2016. Maximum Difference Between Increasing Elements
# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
# Return the maximum difference. If no such i and j exists, return -1.

from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        max_right = nums[-1]
        max_diff = -1
        for i in range(n - 2, -1, -1):
            max_diff = max(max_diff, max_right - nums[i])
            max_right = max(max_right, nums[i])
        return -1 if max_diff == 0 else max_diff

s = Solution()
print(s.maximumDifference([7,1,5,4]))
print(s.maximumDifference([1,1]))