# 342. Power of Four
# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.

import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return math.log(n, 4) % 1 == 0

s = Solution()
print(s.isPowerOfFour(16))
print(s.isPowerOfFour(5))
print(s.isPowerOfFour(1))
print(s.isPowerOfFour(4))