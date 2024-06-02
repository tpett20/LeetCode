# 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

s = Solution()

test_case1 = ["h","e","l","l","o"]
print("Input:", test_case1)
s.reverseString(test_case1)
print("Output:", test_case1)

test_case2 = ["M","e","t","s"]
print("Input:", test_case2)
s.reverseString(test_case2)
print("Output:", test_case2)