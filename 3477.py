# 3477. Fruits Into Baskets II
# You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.
# From left to right, place the fruits according to these rules:
    # Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
    # Each basket can hold only one type of fruit.
    # If a fruit type cannot be placed in any basket, it remains unplaced.
# Return the number of fruit types that remain unplaced after all possible allocations are made.

from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0
        b = baskets.copy()
        for fruit in fruits:
            placed = False
            for i, basket in enumerate(b):
                if basket >= fruit:
                    b[i] = 0
                    placed = True
                    break
            if not placed:
                unplaced += 1
        return unplaced

s = Solution()
print(s.numOfUnplacedFruits([4,2,5], [3,5,4]))
print(s.numOfUnplacedFruits([1,2,3,4,5], [1,2,3,4,5]))