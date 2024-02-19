# 2485. Find the Pivot Integer
# Given a positive integer n, find the pivot integer x such that:
    # The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

class Solution:
    def pivotInteger(self, n: int) -> int:
        front_sum = (n + 1) / 2 * n
        back_sum = i = n
        while front_sum > back_sum:
            front_sum -= i
            back_sum += (i - 1)
            i -= 1
        return i if front_sum == back_sum else -1

s = Solution()
print(s.pivotInteger(8))
print(s.pivotInteger(1))
print(s.pivotInteger(4))