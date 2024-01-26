# 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row = flr_row = col = flr_col = 0
        ceil_row = len(matrix) - 1
        ceil_col = len(matrix[0]) - 1
        output = []
        total_els = len(matrix) * len(matrix[0])
        while len(output) < total_els:
            if col <= ceil_col:
                while col <= ceil_col:
                    output.append(matrix[row][col])
                    col += 1
                col -= 1
                flr_row += 1
                row += 1
            if len(output) == total_els:
                break
            if row <= ceil_row:
                while row <= ceil_row:
                    output.append(matrix[row][col])
                    row += 1
                row -= 1
                ceil_col -= 1
                col -= 1
            if len(output) == total_els:
                break
            if col >= flr_col:
                while col >= flr_col:
                    output.append(matrix[row][col])
                    col -= 1
                col += 1
                ceil_row -= 1
                row -= 1
            if len(output) == total_els:
                break
            if row >= flr_row:
                while row >= flr_row:
                    output.append(matrix[row][col])
                    row -= 1
                row += 1
                flr_col += 1
                col += 1
        return output

s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))