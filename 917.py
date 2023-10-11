# 917. Reverse Only Letters
# Given a string s, reverse the string according to the following rules:
# - All the characters that are not English letters remain in the same position.
# - All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ltrs = ''
        for char in s:
            if char.isalpha():
                ltrs = char + ltrs
        output = ''
        i = 0
        for char in s:
            if char.isalpha():
                output += ltrs[i]
                i += 1
            else:
                output += char
        return output

s = Solution()
print(s.reverseOnlyLetters("ab-cd"))
print(s.reverseOnlyLetters("a-bC-dEf-ghIj"))
print(s.reverseOnlyLetters("Let's-Go-Mets!"))