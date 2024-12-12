# 2779. Maximum Beauty of an Array After Applying Operation
# You are given a 0-indexed array nums and a non-negative integer k.
# In one operation, you can do the following:
    # Choose an index i that hasn't been chosen before from the range [0, nums.length - 1].
    # Replace nums[i] with any integer from the range [nums[i] - k, nums[i] + k].
# The beauty of the array is the length of the longest subsequence consisting of equal elements.
# Return the maximum possible beauty of the array nums after applying the operation any number of times.
# Note that you can apply the operation to each index only once.
# A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the order of the remaining elements.

from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        arr = sorted(nums)
        max_len = 1
        lt = 0
        for rt in range(1, len(arr)):
            max_start = arr[lt] + k
            min_curr = arr[rt] - k
            while min_curr > max_start:
                lt += 1
                max_start = arr[lt] + k
            max_len = max(max_len, (rt - lt) + 1)
        return max_len

s = Solution()
print(s.maximumBeauty([4,6,1,2], 2))
print(s.maximumBeauty([10,10,10,15], 3))