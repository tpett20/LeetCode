# 1446. Consecutive Characters
# The power of the string is the maximum length of a non-empty substring that contains only one unique character.
# Given a string s, return the power of s.

class Solution:
    def maxPower(self, s: str) -> int:
        curr_len = max_len = 1
        curr_char = s[0]
        for i in range(1, len(s)):
            if s[i] == curr_char:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1
                curr_char = s[i]
        return max_len

s = Solution()
print(s.maxPower("leetcode"))
print(s.maxPower("abbcccddddeeeeedcba"))