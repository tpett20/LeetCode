# 2000. Reverse Prefix of Word
# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
    # For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word
        new_prefix = ""
        for i in range(idx, -1, -1):
            new_prefix += word[i]
        return new_prefix + word[idx + 1:]

s = Solution()
print(s.reversePrefix("abcdefd", "d"))
print(s.reversePrefix("xyxzxe", "z"))
print(s.reversePrefix("abcd", "z"))