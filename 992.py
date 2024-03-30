# 992. Subarrays with K Different Integers
# Given an integer array nums and an integer k, return the number of good subarrays of nums.
# A good array is an array where the number of different integers in that array is exactly k.
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = i = 0
        freq = {}
        for j in range(0, len(nums)):
            if nums[j] in freq:
                freq[nums[j]] += 1
            else:
                freq[nums[j]] = 1
            while len(freq) > k:
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]
                i += 1
            if len(freq) == k:
                c_freq = freq.copy()
                l = i
                while len(c_freq) == k:
                    count += 1
                    c_freq[nums[l]] -= 1
                    if c_freq[nums[l]] == 0:
                        del c_freq[nums[l]]
                    l += 1
        return count

s = Solution()
print(s.subarraysWithKDistinct([1,2,1,2,3], 2))
print(s.subarraysWithKDistinct([1,2,1,3,4], 3))
print(s.subarraysWithKDistinct([1,2,3,4], 1))
print(s.subarraysWithKDistinct([1,2,3,3,1], 2))