# 2578. Split With Minimum Sum
# Given a positive integer num, split it into two non-negative integers num1 and num2 such that:
# - The concatenation of num1 and num2 is a permutation of num.
#   - In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num.
# - num1 and num2 can contain leading zeros.
# Return the minimum possible sum of num1 and num2.
# Notes:
# - It is guaranteed that num does not contain any leading zeros.
# - The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.

class Solution:
    def splitNum(self, num: int) -> int:
        s = list(str(num))
        s.sort()
        num1 = ''
        num2 = ''
        for i, num in enumerate(s):
            if i % 2 == 0:
                num1 += num
            else:
                num2 += num
        return int(num1) + int(num2)

s = Solution()
print(s.splitNum(2578))
print(s.splitNum(4325))
print(s.splitNum(687))
print(s.splitNum(123456))
print(s.splitNum(629834627))