# 1503. Last Moment Before All Ants Fall Out of a Plank
# We have a wooden plank of the length n units. Some ants are walking on the plank, each ant moves with a speed of 1 unit per second. Some of the ants move to the left, the other move to the right.
# When two ants moving in two different directions meet at some point, they change their directions and continue moving again. Assume changing directions does not take any additional time.
# When an ant reaches one end of the plank at a time t, it falls out of the plank immediately.
# Given an integer n and two integer arrays left and right, the positions of the ants moving to the left and the right, return the moment when the last ant(s) fall out of the plank.

class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        left_time = right_time = 0
        if len(left):
            left_time = max(left)
        if len(right):
            right_time = n - min(right)
        return max(left_time, right_time)

s = Solution()
print(s.getLastMoment(4, [4,3], [0,1]))
print(s.getLastMoment(7, [], [0,1,2,3,4,5,6,7]))
print(s.getLastMoment(7, [0,1,2,3,4,5,6,7], []))