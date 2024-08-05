# 2053. Kth Distinct String in an Array
# A distinct string is a string that is present only once in an array.
# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".
# Note that the strings are considered in the order in which they appear in the array.

from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        for string in arr:
            if string in freq:
                freq[string] += 1
            else:
                freq[string] = 1
        i = 0
        for string in freq:
            if freq[string] == 1:
                i += 1
                if i == k:
                    return string
        return ""

s = Solution()
print(s.kthDistinct(["d","b","c","b","c","a"], 2))