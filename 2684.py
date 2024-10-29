# 2684. Maximum Number of Moves in a Grid
# You are given a 0-indexed m x n matrix grid consisting of positive integers.
# You can start at any cell in the first column of the matrix, and traverse the grid in the following way:
    # From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
# Return the maximum number of moves that you can perform.

from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def dfs(row, col, last_val=-1):
            if (row == len(grid) or col == len(grid[0]) or 
                grid[row][col] <= last_val):
                return 0
            if ref[row][col] != -1:
                return ref[row][col]
            val = grid[row][col]
            grid[row][col] = -1
            up = dfs(row - 1, col + 1, val) if row > 0 else 0
            dn = dfs(row + 1, col + 1, val) if row < len(grid) - 1 else 0
            rt = dfs(row, col + 1, val)
            grid[row][col] = val
            ret_val = max(up, dn, rt) + 1
            ref[row][col] = ret_val
            return ret_val
        
        ref = []
        for _ in range(len(grid)):
            ref.append([-1] * len(grid[0]))
        max_moves = 0
        for row in range(len(grid)):
            max_moves = max(max_moves, dfs(row, 0))
        return max_moves - 1

test_case = [
    [2,4,3,5],
    [5,4,9,3],
    [3,4,2,11],
    [10,9,13,15]
]
s = Solution()
print(s.maxMoves(test_case))