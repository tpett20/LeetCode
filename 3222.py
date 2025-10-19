# 3222. Find the Winning Player in Coin Game
# You are given two positive integers x and y, denoting the number of coins with values 75 and 10 respectively.
# Alice and Bob are playing a game. Each turn, starting with Alice, the player must pick up coins with a total value 115. If the player is unable to do so, they lose the game.
# Return the name of the player who wins the game if both players play optimally.

class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        alice_wins = False
        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            alice_wins = not alice_wins
        return "Alice" if alice_wins else "Bob"

s = Solution()
print(s.winningPlayer(4, 16))
print(s.winningPlayer(5, 20))