# 2285. Maximum Total Importance of Roads
# You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.
# You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.
# You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.
# Return the maximum total importance of all roads possible after assigning the values optimally.

from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        def get_freq(c):
            return freq[c]
        
        total = 0
        freq = {}
        for road in roads:
            city1, city2 = road
            if city1 in freq:
                freq[city1] += 1
            else:
                freq[city1] = 1
            if city2 in freq:
                freq[city2] += 1
            else:
                freq[city2] = 1
        cities = list(freq.keys())
        cities.sort(key=get_freq)
        total = 0
        val = n - len(cities)
        for city in cities:
            val += 1
            total += freq[city] * val
        return total

s = Solution()
print(s.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
print(s.maximumImportance(5, [[0,3],[2,4],[1,3]]))