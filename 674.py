# 674. Longest Continuous Increasing Subsequence
# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
# A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        max_length = 1
        length = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                length += 1
                max_length = max(length, max_length)
            else:
                length = 1
        return max_length

s = Solution()
print(s.findLengthOfLCIS([1,3,5,4,7]))
print(s.findLengthOfLCIS([2,2,2,2,2]))