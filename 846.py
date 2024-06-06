# 846. Hand of Straights
# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True
        cards = sorted(hand)
        stack = [[1, cards[0]]]
        for i in range(1, len(cards)):
            if not len(stack) or cards[i] == stack[-1][1]:
                stack.append([1, cards[i]])
            elif cards[i] - stack[-1][1] == 1:
                stack[-1][0] += 1
                stack[-1][1] = cards[i]
                last = stack.pop()
                if last[0] != groupSize:
                    stack.insert(0, last)
            else:
                return False
        return False if len(stack) else True

s = Solution()
print(s.isNStraightHand([1,2,3,6,2,3,8,4,7], 3))
print(s.isNStraightHand([1,2,3,4,5], 4))
print(s.isNStraightHand([1,22,333], 1))