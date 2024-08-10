# 840. Magic Squares In Grid
# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
# Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?
# Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check_sq_rules(start):
            r_start, c_start = start
            cells = set()
            for row in range(3):
                for col in range(3):
                    cell = grid[r_start + row][c_start + col]
                    if cell in cells or cell > 9 or cell < 1:
                        return False
                    cells.add(cell)
            return True
        
        count = 0
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                if check_sq_rules([row, col]) is False:
                    continue
                target_sum = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
                # horizontal
                if target_sum != (grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]):
                    continue
                if target_sum != (grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]):
                    continue
                # vertical
                if target_sum != (grid[row][col] + grid[row + 1][col] + grid[row + 2][col]):
                    continue
                if target_sum != (grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]):
                    continue
                if target_sum != (grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]):
                    continue
                # diagonal
                if target_sum != (grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]):
                    continue
                if target_sum != (grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]):
                    continue
                count += 1
        return count

s = Solution()
print(s.numMagicSquaresInside([[4,3,8,4], [9,5,1,9], [2,7,6,2]]))