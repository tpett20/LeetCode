# 2200. Find All K-Distant Indices in an Array
# You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.
# Return a list of all k-distant indices sorted in increasing order.

from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        output = []
        key_idxs = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == key:
                key_idxs.append(i)
        next_idx = key_idxs.pop()
        i = max(next_idx - k, 0)
        while i < len(nums):
            while i < len(nums) and abs(next_idx - i) <= k:
                output.append(i)
                i += 1
            if len(key_idxs):
                next_idx = key_idxs.pop()
            else:
                break
            i = max(next_idx - k, i)
        return output

s = Solution()
print(s.findKDistantIndices([3,4,9,1,3,9,5], 9, 1))
print(s.findKDistantIndices([2,2,2,2,2], 2, 2))