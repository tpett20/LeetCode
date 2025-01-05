# 2381. Shifting Letters II
# You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.
# Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').
# Return the final string after all such shifts to s are applied.

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff_arr = [0] * len(s)
        for shift in shifts:
            start, end, direction = shift
            change = -1 if direction == 0 else direction
            diff_arr[start] += change
            if end < len(s) - 1:
                diff_arr[end + 1] -= change
        output = []
        prefix_sum = 0
        for i in range(len(s)):
            char = s[i]
            code = ord(char)
            prefix_sum += diff_arr[i]
            shift = prefix_sum
            positive = (shift >= 1)
            shift = abs(shift) % 26
            shift = shift if positive else -shift
            code += shift
            if code > 122:
                code = 97 + (code - 1 - 122)
            elif code < 97:
                code = 122 - (97 - code - 1)
            output.append(chr(code))
        return "".join(output)

s = Solution()
print(s.shiftingLetters("abc", [[0,1,0], [1,2,1], [0,2,1]]))
print(s.shiftingLetters("za", [[0,0,1], [1,1,0]]))