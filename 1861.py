# 1861. Rotating the Box
# You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:
    # A stone '#'
    # A stationary obstacle '*'
    # Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.
# It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.
# Return an n x m matrix representing the box after the rotation described above.

from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        rotated = []
        for r in range(n):
            row = []
            for c in range(m):
                row.append(".")
            rotated.append(row)
        for r in range(m):
            stones = 0
            for c in range(n):
                cell = boxGrid[r][c]
                if cell == "#":
                    stones += 1
                elif cell == "*":
                    for i in range(stones):
                        rotated[c - i - 1][m - r - 1] = "#"
                    rotated[c][m - r - 1] = "*"
                    stones = 0
            for i in range(stones):
                rotated[n - i - 1][m - r - 1] = "#"
        return rotated

s = Solution()
test_case = [
    ["#",".","*","#","*","."],
    ["#","#","#",".","*","."],
    ["#","#","#",".","#","."]
]
result = s.rotateTheBox(test_case)
for row in result:
    print(row)