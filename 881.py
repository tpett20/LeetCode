# 881. Boats to Save People
# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
# Return the minimum number of boats to carry every given person.

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        s_p = sorted(people)
        boats = l = 0
        r = len(s_p) - 1
        while l <= r:
            if s_p[l] + s_p[r] <= limit:
                l += 1
            r -= 1
            boats += 1
        return boats

s = Solution()
print(s.numRescueBoats([1,2], 3))
print(s.numRescueBoats([3,2,2,1], 3))
print(s.numRescueBoats([3,5,3,4], 5))