# 3158. Find the XOR of Numbers Which Appear Twice
# 🏆 Biweekly Contest 131 - Solved Problem in 4:16
# You are given an array nums, where each number in the array appears either once or twice.
# Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.

from typing import List

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        m = {}
        a = []
        output = 0
        for num in nums:
            if num in m:
                a.append(num)
            else:
                m[num] = True
        for num in a:
            output ^= num
        return output

s = Solution()
print(s.duplicateNumbersXOR([1,2,1,3]))
print(s.duplicateNumbersXOR([1,2,3]))
print(s.duplicateNumbersXOR([1,2,2,1]))