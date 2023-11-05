# 1535. Find the Winner of an Array Game
# Given an integer array arr of distinct integers and an integer k.
# A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.
# Return the integer which will win the game.
# It is guaranteed that there will be a winner of the game.

class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)
        highest = arr[0]
        wins = 0
        for i in range(1, len(arr)):
            if highest > arr[i]:
                wins += 1
            else:
                highest = arr[i]
                wins = 1
            if wins == k:
                return highest
        return highest

s = Solution()
print(s.getWinner([2,1,3,5,4,6,7], 2))
print(s.getWinner([3,2,1], 10))