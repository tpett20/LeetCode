# 763. Partition Labels
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        output = []
        last_idxs = [-1] * 26
        for idx, char in enumerate(s):
            code = ord(char) - 97
            last_idxs[code] = idx
        count = 0
        next_split = -1
        for idx, char in enumerate(s):
            count += 1
            code = ord(char) - 97
            last_idx = last_idxs[code]
            next_split = max(last_idx, next_split)
            if idx == next_split:
                output.append(count)
                count = 0
        return output

s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
print(s.partitionLabels("abcdefghijklmnopqrstuvwxyz"))
print(s.partitionLabels("abcdefghijklmnopqrstuvwxyza"))