# 1592. Rearrange Spaces Between Words
# You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.
# Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.
# Return the string after rearranging the spaces.

class Solution:
    def reorderSpaces(self, text: str) -> str:
        word = ""
        words = []
        spaces = 0
        for char in text:
            if char == " ":
                if word:
                    words.append(word)
                word = ""
                spaces += 1
            else:
                word += char
        if word:
            words.append(word)
        if spaces == 0:
            return text
        if len(words) == 1:
            return words[0] + " " * spaces
        per_word = spaces // (len(words) - 1)
        extra = spaces % (len(words) - 1)
        output = ""
        for i in range(len(words) - 1):
            output += words[i] + " " * per_word
        return output + words[-1] + " " * extra

s = Solution()
print(s.reorderSpaces("  this   is  a sentence "))
print(s.reorderSpaces(" practice   makes   perfect"))