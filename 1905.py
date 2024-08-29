# 1905. Count Sub Islands
# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
# Return the number of islands in grid2 that are considered sub-islands.

from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        grid = []
        for row in range(len(grid2)):
            arr = []
            for col in range(len(grid2[0])):
                arr.append(grid2[row][col])
            grid.append(arr)
        
        def check_island(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return True
            grid[r][c] = 0
            good = True
            if grid1[r][c] == 0:
                good = False
            good = check_island(r - 1, c) and good
            good = check_island(r + 1, c) and good
            good = check_island(r, c - 1) and good
            good = check_island(r, c + 1) and good
            return good
        
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and check_island(row, col) is True:
                    count += 1
        return count

s = Solution()
print(s.countSubIslands(
    [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
    [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
))