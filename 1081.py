# 1081. Smallest Subsequence of Distinct Characters
# Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

from typing import Set

class Solution:
    def find_next_char_idx(self, s: str, start_idx: int, used_chars: Set[str]) -> str:
        n = len(s)
        unique_chars = set(s)
        for used_char in used_chars:
            unique_chars.remove(used_char)
        seen = set()
        i = n - 1
        while i >= start_idx and len(seen) < len(unique_chars):
            char = s[i]
            if char not in used_chars:
                seen.add(char)
            i -= 1
        i += 1
        small_char = "~"
        small_idx = i + 1
        while i >= start_idx:
            char = s[i]
            if char <= small_char and char not in used_chars:
                small_char = char
                small_idx = i
            i -= 1
        return small_idx

    def smallestSubsequence(self, s: str) -> str:
        used = set()
        unique_chars = set(s)
        smallest_subseq = ""
        start_idx = 0
        while len(smallest_subseq) < len(unique_chars):
            i = self.find_next_char_idx(s, start_idx, used)
            smallest_subseq += s[i]
            used.add(s[i])
            start_idx = i + 1
        return smallest_subseq

s = Solution()
print(s.smallestSubsequence("cbacdcbc"))