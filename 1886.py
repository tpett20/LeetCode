# 1886. Determine Whether Matrix Can Be Obtained By Rotation
# Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

from typing import List

class Solution:
    def grids_match(self, grid1: List[List[int]], grid2: List[List[int]]) -> bool:
        n = len(grid1)
        for r in range(n):
            if grid1[r] != grid2[r]:
                return False
        return True

    def rotate_grid(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        new_grid = []
        for c in range(n):
            row = []
            for r in range(n - 1, -1, -1):
                row.append(grid[r][c])
            new_grid.append(row)
        return new_grid

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if self.grids_match(mat, target):
            return True
        grid = mat
        for i in range(3):
            grid = self.rotate_grid(grid)
            if self.grids_match(grid, target):
                return True
        return False