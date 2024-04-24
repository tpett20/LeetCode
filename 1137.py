# 1137. N-th Tribonacci Number
# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

class Solution:
    def tribonacci(self, n: int) -> int:
        seq = [0, 1, 1]
        if n < 3:
            return seq[n]
        i = 3
        while i <= n:
            nxt = sum(seq)
            seq[0] = seq[1]
            seq[1] = seq[2]
            seq[2] = nxt
            i += 1
        return nxt

s = Solution()
print(s.tribonacci(4))
print(s.tribonacci(25))
print(s.tribonacci(37))