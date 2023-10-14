# 2027. Minimum Moves to Convert String
# You are given a string s consisting of n characters which are either 'X' or 'O'.
# A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note that if a move is applied to the character 'O', it will stay the same.
# Return the minimum number of moves required so that all the characters of s are converted to 'O'.

class Solution:
    def minimumMoves(self, s: str) -> int:
        moves = 0
        i = 0
        while i < len(s):
            if s[i] == 'X':
                moves += 1
                i += 3
            else: 
                i += 1
        return moves
    
s = Solution()
print(s.minimumMoves('XXX'))
print(s.minimumMoves('OXOXOO'))
print(s.minimumMoves('OOXXOXXOXXX'))