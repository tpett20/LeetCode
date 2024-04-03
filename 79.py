# 79. Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])
        def search(r, c, i, used):
            if (
                r < 0 or r == num_rows or 
                c < 0 or c == num_cols or 
                (r, c) in used or
                board[r][c] != word[i]
            ):
                return False
            if i == len(word) - 1:
                return True
            used.add((r, c))
            i += 1
            up = search(r - 1, c, i, used.copy())
            dn = search(r + 1, c, i, used.copy())
            lt = search(r, c - 1, i, used.copy())
            rt = search(r, c + 1, i, used.copy())
            return up or dn or lt or rt
        
        for row in range(num_rows):
            for col in range(num_cols):
                cell = board[row][col]
                if cell == word[0] and search(row, col, 0, set()):
                    return True
        return False

s = Solution()
print(s.exist([["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]], "ABCCED"))
print(s.exist([["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]], "SEE"))
print(s.exist([["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]], "ABCB"))
print(s.exist([["C","A","A"], ["A","A","A"], ["B","C","D"]], "AAB"))