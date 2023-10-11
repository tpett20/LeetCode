# 387. First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for idx, char in enumerate(s):
            if char in map:
                map[char]['count'] += 1
            else:
                map[char] = {
                    'count': 1,
                    'index': idx
                }
        for key in map:
            if map[key]['count'] == 1:
                return map[key]['index']
        return -1

s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("aabb"))