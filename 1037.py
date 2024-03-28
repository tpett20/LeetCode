# 1037. Valid Boomerang
# Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.
# A boomerang is a set of three points that are all distinct and not in a straight line.

from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False
        
        xDiff1 = points[1][0] - points[0][0]
        if xDiff1 == 0:
            slope1 = float('inf')
        else:
            slope1 = (points[1][1] - points[0][1]) / xDiff1
        xDiff2 = points[2][0] - points[1][0]
        if xDiff2 == 0:
            slope2 = float('inf')
        else:
            slope2 = (points[2][1] - points[1][1]) / xDiff2
        return slope1 != slope2

s = Solution()
print(s.isBoomerang([[1,1],[2,3],[3,2]]))
print(s.isBoomerang([[1,1],[2,2],[3,3]]))
print(s.isBoomerang([[0,1],[2,0],[1,1]]))