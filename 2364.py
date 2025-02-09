# 2364. Count Number of Bad Pairs
# You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
# Return the total number of bad pairs in nums.

from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = n * (n - 1) // 2
        starts_freq = {}
        for i, num in enumerate(nums):
            start = num - i
            if start in starts_freq:
                starts_freq[start] += 1
            else:
                starts_freq[start] = 1
        for start in starts_freq:
            freq = starts_freq[start]
            count -= freq * (freq - 1) // 2
        return count

s = Solution()
print(s.countBadPairs([4,1,3,3]))
print(s.countBadPairs([1,2,3,4,5]))
print(s.countBadPairs([1,1,2,2,3,3]))