# 1456. Maximum Number of Vowels in a Substring of Given Length
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        v_count = i = 0
        while i < k:
            if s[i] in vowels:
                v_count += 1
            i += 1
        max_vowels = v_count
        for j in range(i, len(s)):
            if s[j] in vowels:
                v_count += 1
            if s[j - k] in vowels:
                v_count -= 1
            max_vowels = max(v_count, max_vowels)
        return max_vowels

s = Solution()
print(s.maxVowels("abciiidef", 3))
print(s.maxVowels("aeiou", 2))
print(s.maxVowels("leetcode", 3))