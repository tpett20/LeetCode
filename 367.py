# 367. Valid Perfect Square
# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
# You must not use any built-in library function, such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        flr, ceil = 2, num // 2
        while flr <= ceil:
            mid = (flr + ceil) // 2
            sqr = mid * mid
            if sqr > num:
                ceil = mid - 1
            elif sqr < num:
                flr = mid + 1
            else:
                return True
        return False

s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(14))