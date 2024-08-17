# 624. Maximum Distance in Arrays
# You are given m arrays, where each array is sorted in ascending order.
# You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.
# Return the maximum distance.

from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        lowest = arrays[0][0]
        highest = arrays[0][-1]
        max_dist = 0
        for i in range(1, len(arrays)):
            arr = arrays[i]
            lo = arr[0]
            hi = arr[-1]
            dist1 = highest - lo
            dist2 = hi - lowest
            max_dist = max(max_dist, dist1, dist2)
            lowest = min(lo, lowest)
            highest = max(hi, highest)
        return max_dist
    
s = Solution()
print(s.maxDistance([[1,2,3], [4,5], [1,2,3]]))