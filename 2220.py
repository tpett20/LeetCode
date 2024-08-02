# 2220. Minimum Bit Flips to Convert Number
# A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.
    # For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
# Given two integers start and goal, return the minimum number of bit flips to convert start to goal.

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bin_start = format(start, 'b')
        bin_goal = format(goal, 'b')
        diff = abs(len(bin_start) - len(bin_goal))
        if len(bin_goal) < len(bin_start):
            bin_goal = '0' * diff + bin_goal
        else:
            bin_start = '0' * diff + bin_start
        count = 0
        for i in range(len(bin_start)):
            if bin_start[i] != bin_goal[i]:
                count += 1
        return count
    
s = Solution()
print(s.minBitFlips(10, 7))
print(s.minBitFlips(3, 4))