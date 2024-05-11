# 1200. Minimum Absolute Difference
# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
    # a, b are from arr
    # a < b
    # b - a equals to the minimum absolute difference of any two elements in arr

from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        output = []
        s_arr = sorted(arr)
        min_diff = float('inf')
        for i in range(1, len(s_arr)):
            diff = s_arr[i] - s_arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                output = [[s_arr[i - 1], s_arr[i]]]
            elif diff == min_diff:
                output.append([s_arr[i - 1], s_arr[i]])
        return output

s = Solution()
print(s.minimumAbsDifference([4,2,1,3]))
print(s.minimumAbsDifference([1,3,6,10,15]))
print(s.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))