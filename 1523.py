# 1523. Count Odd Numbers in an Interval Range
# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odds = (high - low) // 2
        if high % 2 == 1 or low % 2 == 1:
            return odds + 1
        return odds
    
s = Solution()
print(s.countOdds(3, 7))
print(s.countOdds(2, 7))
print(s.countOdds(3, 8))
print(s.countOdds(2, 8))