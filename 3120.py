# 3120. Count the Number of Special Characters I
# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
# Return the number of special letters in word.

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_set = set()
        upper_set = set()
        both_set = set()
        for ltr in word:
            if ltr.isupper():
                upper_set.add(ltr)
                if ltr.lower() in lower_set:
                    both_set.add(ltr.lower())
            else:
                lower_set.add(ltr)
                if ltr.upper() in upper_set:
                    both_set.add(ltr)
        return len(both_set)

s = Solution()
print(s.numberOfSpecialChars("aaAbcBC"))
print(s.numberOfSpecialChars("abc"))
print(s.numberOfSpecialChars("abBCab"))