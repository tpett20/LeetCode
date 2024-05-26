# 3161. Block Placement Queries
# 🚫 INCOMPLETE - Biweekly Contest 131 - Wrong Answer
# There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.
# You are given a 2D array queries, which contains two types of queries:
    # For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
    # For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.
# Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.

from typing import List

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        def b_search(pos, arr):
            low = 0
            hi = len(arr) - 1
            while low <= hi:
                mid = (low + hi) // 2
                if arr[mid][1] < pos:
                    low = mid + 1
                elif arr[mid][1] > pos:
                    hi = mid - 1
                else:
                    return mid
            return mid
        
        def check_itvls(arr, size, pos):
            if not len(arr):
                return True
            i = 0
            while i < len(arr) and arr[i][1] <= pos:
                space = arr[i][1] - arr[i][0]
                if space >= size:
                    return True
                i += 1
            if i == len(arr):
                return False
            space = pos - arr[i][0]
            if space >= size:
                return True
            return False

        output = []
        intervals = []
        for q in queries:
            x = q[1]
            if q[0] == 1:
                # build obstacle
                if not len(intervals):
                    intervals.append([0, x])
                    continue
                idx = b_search(x, intervals)
                if intervals[idx][1] == x:
                    continue
                elif intervals[idx][1] < x:
                    lo = intervals[idx][1]
                    new_intvl = [lo, x]
                    if len(intervals) > idx + 1:
                        intervals[idx + 1][0] = x
                    intervals.insert(idx+1, new_intvl)
                else:
                    if idx == 0:
                        intervals[idx][0] = x
                        new_intvl = [0, x]
                        intervals.insert(0, new_intvl)
                        continue
                    lo = intervals[idx-1][1]
                    new_intvl = [lo, x]
                    intervals[idx][0] = x
                    intervals.insert(idx, new_intvl)
            else:
                # check block
                sz = q[2]
                output.append(check_itvls(intervals, sz, x))
        return output

s = Solution()
print(s.getResults([[1,2],[2,3,3],[2,3,1],[2,2,2]]))
print(s.getResults([[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]))
print(s.getResults([[1,7],[1,6],[1,10], [1, 2],[2,10,2]]))