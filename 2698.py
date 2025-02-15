# 2698. Find the Punishment Number of an Integer
# Given a positive integer n, return the punishment number of n.
# The punishment number of n is defined as the sum of the squares of all integers i such that:
    # 1 <= i <= n
    # The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.

from typing import List

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(target: int, parts: List[int], remainder: str) -> bool:
            if not remainder:
                return sum(parts) == target
            for i in range(len(remainder)):
                p = parts.copy()
                p.append(int(remainder[:i + 1]))
                if can_partition(target, p, remainder[i + 1:]):
                    return True
            return False
        
        res = 0
        for i in range(1, n + 1):
            sq = i * i
            digits = str(sq)
            if can_partition(i, [], digits):
                res += sq
        return res

s = Solution()
print(s.punishmentNumber(1000))