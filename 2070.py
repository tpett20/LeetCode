# 2070. Most Beautiful Item for Each Query
# You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.
# You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.
# Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        def find_best_deal(price):
            flr = 0
            ceil = len(deals) - 1
            while flr <= ceil:
                mid = (flr + ceil) // 2
                deal = deals[mid]
                if price < deal[0]:
                    ceil = mid - 1
                elif price > deal[1]:
                    flr = mid + 1
                else:
                    return deal[2]
        
        itms = sorted(items)
        deals = [[itms[0][0], itms[0][0], itms[0][1]]]
        for item in itms:
            curr_price, curr_beauty = item
            last_deal = deals[-1]
            if curr_beauty > last_deal[2]:
                if curr_price > last_deal[1]:
                    deals.append([curr_price, curr_price, curr_beauty])
                    last_deal[1] = curr_price - 1
                else:
                    last_deal[1] = curr_price
                    last_deal[2] = curr_beauty
        answer = []
        for budget in queries:
            if budget < deals[0][0]:
                answer.append(0)
            elif budget > deals[-1][1]:
                answer.append(deals[-1][2])
            else:
                answer.append(find_best_deal(budget))
        return answer

s = Solution()
print(s.maximumBeauty([[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6]))