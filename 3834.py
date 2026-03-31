# 3834. Merge Adjacent Equal Elements
# You are given an integer array nums.
# You must repeatedly apply the following merge operation until no more changes can be made:
    # If any two adjacent elements are equal, choose the leftmost such adjacent pair in the current array and replace them with a single element equal to their sum.
# After each merge operation, the array size decreases by 1. Repeat the process on the updated array until no more changes can be made.
# Return the final array after all possible merge operations.

from typing import List

class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack[-1] *= 2
        return stack

s = Solution()
print(s.mergeAdjacent([8, 4, 2, 1, 1]))