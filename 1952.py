# 1952. Three Divisors
# Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.
# An integer m is a divisor of n if there exists an integer k such that n = k * m.

class Solution:
    def isThree(self, n: int) -> bool:
        divs = set()
        l = 1
        r = n
        while l < r and len(divs) < 5:
            if n % l == 0:
                r = n // l
                divs.update((l, r))
            l += 1
        return len(divs) == 3

s = Solution()
print(s.isThree(169))
print(s.isThree(1969))