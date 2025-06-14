# 2566. Maximum Difference by Remapping a Digit
# You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.
# Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.
# Notes:
    # When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
    # Bob can remap a digit to itself, in which case num does not change.
    # Bob can remap different digits for obtaining minimum and maximum values respectively.
    # The resulting number after remapping can contain leading zeroes.

class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_list = list(str(num))
        max_num = num_list.copy()
        min_num = num_list.copy()
        max_swap = None
        min_swap = min_num[0]
        for n in max_num:
            if n != "9":
                max_swap = n
                break
        for i in range(len(num_list)):
            if max_num[i] == max_swap:
                max_num[i] = "9"
            if min_num[i] == min_swap:
                min_num[i] = "0"
        return int("".join(max_num)) - int("".join(min_num))

s = Solution()
print(s.minMaxDifference(100))
print(s.minMaxDifference(999))