# 1266. Minimum Time Visiting All Points
# On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.
# You can move according to these rules:
# - In 1 second, you can either:
#   - move vertically by one unit,
#   - move horizontally by one unit, or
#   - move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
# - You have to visit the points in the same order as they appear in the array.
# - You are allowed to pass through points that appear later in the order, but these do not count as visits.

class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        time = 0
        for i in range(len(points) - 1):
            curr = points[i]
            next = points[i + 1]
            time += max(abs(next[0] - curr[0]), abs(next[1] - curr[1]))
        return time

s = Solution()
print(s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
print(s.minTimeToVisitAllPoints([[3,2],[-2,2]]))