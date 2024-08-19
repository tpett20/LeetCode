# 1491. Average Salary Excluding the Minimum and Maximum Salary
# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        lo = float('inf')
        hi = float('-inf')
        for s in salary:
            total += s
            lo = min(lo, s)
            hi = max(hi, s)
        total -= (lo + hi)
        return total / (len(salary) - 2)

s = Solution()
print(s.average([4000, 3000, 1000, 2000]))
print(s.average([1000, 2000, 3000]))