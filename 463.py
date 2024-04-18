# 463. Island Perimeter
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        sides = 0
        height = len(grid)
        width = len(grid[0])
        for row in range(height):
            for col in range(width):
                if grid[row][col] == 0:
                    continue
                if row == 0 or grid[row - 1][col] == 0:
                    sides += 1
                if row == height - 1 or grid[row + 1][col] == 0:
                    sides += 1
                if col == 0 or grid[row][col - 1] == 0:
                    sides += 1
                if col == width - 1 or grid[row][col + 1] == 0:
                    sides += 1
        return sides

s = Solution()
print(s.islandPerimeter([[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]))