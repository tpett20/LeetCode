# 1925. Count Square Sum Triples
# A square triple (a,b,c) is a triple where a, b, and c are integers and a^2 + b^2 = c^2.
# Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        sqrt_log = {}
        for c in range(1, n + 1):
            c_sq = c ** 2
            for a in range(1, c):
                a_sq = a ** 2
                b_sq = c_sq - a_sq
                if b_sq <= 0:
                    continue
                b = sqrt_log.get(b_sq, math.sqrt(b_sq))
                sqrt_log[b_sq] = b
                count += 1 if b % 1 == 0 else 0
        return count

s = Solution()
print(s.countTriples(5))
print(s.countTriples(250))