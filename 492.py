# 492. Construct the Rectangle
# A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
    # The area of the rectangular web page you designed must equal to the given target area.
    # The width W should not be larger than the length L, which means L >= W.
    # The difference between length L and width W should be as small as possible.
# Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.

import math
from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = math.sqrt(area)
        if w % 1 == 0:
            w = int(w)
            return [w, w]
        w = math.floor(w)
        while area % w != 0:
            w -= 1
        return [area // w, w]

s = Solution()
print(s.constructRectangle(4))
print(s.constructRectangle(37))
print(s.constructRectangle(122122))