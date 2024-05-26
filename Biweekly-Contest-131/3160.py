# 3160. Find the Number of Distinct Colors Among the Balls
# 🏆 Biweekly Contest 131 - Solved Problem in 30:41 (🐞 1 Incorrect Attempt)
# You are given an integer limit and a 2D array queries of size n x 2.
# There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.
# Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.
# Note that when answering a query, lack of a color will not be considered as a color.

from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        m = {}
        output = []
        for q in queries:
            ball = q[0]
            color = q[1]
            if ball in balls:
                remove = balls[ball]
                m[remove] -= 1
                if m[remove] == 0:
                    del m[remove]
                balls[ball] = color
            else:
                balls[ball] = color
            if color in m:
                m[color] += 1
            else:
                m[color] = 1
            output.append(len(m))
        return output

s = Solution()
print(s.queryResults(4, [[1,4],[2,5],[1,3],[3,4]]))
print(s.queryResults(4, [[0,1],[1,2],[2,2],[3,4],[4,5],[0,2]]))