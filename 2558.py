# 2558. Take Gifts From the Richest Pile
# You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:
    # Choose the pile with the maximum number of gifts.
    # If there is more than one pile with the maximum number of gifts, choose any.
    # Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
# Return the number of gifts remaining after k seconds.

from math import floor, sqrt
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        g = sorted(gifts)
        for _ in range(k):
            if g[-1] == 1:
                break
            g[-1] = floor(sqrt(g[-1]))
            g.sort()
        return sum(g)

s = Solution()
print(s.pickGifts([25,64,9,4,100], 4))
print(s.pickGifts([1,1,1,1], 1000))