# 773. Sliding Puzzle
# On a 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
# Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def get_board_state(brd):
            string = ""
            for row in range(len(brd)):
                for col in range(len(brd[0])):
                    string += str(brd[row][col])
            return string
       
        def duplicate_board(brd):
            return [brd[0].copy(), brd[1].copy()]
        
        start_grid = duplicate_board(board)
        start_zero_row = 0 if 0 in board[0] else 1
        start_zero_col = board[start_zero_row].index(0)
        seen = set()
        depth = -1
        q = [[start_grid, start_zero_row, start_zero_col]]
        while q:
            q_len = len(q)
            depth += 1
            for _ in range(q_len):
                grid, zero_row, zero_col = q.pop(0)
                state = get_board_state(grid)
                if state == "123450":
                    return depth
                elif state in seen:
                    continue
                seen.add(state)
                if zero_col == 0 or zero_col == 1:
                    rt_board = duplicate_board(grid)
                    rt_board[zero_row][zero_col] = rt_board[zero_row][zero_col + 1]
                    rt_board[zero_row][zero_col + 1] = 0
                    q.append([rt_board, zero_row, zero_col + 1])
                if zero_col == 2 or zero_col == 1:
                    lt_board = duplicate_board(grid)
                    lt_board[zero_row][zero_col] = lt_board[zero_row][zero_col - 1]
                    lt_board[zero_row][zero_col - 1] = 0
                    q.append([lt_board, zero_row, zero_col - 1])
                if zero_row == 0:
                    dn_board = duplicate_board(grid)
                    dn_board[zero_row][zero_col] = dn_board[zero_row + 1][zero_col]
                    dn_board[zero_row + 1][zero_col] = 0
                    q.append([dn_board, zero_row + 1, zero_col])
                else:
                    up_board = duplicate_board(grid)
                    up_board[zero_row][zero_col] = up_board[zero_row - 1][zero_col]
                    up_board[zero_row - 1][zero_col] = 0
                    q.append([up_board, zero_row - 1, zero_col])
        return -1

s = Solution()
print(s.slidingPuzzle([[1, 2, 3], [4, 0, 5]]))
print(s.slidingPuzzle([[1, 4, 3], [5, 0, 2]]))
print(s.slidingPuzzle([[0, 3, 2], [4, 5, 1]]))