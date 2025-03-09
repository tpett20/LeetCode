# 3208. Alternating Groups II
# There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:
    # colors[i] == 0 means that tile i is red.
    # colors[i] == 1 means that tile i is blue.
# An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).
# Return the number of alternating groups.
# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        count = 0
        curr_len = 1
        arr = colors.copy()
        for i in range(k - 1):
            arr.append(colors[i])
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                curr_len += 1
                if curr_len >= k:
                    count += 1
            else:
                curr_len = 1
        return count

s = Solution()
print(s.numberOfAlternatingGroups([0,1,0,0,1,0,1], 6))