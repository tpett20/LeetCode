# 1897. Redistribute Characters to Make All Strings Equal
# You are given an array of strings words (0-indexed).
# In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].
# Return true if you can make every string in words equal using any number of operations, and false otherwise.

class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        map = {}
        for word in words:
            for char in word:
                if char in map:
                    map[char] += 1
                else:
                    map[char] = 1
        for char in map:
            if map[char] % len(words) != 0:
                return False
        return True

s = Solution()
print(s.makeEqual(["abc", "aabc", "bc"]))
print(s.makeEqual(["ab", "a"]))