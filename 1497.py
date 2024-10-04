# 1497. Check If Array Pairs Are Divisible by k
# Given an array of integers arr of even length n and an integer k.
# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
# Return true If you can find a way to do that or false otherwise.

from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        r_counts = {}
        for num in arr:
            r = num % k
            if r in r_counts:
                r_counts[r] += 1
            else:
                r_counts[r] = 1
        if 0 in r_counts:
            if r_counts[0] % 2 != 0:
                return False
            del r_counts[0]
        for r in r_counts:
            r_partner = k - r
            r_partner_freq = r_counts.get(r_partner, -1)
            if r_counts[r] != r_partner_freq:
                return False
        return True

s = Solution()
print(s.canArrange([1,2,3,4,5,10,6,7,8,9], 5))
print(s.canArrange([1,2,3,4,5,6], 7))
print(s.canArrange([1,2,3,4,5,6], 10))