# 1967. Number of Strings That Appear as Substrings in Word
# Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.
# A substring is a contiguous sequence of characters within a string.

from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        checked = {}
        for pattern in patterns:
            if pattern in checked:
                if checked[pattern] == 1:
                    count += 1
            else:
                if pattern in word:
                    count += 1
                    checked[pattern] = 1
                else:
                    checked[pattern] = 0
        return count

s = Solution()
print(s.numOfStrings(["a","abc","bc","d"], "abc"))
print(s.numOfStrings(["a","b","c"], "aaaaabbbbb"))
print(s.numOfStrings(["a","a","a"], "ab"))