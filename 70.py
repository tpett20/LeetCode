# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        ways = [1, 2]
        for _ in range(n - 2):
            next = ways[0] + ways[1]
            ways[0] = ways[1]
            ways[1] = next
        return ways[1]

s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(10))