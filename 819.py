# 819. Most Common Word
# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned = set(banned)
        freq = {}
        word = ""
        separators = {" ", "!", "?", "'", ",", ";", "."}
        for i in range(len(paragraph) + 1):
            char = paragraph[i] if i < len(paragraph) else "."
            if char in separators and word:
                if word not in banned:
                    if word in freq:
                        freq[word] += 1
                    else:
                        freq[word] = 1
                word = ""
            elif char not in separators:
                word += char.lower()
        
        max_freq = 0
        max_word = ""
        for word in freq:
            if freq[word] > max_freq:
                max_freq = freq[word]
                max_word = word
        return max_word

s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(s.mostCommonWord("a.", []))