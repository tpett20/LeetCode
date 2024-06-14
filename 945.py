# 945. Minimum Increment to Make Array Unique
# You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
# Return the minimum number of moves to make every value in nums unique.
# The test cases are generated so that the answer fits in a 32-bit integer.

from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        moves = 0
        nums_set = set()
        duplicates = []
        for num in nums:
            if num in nums_set:
                duplicates.append(num)
            else:
                nums_set.add(num)
        duplicates.sort(reverse=True)
        i = 0
        while duplicates:
            num = duplicates.pop()
            if num >= i:
                i = num
            else:
                moves += (i - num)
            while i in nums_set:
                i += 1
                moves += 1
            nums_set.add(i)
            i += 1
        return moves

s = Solution()
print(s.minIncrementForUnique([1,2,2]))
print(s.minIncrementForUnique([3,2,1,2,1,7]))
print(s.minIncrementForUnique([1,1,1,2,3,4,5]))