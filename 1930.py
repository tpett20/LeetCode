# 1930. Unique Length-3 Palindromic Subsequences
# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
# A palindrome is a string that reads the same forwards and backwards.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        pairs = {}
        for i in range(len(s)):
            char = s[i]
            if char in pairs:
                pairs[char][1] = i
            else:
                pairs[char] = [i, -1]
        count = 0
        for char in pairs:
            start, end = pairs[char]
            seen = set()
            for i in range(start + 1, end):
                seen.add(s[i])
                if len(seen) == 26:
                    break
            count += len(seen)
        return count

s = Solution()
print(s.countPalindromicSubsequence("aabca"))
print(s.countPalindromicSubsequence("a" * 100))