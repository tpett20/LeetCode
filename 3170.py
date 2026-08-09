# 3170. Lexicographically Minimum String After Removing Stars
# You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.
# While there is a '*', do the following operation:
# Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
# Return the lexicographically smallest resulting string after removing all '*' characters.

from typing import List

class Solution:
    def get_smallest_remaining_alpha_idx(self, map: List[int]) -> int:
        for idx in range(26):
            if map[idx]:
                return idx
        return 27

    def clearStars(self, s: str) -> str:
        chars = list(s)
        idx_map = []
        for _ in range(26):
            idx_map.append([])
        smallest_alpha_idx = 27
        for idx, char in enumerate(s):
            if char == "*":
                chars[idx] = "_"
                smallest_letter_idx = idx_map[smallest_alpha_idx].pop()
                chars[smallest_letter_idx] = "_"
                if not idx_map[smallest_alpha_idx]:
                    smallest_alpha_idx = self.get_smallest_remaining_alpha_idx(idx_map)
            else:
                alpha_idx = ord(char) - 97
                idx_map[alpha_idx].append(idx)
                smallest_alpha_idx = min(alpha_idx, smallest_alpha_idx)
        return "".join(c for c in chars if c != "_")