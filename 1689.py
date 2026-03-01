# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
# A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
# Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

class Solution:
    def minPartitions(self, n: str) -> int:
        hi = "0"
        for digit in n:
            hi = max(digit, hi)
            if hi == "9":
                return 9
        return int(hi)

s = Solution()
print(s.minPartitions("111"))
print(s.minPartitions("9"))