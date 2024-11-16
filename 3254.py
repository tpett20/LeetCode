# 3254. Find the Power of K-Size Subarrays I
# You are given an array of integers nums of length n and a positive integer k.
# The power of an array is defined as:
# Its maximum element if all of its elements are consecutive and sorted in ascending order.
# -1 otherwise.
# You need to find the power of all subarrays of nums of size k.
# Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1: 
            return nums
        output = [-1] * (len(nums) - k + 1)
        i = 0
        j = 1
        while i < len(output):
            while j < (i + k) and nums[j] == nums[j - 1] + 1:
                j += 1
            if j == i + k:
                output[i] = nums[j - 1]
                i += 1
            else:
                i = j
                j += 1
        return output

s = Solution()
print(s.resultsArray([1,2,3,4,3,2,5], 3))