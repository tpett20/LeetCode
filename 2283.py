# 2283. Check if Number Has Equal Digit Count and Digit Value
# You are given a 0-indexed string num of length n consisting of digits.
# Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.

class Solution:
    def digitCount(self, num: str) -> bool:
        freq = {}
        for digit in num:
            digint = int(digit)
            if digint in freq:
                freq[digint] += 1
            else:
                freq[digint] = 1
        for i in range(len(num)):
            frequency = freq.get(i, 0)
            if int(num[i]) != frequency:
                return False
        return True

s = Solution()
print(s.digitCount("1210"))
print(s.digitCount("19691986"))