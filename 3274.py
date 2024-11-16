# 3274. Check if Two Chessboard Squares Have the Same Color
# You are given two strings, coordinate1 and coordinate2, representing the coordinates of a square on an 8 x 8 chessboard.
# Return true if these two squares have the same color and false otherwise.
# The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first (indicating its column), and the number second (indicating its row).

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def get_parity(string):
            row = ord(string[0]) - 97
            col = int(string[1:])
            return [row % 2, col % 2]
        
        row_parity1, col_parity1 = get_parity(coordinate1)
        row_parity2, col_parity2 = get_parity(coordinate2)
        return abs(row_parity1 - col_parity1) == abs(row_parity2 - col_parity2)
    
s = Solution()
print(s.checkTwoChessboards("a1", "c3"))
print(s.checkTwoChessboards("a1", "a2"))