# 1422. Maximum Score After Splitting a String
# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

class Solution:
    def maxScore(self, s: str) -> int:
        l_zeros = l_ones = 0
        for bit in s:
            if bit == "1":
                l_ones += 1
            else:
                l_zeros += 1
        r_zeros = r_ones = max_score = 0
        for i in range(len(s) - 1, 0, -1):
            bit = s[i]
            if bit == "1":
                l_ones -= 1
                r_ones += 1
            else: 
                l_zeros -= 1
                r_zeros += 1
            max_score = max(l_zeros + r_ones, max_score)
        return max_score
            
s = Solution()
print(s.maxScore("011101"))
print(s.maxScore("00111"))
print(s.maxScore("11110"))