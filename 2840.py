# 2840. Check if Strings Can be Made Equal With Operations II
# You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.
# You can apply the following operation on any of the two strings any number of times:
    # Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.

from typing import List

class Solution:
    def char_freqs_match(self, d1: dict, d2: dict) -> bool:
        if len(d1) != len(d2):
            return False
        for char in d1:
            freq1 = d1[char]
            freq2 = d2.get(char, 0)
            if freq1 != freq2:
                return False
        return True

    def get_freqs_by_idx_parity(self, string: str) -> List[dict]:
        evens = {}
        odds = {}
        for idx, char in enumerate(string):
            freq_map = evens if idx % 2 == 0 else odds
            freq_map[char] = freq_map.get(char, 0) + 1
        return [evens, odds]

    def checkStrings(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        evens1, odds1 = self.get_freqs_by_idx_parity(s1)
        evens2, odds2 = self.get_freqs_by_idx_parity(s2)
        if not self.char_freqs_match(evens1, evens2):
            return False
        if not self.char_freqs_match(odds1, odds2):
            return False
        return True

s = Solution()
print(s.checkStrings("pixel", "lexip"))
print(s.checkStrings("pixels", "slexip"))
print(s.checkStrings("pixels", "xelspi"))