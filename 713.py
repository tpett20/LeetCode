# 713. Subarray Product Less Than K
# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = j = count = 0
        prod = 1
        while j < len(nums):
            prod *= nums[j]
            if prod < k:
                count += j - i + 1
                j += 1
            elif i == j:
                i += 1
                j += 1
                prod = 1
            else:
                while prod >= k:
                    prod /= nums[i]
                    i += 1
                count += j - i + 1
                j += 1
        return count

s = Solution()
print(s.numSubarrayProductLessThanK([10,5,2,6], 100))
print(s.numSubarrayProductLessThanK([1,2,3], 0))