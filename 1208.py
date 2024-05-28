# 1208. Get Equal Substrings Within Budget
# You are given two strings s and t of the same length and an integer maxCost.
# You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).
# Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = j = cost = max_len = 0
        while j < len(s):
            cost += abs(ord(t[j]) - ord(s[j]))
            while i < j and cost > maxCost:
                cost -= abs(ord(t[i]) - ord(s[i]))
                i += 1
            length = j - i + 1
            if length > max_len and cost <= maxCost:
                max_len = length
            j += 1
        return max_len

s = Solution()
print(s.equalSubstring("abcd", "bcdf", 3))
print(s.equalSubstring("abcd", "cdef", 3))
print(s.equalSubstring("abcd", "acde", 0))
print(s.equalSubstring("krrgw", "zjxss", 19))