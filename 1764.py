# 1764. Form Array by Concatenating Subarrays of Another Array
# You are given a 2D integer array groups of length n. You are also given an integer array nums.
# You are asked if you can choose n disjoint subarrays from the array nums such that the ith subarray is equal to groups[i] (0-indexed), and if i > 0, the (i-1)th subarray appears before the ith subarray in nums (i.e. the subarrays must be in the same order as groups).
# Return true if you can do this task, and false otherwise.
# Note that the subarrays are disjoint if and only if there is no index k such that nums[k] belongs to more than one subarray. A subarray is a contiguous sequence of elements within an array.

from typing import List

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = j = 0
        while i < len(groups) and j < len(nums):
            if nums[j] == groups[i][0]:
                group_len = len(groups[i])
                block = nums[j:j + group_len]
                if block == groups[i]:
                    i += 1
                    j += group_len - 1
            j += 1
        return i == len(groups)

s = Solution()
print(s.canChoose([[1,-1,-1],[3,-2,0]], [1,-1,0,1,-1,-1,3,-2,0]))
print(s.canChoose([[1,-1,-1],[3,-2,0]], [1,-1,0,1,-1,-1,3,-2,1,0]))