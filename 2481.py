# 2481. Minimum Cuts to Divide a Circle
# A valid cut in a circle can be:
    # A cut that is represented by a straight line that touches two points on the edge of the circle and passes through its center, or
    # A cut that is represented by a straight line that touches one point on the edge of the circle and its center.
# Some valid and invalid cuts are shown in the figures below.

class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return n // 2
        return n

s = Solution()
print(s.numberOfCuts(4))
print(s.numberOfCuts(1))
print(s.numberOfCuts(5))