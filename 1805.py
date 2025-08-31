# 1805. Number of Different Integers in a String
# You are given a string word that consists of digits and lowercase English letters.
# You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34". Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".
# Return the number of different integers after performing the replacement operations on word.
# Two integers are considered different if their decimal representations without any leading zeros are different.

class Solution:
    def remove_lead_zeros(self, word: str) -> str:
        if len(word) == 1:
            return word
        i = 0
        while i < len(word) - 1 and word[i] == "0":
            i += 1
        return word[i:]

    def numDifferentIntegers(self, word: str) -> int:
        int_strs = set()
        word += "a"
        curr = ""
        for char in word:
            if char.isnumeric():
                curr += char
            elif curr:
                cleaned_str = self.remove_lead_zeros(curr)
                int_strs.add(cleaned_str)
                curr = ""
        return len(int_strs)

s = Solution()
print(s.numDifferentIntegers("00a1b01c001d100"))