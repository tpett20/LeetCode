# 2255. Count Prefixes of a Given String
# You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.
# Return the number of strings in words that are a prefix of s.
# A prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous sequence of characters within a string.

from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        memory = {}
        for word in words:
            if word in memory:
                count += memory[word]
                continue
            if len(word) > len(s):
                continue
            for i in range(len(word)):
                sub_str = word[:i + 1]
                if word[i] == s[i]:
                    memory[sub_str] = 1
                else:
                    memory[sub_str] = 0
                    break
            count += memory.get(word, 0)
        return count

s = Solution()
print(s.countPrefixes(["a","b","c","ab","bc","abc"], "abc"))
print(s.countPrefixes(["a","a"], "aa"))