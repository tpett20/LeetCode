# 1829. Maximum XOR for Each Query
# You are given a sorted array nums of n non-negative integers and an integer maximumBit. You want to perform the following query n times:
    # 1. Find a non-negative integer k < 2maximumBit such that nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to the ith query.
    # 2. Remove the last element from the current array nums.
# Return an array answer, where answer[i] is the answer to the ith query.

from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], max_bit: int) -> List[int]:
        answer = []
        total_XOR = 0
        max_int = (2 ** max_bit) - 1
        for num in nums:
            total_XOR ^= num
        for i in range(len(nums) - 1, -1, -1):
            answer.append(total_XOR ^ max_int)
            total_XOR ^= nums[i]
        return answer

s = Solution()
print(s.getMaximumXor([0,1,1,3], 2))
print(s.getMaximumXor([0,1,2,2,5,7], 3))