# 2131. Longest Palindrome by Concatenating Two Letter Words
# You are given an array of strings words. Each element of words consists of two lowercase English letters.
# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.
# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
# A palindrome is a string that reads the same forward and backward.

from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        length = 0
        ref = {}
        extra = False
        for word in words:
            ref[word] = ref.get(word, 0) + 1
        for word in ref:
            freq1 = ref[word]
            opposite = word[1] + word[0]
            if word == opposite:
                if freq1 % 2 == 1:
                    extra = True
                length += (freq1 // 2) * 4
            else:
                freq2 = ref.get(opposite, 0)
                length += min(freq1, freq2) * 2
        return length + 2 if extra else length

s = Solution()
print(s.longestPalindrome(["ab","ba","aa","bb","aa"]))
print(s.longestPalindrome(["cc","cc","cc","cc","cc"]))