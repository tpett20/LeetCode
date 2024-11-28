# 2965. Find Missing and Repeated Values
# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.
# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        dbl = -1
        seen = set()
        for row in range(n):
            for col in range(n):
                cell = grid[row][col]
                if cell in seen:
                    dbl = cell
                else:
                    seen.add(cell)
        i = 1
        while True:
            if i not in seen:
                return [dbl, i]
            i += 1

s = Solution()
print(s.findMissingAndRepeatedValues([[9,1,7], [8,9,2], [3,4,6]]))