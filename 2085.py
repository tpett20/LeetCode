# 2085. Count Common Words With One Occurrence
# Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

from typing import List

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        d1 = {}
        d2 = {}
        for word in words1:
            if word in d1:
                d1[word] = 2
            else:
                d1[word] = 1
        for word in words2:
            if word in d2:
                d2[word] = 2
            else:
                d2[word] = 1
        for word in d1:
            if d1[word] == 1 and word in d2 and d2[word] == 1:
                count += 1
        return count

s = Solution()
print(s.countWords(["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"]))
print(s.countWords(["b","bb","bbb"], ["a","aa","aaa"]))
print(s.countWords(["a","ab"], ["a","a","a","ab"]))