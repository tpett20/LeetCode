# 1390. Four Divisors
# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        cache = {}
        for num in nums:
            if num in cache:
                total += cache[num]
                continue
            i = 1
            sub_total = 0
            divisors = set()
            while i <= num / i and len(divisors) <= 4:
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
                    sub_total += (num // i) + i
                i += 1
            if len(divisors) == 4:
                total += sub_total
                cache[num] = sub_total
            else:
                cache[num] = 0
        return total

s = Solution()
print(s.sumFourDivisors([36, 38]))