# 1637. Widest Vertical Area Between Two Points Containing No Points
# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.
# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.
# Note that points on the edge of a vertical area are not considered included in the area.

class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        sorted_pts = sorted(points, key = list[0])
        max_width = 0
        for i in range(1, len(sorted_pts)):
            width = sorted_pts[i][0] - sorted_pts[i - 1][0]
            max_width = max(width, max_width)
        return max_width


s = Solution()
print(s.maxWidthOfVerticalArea([[8,7], [9,9], [7,4], [9,7]]))
print(s.maxWidthOfVerticalArea([[3,1], [9,0], [1,0], [1,4], [5,3], [8,8]]))