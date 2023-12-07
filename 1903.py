# 1903. Largest Odd Number in String
# You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
# A substring is a contiguous sequence of characters within a string.

class Solution:
    def largestOddNumber(self, num: str) -> str:
        even_set = {"0", "2", "4", "6", "8"}
        last_odd = len(num) - 1
        while last_odd >= 0 and num[last_odd] in even_set:
            last_odd -= 1
        return num[:last_odd + 1]

s = Solution()
print(s.largestOddNumber("52"))
print(s.largestOddNumber("4206"))
print(s.largestOddNumber("3542722"))