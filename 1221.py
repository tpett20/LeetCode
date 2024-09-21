# 1221. Split a String in Balanced Strings
# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it into some number of substrings such that:
    # Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = l = 0
        count = 0
        for char in s:
            if char == "R":
                r += 1
            else:
                l += 1
            if l == r:
                count += 1
        return count

s = Solution()
print(s.balancedStringSplit("RLRRLLRLRL"))
print(s.balancedStringSplit("RLRRRLLRLL"))