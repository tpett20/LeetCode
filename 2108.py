# 2108. Find First Palindromic String in the Array
# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        def check_pal(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        for word in words:
            if check_pal(word):
                return word
        return ""

s = Solution()
print(s.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]))