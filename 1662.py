# 1662. Check If Two String Arrays are Equivalent
# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        i1 = j1 = 0
        i2 = j2 = 0
        while i1 < len(word1) and i2 < len(word2):
            char1 = word1[i1][j1]
            char2 = word2[i2][j2]
            if char1 == char2:
                j1 += 1
                j2 += 1
            else:
                return False
            if j1 == len(word1[i1]):
                i1 += 1
                j1 = 0
            if j2 == len(word2[i2]):
                i2 += 1
                j2 = 0
        if i1 != len(word1) or i2 != len(word2):
            return False
        return True

s = Solution()
print(s.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
print(s.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))

# Alternate One Line Solution:
# def arrayStringsAreEqual(word1, word2):
#     return "".join(word1) == "".join(word2)