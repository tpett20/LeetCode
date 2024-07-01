# 1550. Three Consecutive Odds
# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        streak = 0
        for num in arr:
            if num % 2 == 1:
                streak += 1
                if streak == 3:
                    return True
            else:
                streak = 0
        return False

s = Solution()
print(s.threeConsecutiveOdds([2,6,4,1]))
print(s.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))