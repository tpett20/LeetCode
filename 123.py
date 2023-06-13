# Best Time to Buy and Sell Stock III
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

def maxProfit(prices):
    profit1 = 0
    profit2 = 0
    low = prices[0]
    consecutive = True
    for i in range(1, len(prices)):
        if prices[i] < low:
            low = prices[i]
            consecutive = False
        elif prices[i] - low > profit1 and profit1 <= profit2:
            if consecutive:
                profit1 += prices[i] - low
                low = prices[i]
            else: 
                profit1 = prices[i] - low
                low = prices[i]
                consecutive = True
        elif prices[i] - low > profit2:
            if consecutive:
                profit2 += prices[i] - low
                low = prices[i]
            else: 
                profit2 = prices[i] - low
                low = prices[i]
                consecutive = True
        print('p[i]:', prices[i], 'p1:', profit1, 'p2:', profit2, 'low:', low, consecutive)
    return profit1 + profit2

print(maxProfit([1,2,3,4,5]))