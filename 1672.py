# 1672. Richest Customer Wealth

# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

def maximumWealth(accounts):
    totals = []
    for account in accounts:
        sum = 0
        for i in range(len(account)):
            sum += account[i]
        totals.append(sum)
    largest = totals[0]
    for i in range(1, len(totals)):
        if totals[i] > largest:
            largest = totals[i]
    return largest

print(maximumWealth([[1,2,3], [3,2,1]]))
print(maximumWealth([[1,5], [7,3], [3,5]]))
print(maximumWealth([[2,8,7], [7,1,3], [1,9,5]]))
print(maximumWealth([[2], [3], []]))
print(maximumWealth([[0], [0]]))
print(maximumWealth([[10]]))