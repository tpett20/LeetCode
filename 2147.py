# 2147. Number of Ways to Divide a Long Corridor
# Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.
# One room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.
# Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.
# Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7. If there is no way, return 0.

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        count = 1
        l = 0
        r = len(corridor) - 1
        while l < r and corridor[l] == "P":
            l += 1
        while r > l and corridor[r] == "P":
            r -= 1
        if l == r:
            return 0
        seats = 0
        plants = 0
        while l <= r:
            if corridor[l] == "S":
                seats += 1
                if seats == 2:
                    seats = 0
                    count *= (plants + 1)
                    plants = 0
            elif not seats:
                plants += 1
            l += 1
        return count % (10 ** 9 + 7) if not seats else 0

s = Solution()
print(s.numberOfWays("SSPPSPS"))
print(s.numberOfWays("PPP"))