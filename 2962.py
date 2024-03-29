# 2962. Count Subarrays Where Max Element Appears at Least K Times
# You are given an integer array nums and a positive integer k.
# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
# A subarray is a contiguous sequence of elements within an array.

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        max_el = max(nums)
        i = nums.index(max_el)
        j = i + 1
        freq = 1
        while freq < k and j < len(nums):
            if nums[j] == max_el:
                freq += 1
            j += 1
        if freq < k:
            return 0
        count = i + 1
        while j < len(nums):
            if nums[j] == max_el:
                i += 1
                while nums[i] != max_el:
                    i += 1
            count += i + 1
            j += 1
        return count

s = Solution()
print(s.countSubarrays([1,3,2,3,3], 2))
print(s.countSubarrays([1,4,2,1], 3))
print(s.countSubarrays([1,3,2,3,1,3], 2))