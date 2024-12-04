# 2825. Make String a Subsequence Using Cyclic Increments
# You are given two 0-indexed strings str1 and str2.
# In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.
# Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.
# Note: A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1): 
            return False
        i = j = 0
        while i < len(str1) and j < len(str2):
            curr1 = str1[i]
            curr2 = str2[j]
            code1 = ord(curr1) + 1
            if code1 == 123:
                code1 = 97
            alt_curr1 = chr(code1)
            if curr1 == curr2 or alt_curr1 == curr2:
                j += 1
            i += 1
        return j == len(str2)

s = Solution()
print(s.canMakeSubsequence("abc", "ad"))
print(s.canMakeSubsequence("mets", "nu"))
print(s.canMakeSubsequence("mets", "un"))