# 1399. Count Largest Group
# You are given an integer n.
# Each number from 1 to n is grouped according to the sum of its digits.
# Return the number of groups that have the largest size.

class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}
        max_size = 0
        for i in range(1, n + 1):
            str_i = str(i)
            sum_digits = 0
            for digit in str_i:
                sum_digits += int(digit)
            if sum_digits in groups:
                groups[sum_digits] += 1
            else:
                groups[sum_digits] = 1
            max_size = max(max_size, groups[sum_digits])
        count = 0
        for sum_digits in groups:
            if groups[sum_digits] == max_size:
                count += 1
        return count

s = Solution()
print(s.countLargestGroup(13))
print(s.countLargestGroup(2))