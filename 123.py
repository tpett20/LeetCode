# Best Time to Buy and Sell Stock III
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

def maxProfit(prices):
    profit1 = 0
    profit2 = 0
    low = prices[0]
    consecutive1 = consecutive2 = False
    for i in range(1, len(prices)):
        difference = prices[i] - low
        if difference < 0:
            low = prices[i]
            consecutive1 = consecutive2 = False
        elif difference > 0 and (consecutive1 or consecutive2):
            if consecutive1:
                profit1 += difference
                low = prices[i]
            elif consecutive2:
                profit2 += difference
                low = prices[i]
        elif difference > profit1 and profit1 <= profit2:
            profit1 = difference
            low = prices[i]
            consecutive1 = True
        elif difference > profit2:
            profit2 = difference
            low = prices[i]
            consecutive2 = True
        print('p[i]:', prices[i], 'p1:', profit1, 'p2:', profit2, 'low:', low, consecutive1, consecutive2)
    return profit1 + profit2

print(maxProfit([1,2,4,2,5,7,2,4,9,0]), 'Expected = 13')