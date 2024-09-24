# 3043. Find the Length of the Longest Common Prefix
# You are given two arrays with positive integers arr1 and arr2.
# A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. For example, 123 is a prefix of the integer 12345, while 234 is not.
# A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b. For example, 5655359 and 56554 have a common prefix 565 while 1223 and 43456 do not have a common prefix.
# You need to find the length of the longest common prefix between all pairs of integers (x, y) such that x belongs to arr1 and y belongs to arr2.
# Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.

from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        cache = {}
        long_arr = arr1 if len(arr1) < len(arr2) else arr2
        short_arr = arr2 if len(arr1) < len(arr2) else arr1
        for num in short_arr:
            num_str = str(num)
            curr = cache
            for digit in num_str:
                if digit not in curr:
                    curr[digit] = {}
                curr = curr[digit]
        max_len = 0
        for num in long_arr:
            num_str = str(num)
            curr = cache
            i = 0
            while i < len(num_str) and num_str[i] in curr:
                curr = curr[num_str[i]]
                i += 1
            max_len = max(i, max_len)
        return max_len

s = Solution()
print(s.longestCommonPrefix([1, 10, 100], [1000]))
print(s.longestCommonPrefix([37, 14, 41, 31, 1969, 1986], [19, 41, 3112, 198]))