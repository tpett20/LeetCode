# 2501. Longest Square Streak in an Array
# You are given an integer array nums. A subsequence of nums is called a square streak if:
    # The length of the subsequence is at least 2, and
    # after sorting the subsequence, each element (except the first element) is the square of the previous number.
# Return the length of the longest square streak in nums, or return -1 if there is no square streak.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        n = sorted(nums)
        ref = set(n)
        max_streak = 0
        for num in n:
            curr = num
            streak = 0
            while curr in ref:
                streak += 1
                ref.remove(curr)
                curr **= 2
            max_streak = max(max_streak, streak)
        return max_streak if max_streak > 1 else -1

s = Solution()
print(s.longestSquareStreak([4,3,6,16,8,2]))