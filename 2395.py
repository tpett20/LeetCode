# 2395. Find Subarrays With Equal Sum
# Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.
# Return true if these subarrays exist, and false otherwise.
# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen_sums = set()
        for i in range(len(nums) - 1):
            curr_sum = nums[i] + nums[i + 1]
            if curr_sum in seen_sums:
                return True
            else:
                seen_sums.add(curr_sum)
        return False

s = Solution()
print(s.findSubarrays([4,2,4]))
print(s.findSubarrays([1,2,3]))