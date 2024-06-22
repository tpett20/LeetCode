# 1248. Count Number of Nice Subarrays
# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def is_even(num):
            return num % 2 == 0
        
        l = 0
        while l < len(nums) and is_even(nums[l]):
            l += 1
        pre_evens = l
        count = odds = 0
        for r in range(l, len(nums)):
            if not is_even(nums[r]):
                odds += 1
                if odds > k:
                    l += 1
                    odds -= 1
                    pre_evens = 0
                    while is_even(nums[l]):
                        pre_evens += 1
                        l += 1
            if odds == k:
                count += (pre_evens + 1)
        return count

s = Solution()
print(s.numberOfSubarrays([1,1,2,1,1], 3))
print(s.numberOfSubarrays([1,1,2,1,1], 1))
print(s.numberOfSubarrays([2,4,6], 1))
print(s.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))