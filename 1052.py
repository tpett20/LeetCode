# 1052. Grumpy Bookstore Owner
# There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
# On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
# Return the maximum number of customers that can be satisfied throughout the day.

from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        if minutes == len(customers):
            return sum(customers)
        count = 0
        for i in range(minutes):
            count += customers[i]
        for i in range(minutes, len(customers)):
            if not grumpy[i]:
                count += customers[i]
        max_count = count
        for r in range(minutes, len(customers)):
            l = r - minutes
            if grumpy[l]:
                count -= customers[l]
            if grumpy[r]:
                count += customers[r]
            max_count = max(max_count, count)
        return max_count

s = Solution()
print(s.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))
print(s.maxSatisfied([1], [0], 1))