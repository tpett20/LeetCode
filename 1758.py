# 1758. Minimum Changes To Make Alternating Binary String
# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.
# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.
# Return the minimum number of operations needed to make s alternating.

class Solution:
    def minOperations(self, s: str) -> int:
        flip = "1"
        ops_0_start = ops_1_start = 0
        for bit in s:
            if flip == "0":
                flip = "1"
            else:
                flip = "0"
            if bit != flip:
                ops_0_start += 1
            else:
                ops_1_start += 1
        return min(ops_0_start, ops_1_start)

s = Solution()
print(s.minOperations("0100"))
print(s.minOperations("10"))
print(s.minOperations("1111"))
print(s.minOperations("010001010101"))