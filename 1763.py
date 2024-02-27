# 1763. Longest Nice Substring
# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.
# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def checkIfNice(string):
            d = {}
            for char in string:
                key = char.lower()
                if key in d:
                    if char.isupper():
                        d[key][1] = True
                    else:
                        d[key][0] = True
                else:
                    if char.isupper():
                        d[key] = [False, True]
                    else:
                        d[key] = [True, False]
            for key in d:
                if d[key] == [False, True] or d[key] == [True, False]:
                    return False
            return True
        
        max_substr = ""
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                substr = s[i:j+1]
                if len(substr) > len(max_substr) and checkIfNice(substr):
                    max_substr = substr
        return max_substr

sol = Solution()
print(sol.longestNiceSubstring("YazaAay"))
print(sol.longestNiceSubstring("Bb"))
print(sol.longestNiceSubstring("c"))