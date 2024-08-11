# 728. Self Dividing Numbers
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check_self_div(num):
            str_num = str(num)
            for digit in str_num:
                digit = int(digit)
                if digit == 0 or num % digit != 0:
                    return False
            return True
        
        output = []
        for num in range(left, right + 1):
            if check_self_div(num) is True:
                output.append(num)
        return output

s = Solution()
print(s.selfDividingNumbers(19, 86))
print(s.selfDividingNumbers(9000, 10000))