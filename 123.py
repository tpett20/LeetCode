# 123. Best Time to Buy and Sell Stock III
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

def maxProfit(prices):
    print(prices)
    profit1 = profit2 = 0
    biggestProfit = 0
    def getMaxDiff(idx1, idx2):
        low = prices[idx1]
        profit = 0
        for i in range(idx1 + 1, idx2):
            difference = prices[i] - low
            if difference < 0:
                low = prices[i]
            elif difference > profit:
                profit = difference
        return profit
    i = 0
    last = len(prices) - 1
    while i < last and prices[i] >= prices[i + 1]: i += 1
    if i == last: return 0
    low = prices[i]
    lowest = prices[i]
    high = prices[i]
    while prices[last] < prices[last - 1]: last -= 1
    while i < last:
        if prices[i] > lowest: 
            profit1 = prices[i] - lowest
            profit2 = getMaxDiff(i, last + 1)
            profit = profit1 + profit2
            print('lowest', profit1, profit2, '=', profit)
            if profit > biggestProfit: 
                biggestProfit = profit
        elif prices[i] >= high:
            profit1 = prices[i] - low
            profit2 = getMaxDiff(i, last + 1)
            profit = profit1 + profit2
            print('low', profit1, profit2, '=', profit)
            if profit > biggestProfit: 
                biggestProfit = profit
            high = prices[i]
        elif prices[i] < lowest:
            print('hit', prices[i])
            lowest = prices[i]
        i += 1
    return biggestProfit

print(maxProfit([3,3,5,0,0,3,1,4]), 'Expected = 6')
print(maxProfit([1,2,3,4,5]), 'Expected = 4')
print(maxProfit([7,6,4,3,1]), 'Expected = 0')
print(maxProfit([1,2,4,2,5,7,2,4,9,0]), 'Expected = 13')
print(maxProfit([2,4,9,1,2,4,2,5,7,2,4,9,0]), 'Expected = 15')
print(maxProfit([2,4,9,1,2,4,2,5,7,0]), 'Expected = 13')
print(maxProfit([2,1,4,5,2,9,7]), 'Expected = 11')
print(maxProfit([14,9,10,12,4,8,1,16]), 'Expected = 19')
print(maxProfit([8,6,4,3,3,2,3,5,8,3,8,2,6]), 'Expected = 11')
print(maxProfit([5,2,3,0,3,5,6,8,1,5]), 'Expected = 12')