# 76. Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_d = {}
        for char in t:
            if char in t_d:
                t_d[char] += 1
            else:
                t_d[char] = 1
        criteria = len(t_d)
        i = j = matches = 0
        s_d = {}
        while j < len(s) and matches != criteria:
            char = s[j]
            if char in s_d:
                s_d[char] += 1
            else:
                s_d[char] = 1
            if char in t_d and t_d[char] == s_d[char]:
                matches += 1
            j += 1
        if j == len(s) and matches < criteria:
            return ""
        while s[i] not in t_d or s_d[s[i]] > t_d[s[i]]:
            s_d[s[i]] -= 1
            i += 1
        min_len = j - i
        min_substr = s[i:j]
        while j < len(s):
            if s[j] in s_d:
                s_d[s[j]] += 1
            else:
                s_d[s[j]] = 1
            j += 1
            while s[i] not in t_d or s_d[s[i]] > t_d[s[i]]:
                s_d[s[i]] -= 1
                i += 1
            length = j - i
            if length < min_len:
                min_len = length
                min_substr = s[i:j]
        return min_substr

s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("a", "a"))
print(s.minWindow("a", "aa"))