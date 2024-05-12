# 2373. Largest Local Values in a Matrix
# You are given an n x n integer matrix grid.
# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
    # maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
# Return the generated matrix.

from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        output = []
        r_s, r_e = 0, 2
        while r_e < len(grid):
            c_s, c_e = 0, 2
            max_row = []
            while c_e < len(grid[0]):
                max_val = 0
                for row in range(r_s, r_e + 1):
                    for col in range(c_s, c_e + 1):
                        max_val = max(max_val, grid[row][col])
                max_row.append(max_val)
                c_s += 1
                c_e += 1
            r_s += 1
            r_e += 1
            output.append(max_row)
        return output

s = Solution()
print(s.largestLocal([[9,9,8,1], [5,6,2,6], [8,2,6,4], [6,2,2,2]]))
print(s.largestLocal([[1,1,1,1,1], [1,1,1,1,1], [1,1,2,1,1], [1,1,1,1,1], [1,1,1,1,1]]))