# 1759. Count Number of Homogenous Substrings
# Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.
# A string is homogenous if all the characters of the string are the same.
# A substring is a contiguous sequence of characters within a string.

class Solution:
    def countHomogenous(self, s: str) -> int:
        output = sub_ct = sub_len = 0
        curr_char = ''
        for char in s:
            if char == curr_char:
                sub_len += 1
                sub_ct += sub_len
            else:
                output += sub_ct
                curr_char = char
                sub_len = 1
                sub_ct = 1
        output += sub_ct
        return output % (10 ** 9 + 7)

s = Solution()
print(s.countHomogenous("abbcccaa"))
print(s.countHomogenous("xy"))
print(s.countHomogenous("zzzzz"))
print(s.countHomogenous("a"))