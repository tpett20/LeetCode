# 2706. Buy Two Chocolates
# You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.
# You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.
# Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.

class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        low = prices[0]
        sec_low = float('inf')
        for i in range(1, len(prices)):
            if prices[i] < low:
                sec_low = low
                low = prices[i]
            elif prices[i] < sec_low:
                sec_low = prices[i]
            if sec_low == 1:
                return money - 2
        leftover = money - (low + sec_low)
        return leftover if leftover >= 0 else money

s = Solution()
print(s.buyChoco([1,2,2], 3))
print(s.buyChoco([3,2,3], 3))