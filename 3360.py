# 3360. Stone Removal Game
# Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.
# Alice starts by removing exactly 10 stones on her first turn.
# For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
# The player who cannot make a move loses the game.
# Given a positive integer n, return true if Alice wins the game and false otherwise.

class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = n
        turn = 10
        count = 1
        while True:
            stones -= turn
            if stones < 0:
                return count % 2 == 0
            turn -= 1
            count += 1

s = Solution()
print(s.canAliceWin(15))
print(s.canAliceWin(16))
print(s.canAliceWin(1))