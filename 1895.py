# 1895. Largest Magic Square
# A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.
# Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

from typing import List

class Solution:
    def is_magic_square(self, row_sums: List[int], col_sums: List[int], diag1: int, diag2: int) -> bool:
        if diag1 != diag2:
            return False
        rule = diag1
        for row_sum in row_sums:
            if row_sum != rule:
                return False
        for col_sum in col_sums:
            if col_sum != rule:
                return False
        return True

    def get_max_magic_size(self, grid: List[List[int]], row: int, col: int) -> int:
        m = len(grid)
        n = len(grid[0])
        size = max_size = 1
        start_row = row
        start_col = col
        row_sums = []
        col_sums = []
        diag_sum_rt = 0
        diag_sum_lt = 0
        while row < m and col < n:
            for i in range(len(row_sums)):
                row_sums[i] += grid[start_row + i][col]
            row_sums.append(sum(grid[row][start_col:col + 1]))
            for i in range(len(col_sums)):
                col_sums[i] += grid[row][start_col + i]
            new_col_sum = 0
            for i in range(size):
                new_col_sum += grid[start_row + i][col]
            col_sums.append(new_col_sum)
            diag_sum_rt += grid[row][col]
            diag_sum_lt = 0
            for i in range(size):
                diag_sum_lt += grid[start_row + i][col - i]
            if self.is_magic_square(row_sums, col_sums, diag_sum_rt, diag_sum_lt):
                max_size = size
            row += 1
            col += 1
            size += 1
        return max_size

    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        max_magic = 1
        m = len(grid)
        n = len(grid[0])
        r = 0
        while r < m - max_magic:
            c = 0
            while c < n - max_magic:
                max_magic = max(max_magic, self.get_max_magic_size(grid, r, c))
                c += 1
            r += 1
        return max_magic

test_case = [
    [7,1,4,5,6],
    [2,5,1,6,4],
    [1,5,4,3,2],
    [1,2,7,3,4]
]
s = Solution()
print(s.largestMagicSquare(test_case))