# 2500. Delete Greatest Value in Each Row
# You are given an m x n matrix grid consisting of positive integers.
# Perform the following operation until grid becomes empty:
    # Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
    # Add the maximum of deleted elements to the answer.
# Note that the number of columns decreases by one after each operation.
# Return the answer after performing the operations described above.

from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        s_grid = []
        for row in grid:
            s_grid.append(sorted(row))
        output = 0
        while len(s_grid[0]):
            removed = []
            for row in s_grid:
                removed.append(row.pop())
            output += max(removed)
        return output

s = Solution()
print(s.deleteGreatestValue([[1,2,4], [3,3,1]]))
print(s.deleteGreatestValue([[10]]))