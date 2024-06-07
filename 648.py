# 648. Replace Words
# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".
# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.
# Return the sentence after the replacement.

from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ref = set(dictionary)
        exp = {}
        words = sentence.split(" ")
        for i in range(len(words)):
            word = words[i]
            if word in exp:
                words[i] = exp[word]
                continue
            prefix = ""
            for j in range(len(word)):
                prefix += word[j]
                if prefix in ref:
                    words[i] = prefix
                    break
            exp[word] = prefix
        return " ".join(words)

s = Solution()
print(s.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
print(s.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))