# 2461. Maximum Sum of Distinct Subarrays With Length K
# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
    # The length of the subarray is k, and
    # All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if k == 1:
            return max(nums)
        seen = set()
        max_sum = 0
        curr_sum = 0
        lt = 0
        for rt in range(len(nums)):
            while nums[rt] in seen:
                seen.remove(nums[lt])
                curr_sum -= nums[lt]
                lt += 1
            seen.add(nums[rt])
            curr_sum += nums[rt]
            if len(seen) == k:
                max_sum = max(max_sum, curr_sum)
                seen.remove(nums[lt])
                curr_sum -= nums[lt]
                lt += 1
        return max_sum

s = Solution()
print(s.maximumSubarraySum([1,5,4,2,9,9,9], 3))