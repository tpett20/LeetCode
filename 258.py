# 258. Add Digits
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        string = str(num)
        total = 0
        for digit in string:
            total += int(digit)
        return self.addDigits(total)

s = Solution()
print(s.addDigits(38))
print(s.addDigits(0))