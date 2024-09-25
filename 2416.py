# 2416. Sum of Prefix Scores of Strings
# You are given an array words of size n consisting of non-empty strings.
# We define the score of a string term as the number of strings words[i] such that term is a prefix of words[i].
    # For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
# Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].
# Note that a string is considered as a prefix of itself.

from typing import List

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        cache = {}
        for word in words:
            curr = cache
            for char in word:
                if char in curr:
                    curr[char]["#"] += 1
                else:
                    curr[char] = { "#": 1 }
                curr = curr[char]
        output = []
        for word in words:
            count = 0
            curr = cache
            for char in word:
                count += curr[char]["#"]
                curr = curr[char]
            output.append(count)
        return output

s = Solution()
print(s.sumPrefixScores(["abc", "ab", "bc", "b"]))
print(s.sumPrefixScores(["abcd"]))