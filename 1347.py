# 1347. Minimum Number of Steps to Make Two Strings Anagram
# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
# Return the minimum number of steps to make t an anagram of s.
# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_map = {}
        for char in s:
            if char in s_map:
                s_map[char] += 1
            else:
                s_map[char] = 1
        steps = 0
        for char in t:
            if char in s_map and s_map[char]:
                s_map[char] -= 1
            else:
                steps += 1
        return steps
        
s = Solution()
print(s.minSteps("bab", "aba"))
print(s.minSteps("leetcode", "practice"))