# 2264. Largest 3-Same-Digit Number in String
# You are given a string num representing a large integer. An integer is good if it meets the following conditions:
    # It is a substring of num with length 3.
    # It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.
# Note:
    # A substring is a contiguous sequence of characters within a string.
    # There may be leading zeroes in num or a good integer.

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_int = 0
        max_int_str = ""
        for i in range(len(num) - 2):
            sub_str = num[i:i+3]
            if sub_str[0] == sub_str[1] == sub_str[2]:
                sub_int = int(sub_str)
                if sub_int >= max_int:
                    max_int = sub_int
                    max_int_str = sub_str
        return max_int_str
    
s = Solution()
print(s.largestGoodInteger("6777133339"))
print(s.largestGoodInteger("2300019"))