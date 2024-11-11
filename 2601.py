# 2601. Prime Subtraction Operation
# You are given a 0-indexed integer array nums of length n.
# You can perform the following operation as many times as you want:
    # Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
# Return true if you can make nums a strictly increasing array using the above operation and false otherwise.
# A strictly increasing array is an array whose each element is strictly greater than its preceding element.

from typing import List

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def check_prime(n):
            if n == 1:
                return False
            ceil = n // 2 + 1
            for i in range(2, ceil):
                if n % i == 0:
                    return False
            return True
        
        prev = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < prev:
                prev = nums[i]
                continue
            p = nums[i] - (prev - 1)
            while check_prime(p) is False and p < nums[i]:
                p += 1
            if p == nums[i]:
                return False
            prev = nums[i] - p
        return True

s = Solution()
print(s.primeSubOperation([4,9,6,10]))
print(s.primeSubOperation([5,8,3]))