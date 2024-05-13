# 861. Score After Flipping Matrix
# You are given an m x n binary matrix grid.
# A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
# Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
# Return the highest possible score after making any number of moves (including zero moves).

from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in grid:
            reg = ""
            flip = ""
            for cell in row:
                if cell == 1:
                    reg += "1"
                    flip += "0"
                else:
                    reg += "0"
                    flip += "1"
            if flip > reg:
                for col in range(len(row)):
                    row[col] = 1 if row[col] == 0 else 0
        for col in range(len(grid[0])):
            reg_ones = 0
            flip_ones = 0
            for row in range(len(grid)):
                if grid[row][col] == 1:
                    reg_ones += 1
                else:
                    flip_ones += 1
            if flip_ones > reg_ones:
                for row in range(len(grid)):
                    grid[row][col] = 1 if grid[row][col] == 0 else 0
        score = 0
        for row in grid:
            b = ""
            for col in row:
                b += str(col)
            score += int(b, 2)
        return score

s = Solution()
print(s.matrixScore([[0,0,1,1], [1,0,1,0], [1,1,0,0]]))
print(s.matrixScore([[0]]))
print(s.matrixScore([[1,0,0,0], [0,0,0,0], [0,0,0,0]]))