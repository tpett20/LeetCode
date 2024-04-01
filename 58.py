# 58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == " ":
            i -= 1
        j = i
        while i >= 0 and s[i] != " ":
            i -= 1
        return j - i

s = Solution()
print(s.lengthOfLastWord("   fly me   to   the moon  "))