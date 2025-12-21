# 955. Delete Columns to Make Sorted II
# You are given an array of n strings strs, all of the same length.
# We may choose any deletion indices, and we delete all the characters in those indices for each string.
# For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].
# Suppose we chose a set of deletion indices answer such that after deletions, the final array has its elements in lexicographic order (i.e., strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]). Return the minimum possible value of answer.length.

from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        count = 0
        col = 0
        cache = [""] * m
        while col < n:
            is_ordered = True
            has_repeat = False
            row = 0
            while row < m - 1 and is_ordered:
                curr = cache[row] + strs[row][col]
                nxt = cache[row + 1] + strs[row + 1][col]
                if curr > nxt:
                    count += 1
                    is_ordered = False
                elif curr == nxt:
                    has_repeat = True
                row += 1
            if is_ordered:
                if has_repeat:
                    for row in range(m):
                        cache[row] += strs[row][col]
                else:
                    break
            col += 1
        return count

s = Solution()
print(s.minDeletionSize(["xxga", "xxfb", "yxfa"]))