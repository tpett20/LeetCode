# 860. Lemonade Change
# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
# Note that you do not have any change in hand at first.
# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 10:
                if cash[5]:
                    cash[5] -= 1
                else:
                    return False
            elif bill == 20:
                if cash[10] and cash[5]:
                    cash[10] -= 1
                    cash[5] -= 1
                elif cash[5] >= 3:
                    cash[5] -= 3
                else:
                    return False
            cash[bill] += 1
        return True

s = Solution()
print(s.lemonadeChange([5,5,5,10,20]))
print(s.lemonadeChange([5,5,10,10,20]))