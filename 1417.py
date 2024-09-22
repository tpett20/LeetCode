# 1417. Reformat The String
# You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
# You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.
# Return the reformatted string or return an empty string if it is impossible to reformat the string.

class Solution:
    def reformat(self, s: str) -> str:
        nums = ""
        ltrs = ""
        for char in s:
            if 48 <= ord(char) <= 57:
                nums += char
            else:
                ltrs += char
        if abs(len(nums) - len(ltrs)) >= 2:
            return ""
        output = ""
        long_str = nums if len(nums) > len(ltrs) else ltrs
        short_str = ltrs if len(nums) > len(ltrs) else nums
        total_len = len(nums) + len(ltrs)
        for i in range(total_len):
            if i % 2 == 0:
                output += long_str[i // 2]
            else:
                output += short_str[i // 2]
        return output

s = Solution()
print(s.reformat("1969mets"))