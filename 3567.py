# 3567. Minimum Absolute Difference in Sliding Submatrix
# You are given an m x n integer matrix grid and an integer k.
# For every contiguous k x k submatrix of grid, compute the minimum absolute difference between any two distinct values within that submatrix.
# Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is the minimum absolute difference in the submatrix whose top-left corner is (i, j) in grid.
# Note: If all elements in the submatrix have the same value, the answer will be 0.
# A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all cells matrix[x][y] where x1 <= x <= x2 and y1 <= y <= y2.

from typing import List

class Solution:
    def get_min_abs_diff(self, grid: List[List[int]], k: int, x: int, y: int) -> int:
        min_diff = float("inf")
        cells_set = set()
        for r in range(k):
            for c in range(k):
                cell = grid[x + r][y + c]
                cells_set.add(cell)
        if len(cells_set) == 1:
            return 0
        cells = sorted(list(cells_set))
        for i in range(1, len(cells)):
            curr, prev = cells[i], cells[i - 1]
            min_diff = min(curr - prev, min_diff)
        return min_diff

    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        res = []
        m = len(grid)
        n = len(grid[0])
        for r in range(m - k + 1):
            res_row = []
            for c in range(n - k + 1):
                res_row.append(self.get_min_abs_diff(grid, k, r, c))
            res.append(res_row)
        return res