# 2375. Construct Smallest Number From DI String
# You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.
# A 0-indexed string num of length n + 1 is created using the following conditions:
    # num consists of the digits '1' to '9', where each digit is used at most once.
    # If pattern[i] == 'I', then num[i] < num[i + 1].
    # If pattern[i] == 'D', then num[i] > num[i + 1].
# Return the lexicographically smallest possible string num that meets the conditions.

from typing import List

class Solution:
    def build_num_arr(self, res: List[int], dirs: str, options: List[str]) -> List[int]:
        if len(res) == len(options):
            return res
        d = dirs[len(res) - 1] if res else ""
        if not res:
            opt_range = range(0, len(options))
        elif d == "I":
            opt_range = range(res[-1], len(options))
        else:
            opt_range = range(0, res[-1] - 1)
        for i in opt_range:
            option = options[i]
            if not option:
                continue
            res.append(option)
            options[i] = 0
            num_arr = self.build_num_arr(res, dirs, options)
            if num_arr:
                return num_arr
            res.pop()
            options[i] = option

    def smallestNumber(self, pattern: str) -> str:
        digits = []
        for i in range(1, len(pattern) + 2):
            digits.append(i)
        num_arr = self.build_num_arr([], pattern, digits)
        num = ""
        for n in num_arr:
            num += str(n)
        return num

s = Solution()
print(s.smallestNumber("IIIDIDDD"))
print(s.smallestNumber("DDDD"))