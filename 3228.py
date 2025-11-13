# 3228. Maximum Number of Operations to Move Ones to the End
# You are given a binary string s.
# You can perform the following operation on the string any number of times:
# Choose any index i from the string where i + 1 < s.length such that s[i] == '1' and s[i + 1] == '0'.
# Move the character s[i] to the right until it reaches the end of the string or another '1'. For example, for s = "010010", if we choose i = 1, the resulting string will be s = "000110".
# Return the maximum number of operations that you can perform.

class Solution:
    def maxOperations(self, s: str) -> int:
        count = 0
        ones = 0
        zero = False
        s += "1"
        for bit in s:
            if bit == "1":
                if zero:
                    count += ones
                    zero = False
                ones += 1
            else:
                zero = True
        return count

s = Solution()
print(s.maxOperations("1001101"))
print(s.maxOperations("10011010"))