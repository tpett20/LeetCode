# 2451. Odd String Difference
# You are given an array of equal-length strings words. Assume that the length of each string is n.
# Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.
# For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
# All the strings in words have the same difference integer array, except one. You should find that string.
# Return the string in words that has different difference integer array.

class Solution:
    def oddString(self, words: list[str]) -> str:
        def get_diffs(s):
            output = []
            for i in range(1, len(s)):
                code1 = ord(s[i - 1])
                code2 = ord(s[i])
                output.append(code2 - code1)
            return tuple(output)
        
        opt1 = get_diffs(words[0])
        opt2 = get_diffs(words[1])
        for i in range(2, len(words)):
            key = get_diffs(words[i])
            if key == opt1 == opt2:
                continue
            elif key != opt1 and key != opt2:
                return words[i]
            elif key == opt1:
                return words[1]
            elif key == opt2:
                return words[0]

s = Solution()
print(s.oddString(["adc","wzy","abc"]))
print(s.oddString(["aaa","bob","ccc","ddd"]))