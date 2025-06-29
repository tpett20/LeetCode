# 748. Shortest Completing Word
# Given a string licensePlate and an array of strings words, find the shortest completing word in words.
# A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.
# For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".
# Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

from typing import List

class Solution:
    def is_completing_word(self, string: str, target: str) -> bool:
        ref = {}
        for char in string:
            ref[char] = ref.get(char, 0) + 1
        for char in target:
            if ref.get(char, 0):
                ref[char] -= 1
            else:
                return False
        return True

    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        res = " " * 16
        key = ""
        for char in licensePlate.lower():
            if 97 <= ord(char) <= 122:
                key += char
        for word in words:
            if len(word) < len(res) and self.is_completing_word(word, key):
                res = word
        return res

s = Solution()
print(s.shortestCompletingWord("1s3 PSt", ["step","steps","stripe","stepple", "mikepiazza"]))