# 3206. Alternating Groups I
# There is a circle of red and blue tiles. You are given an array of integers colors. The color of tile i is represented by colors[i]:
    # colors[i] == 0 means that tile i is red.
    # colors[i] == 1 means that tile i is blue.
# Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different color from its left and right tiles) is called an alternating group.
# Return the number of alternating groups.
# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        i = 0
        while i < len(colors) - 1:
            if colors[i - 1] != colors[i] != colors[i + 1]:
                count += 1
            i += 1
        if colors[i - 1] != colors[i] != colors[0]:
            count += 1
        return count

s = Solution()
print(s.numberOfAlternatingGroups([0,1,0,0,1]))