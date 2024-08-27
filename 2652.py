# 2652. Sum Multiples
# Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.
# Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        nums = set()
        divs = [3, 5, 7]
        for div in divs:
            for i in range(div, n + 1, div):
                nums.add(i)
        return sum(nums)
    
s = Solution()
print(s.sumOfMultiples(7))
print(s.sumOfMultiples(1000))