# 2760. Longest Even Odd Subarray With Threshold
# You are given a 0-indexed integer array nums and an integer threshold.
# Find the length of the longest subarray of nums starting at index l and ending at index r (0 <= l <= r < nums.length) that satisfies the following conditions:
    # nums[l] % 2 == 0
    # For all indices i in the range [l, r - 1], nums[i] % 2 != nums[i + 1] % 2
    # For all indices i in the range [l, r], nums[i] <= threshold
# Return an integer denoting the length of the longest such subarray.
# Note: A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_len = length = 0
        for num in nums:
            if num > threshold:
                length = 0
                continue
            r = num % 2
            if r == length % 2:
                length += 1
            elif r == 0:
                length = 1
            else:
                length = 0
            max_len = max(length, max_len)
        return max_len

s = Solution()
print(s.longestAlternatingSubarray([3,2,5,4], 5))
print(s.longestAlternatingSubarray([1,2], 2))
print(s.longestAlternatingSubarray([2,3,4,5], 4))