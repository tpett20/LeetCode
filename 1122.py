# 1122. Relative Sort Array
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict2 = {}
        for num in arr2:
            dict2[num] = []
        extra = []
        for num in arr1:
            if num in dict2:
                dict2[num].append(num)
            else:
                extra.append(num)
        output = []
        for num in dict2:
            output += dict2[num]
        return output + sorted(extra)

s = Solution()
print(s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
print(s.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))