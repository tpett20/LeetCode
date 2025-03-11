# 1403. Minimum Subsequence in Non-Increasing Order
# Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence. 
# If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 
# Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.

from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        s_nums = sorted(nums)
        pull_sum = 0
        rem_sum = sum(nums)
        subseq = []
        while pull_sum <= rem_sum:
            curr = s_nums.pop()
            subseq.append(curr)
            pull_sum += curr
            rem_sum -= curr
        return subseq

s = Solution()
print(s.minSubsequence([4,3,10,9,8]))
print(s.minSubsequence([1,1,1,100]))