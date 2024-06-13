# 2037. Minimum Number of Moves to Seat Everyone
# There are n seats and n students in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student.
# You may perform the following move any number of times:
    # Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
# Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.
# Note that there may be multiple seats or students in the same position at the beginning.

from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        moves = 0
        s_seats = sorted(seats)
        s_stdnts = sorted(students)
        for i in range(len(students)):
            moves += abs(s_stdnts[i] - s_seats[i])
        return moves

s = Solution()
print(s.minMovesToSeat([3,1,5], [2,7,4]))
print(s.minMovesToSeat([4,1,5,9], [1,3,2,6]))
print(s.minMovesToSeat([2,2,6,6], [1,3,2,6]))