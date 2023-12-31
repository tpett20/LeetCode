# 1624. Largest Substring Between Two Equal Characters
# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.
# A substring is a contiguous sequence of characters within a string.

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        map = {}
        max_len = -1
        for idx, char in enumerate(s):
            if char in map:
                max_len = max(idx - map[char], max_len)
            else:
                map[char] = idx + 1
        return max_len

s = Solution()
print(s.maxLengthBetweenEqualCharacters("aa"))
print(s.maxLengthBetweenEqualCharacters("abca"))
print(s.maxLengthBetweenEqualCharacters("cbzxy"))