# 3163. String Compression III
# Given a string word, compress it using the following algorithm:
# Begin with an empty string comp. While word is not empty, use the following operation:
# Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
# Append the length of the prefix followed by c to comp.
# Return the string comp.

class Solution:
    def compressedString(self, word: str) -> str:
        num_str = "0123456789"
        comp = ""
        prev = word[0]
        rep_len = 1
        for i in range(1, len(word)):
            curr = word[i]
            if rep_len == 9 or curr != prev:
                comp += num_str[rep_len] + prev
                rep_len = 1
            else:
                rep_len += 1
            prev = curr
        return comp + num_str[rep_len] + prev

s = Solution()
print(s.compressedString("abcde"))
print(s.compressedString("aaaaaaaaab"))