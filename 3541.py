# 3541. Find Most Frequent Vowel and Consonant
# You are given a string s consisting of lowercase English letters ('a' to 'z').
# Your task is to:
    # Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
    # Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.
# Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.
# The frequency of a letter x is the number of times it occurs in the string.

class Solution:
    def maxFreqSum(self, s: str) -> int:
        max_vowel_count = max_cons_count = 0
        vowels = set(list("aeiou"))
        freq_map = {}
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1
        for char in freq_map:
            freq = freq_map[char]
            if char in vowels and freq > max_vowel_count:
                max_vowel_count = freq
            elif char not in vowels and freq > max_cons_count:
                max_cons_count = freq
        return max_vowel_count + max_cons_count

s = Solution()
print(s.maxFreqSum("letsgomets"))