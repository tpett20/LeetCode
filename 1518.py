# 1518. Water Bottles
# There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.
# The operation of drinking a full water bottle turns it into an empty bottle.
# Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = empty = 0
        while (numBottles + empty) >= numExchange:
            count += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty %= numExchange
        return count + numBottles

s = Solution()
print(s.numWaterBottles(9, 3))
print(s.numWaterBottles(15, 4))