# 885. Spiral Matrix III
# You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.
# You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.
# Return an array of coordinates representing the positions of the grid in the order you visited them

from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        total_cells = rows * cols
        row = rStart
        col = cStart
        visited = [[row, col]]
        row_flr = row_ceil = row
        col_flr = col_ceil = col
        while len(visited) < total_cells:
            # right
            while col <= col_ceil:
                col += 1
                if 0 <= row < rows and 0 <= col < cols:
                    visited.append([row, col])
            col_ceil = min(cols, col_ceil + 1)
            # down
            while row <= row_ceil:
                row += 1
                if 0 <= row < rows and 0 <= col < cols:
                    visited.append([row, col])
            row_ceil = min(rows, row_ceil + 1)
            # left
            while col >= col_flr:
                col -= 1
                if 0 <= row < rows and 0 <= col < cols:
                    visited.append([row, col])
            col_flr = max(-1, col_flr - 1)
            # up
            while row >= row_flr:
                row -= 1
                if 0 <= row < rows and 0 <= col < cols:
                    visited.append([row, col])
            row_flr = max(-1, row_flr - 1)
        return visited
    
s = Solution()
print(s.spiralMatrixIII(5, 6, 1, 4))