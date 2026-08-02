# 2587. Rearrange Array to Maximize Prefix Score
# You are given a 0-indexed integer array nums. You can rearrange the elements of nums to any order (including the given order).
# Let prefix be the array containing the prefix sums of nums after rearranging it. In other words, prefix[i] is the sum of the elements from 0 to i in nums after rearranging it. The score of nums is the number of positive integers in the array prefix.
# Return the maximum score you can achieve.

from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        s_nums = sorted(nums, reverse=True)
        prefix_sum = s_nums[0]
        i = 1
        while i < len(s_nums) and prefix_sum > 0:
            prefix_sum += s_nums[i]
            i += 1
        return i if prefix_sum > 0 else i - 1

s = Solution()
print(s.maxScore([50]))
print(s.maxScore([1, 9, -8, -6]))