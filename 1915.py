# 1915. Number of Wonderful Substrings - INCOMPLETE, TIME LIMIT EXCEEDED
# A wonderful string is a string where at most one letter appears an odd number of times.
    # For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
# Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.
# A substring is a contiguous sequence of characters in a string.

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = 0
        for i in range(len(word)):
            s = set()
            for j in range(i, len(word)):
                ltr = word[j]
                if ltr in s:
                    s.remove(ltr)
                else:
                    s.add(word[j])
                if len(s) <= 1:
                    count += 1
        return count

s = Solution()
print(s.wonderfulSubstrings("aabb"))