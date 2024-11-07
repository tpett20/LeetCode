# 2275. Largest Combination With Bitwise AND Greater Than Zero
# The bitwise AND of an array nums is the bitwise AND of all integers in nums.
    # For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
    # Also, for nums = [7], the bitwise AND is 7.
# You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.
# Return the size of the largest combination of candidates with a bitwise AND greater than 0.

from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_counter = [0] * 24
        for c in candidates:
            i = 0
            while c >= 1:
                if c % 2 == 1:
                    bit_counter[i] += 1
                c //= 2
                i += 1
        return max(bit_counter)

s = Solution()
print(s.largestCombination([16,17,71,62,12,24,14]))
print(s.largestCombination([8,8,8]))