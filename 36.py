# 36. Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    # Each row must contain the digits 1-9 without repetition.
    # Each column must contain the digits 1-9 without repetition.
    # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
    # A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    # Only the filled cells need to be validated according to the mentioned rules.

from typing import List

class Solution:
    def is_valid_sub_box(self, grid: List[List[str]], r: int, c: int) -> bool:
        seen = set()
        for row in range(r, r + 3):
            for col in range(c, c + 3):
                cell = grid[row][col]
                if cell.isnumeric() and cell in seen:
                    return False
                seen.add(cell)
        return True

    def has_valid_rows_and_cols(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        for row in range(n):
            seen = set()
            for col in range(n):
                cell = grid[row][col]
                if cell.isnumeric() and cell in seen:
                    return False
                seen.add(cell)
        for col in range(n):
            seen = set()
            for row in range(n):
                cell = grid[row][col]
                if cell.isnumeric() and cell in seen:
                    return False
                seen.add(cell)
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        if not self.has_valid_rows_and_cols(board):
            return False
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not self.is_valid_sub_box(board, row, col):
                    return False
        return True