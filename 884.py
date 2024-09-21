# 884. Uncommon Words from Two Sentences
# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        def get_word_count(string):
            words = string.split(" ")
            counter = {}
            for word in words:
                counter[word] = counter.get(word, 0) + 1
            return counter
        
        def pull_uncommon_words(d1, d2):
            output = []
            for word in d1:
                if word not in d2 and d1[word] == 1:
                    output.append(word)
            return output
        
        word_count1 = get_word_count(s1)
        word_count2 = get_word_count(s2)
        uncommon1 = pull_uncommon_words(word_count1, word_count2)
        uncommon2 = pull_uncommon_words(word_count2, word_count1)
        return uncommon1 + uncommon2

s = Solution()
print(s.uncommonFromSentences("lets go mets", "lets go knicks"))