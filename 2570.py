# 2570. Merge Two 2D Arrays by Summing Values
# You are given two 2D integer arrays nums1 and nums2.
    # nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
    # nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
# Each array contains unique ids and is sorted in ascending order by id.
# Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:
    # Only ids that appear in at least one of the two arrays should be included in the resulting array.
    # Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
# Return the resulting array. The returned array must be sorted in ascending order by id.

from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        arr = []
        i = j = 0
        n = len(nums1)
        m = len(nums2)
        while i < n and j < m:
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            if id1 == id2:
                arr.append([id1, val1 + val2])
                i += 1
                j += 1
            elif id1 < id2:
                arr.append([id1, val1])
                i += 1
            else:
                arr.append([id2, val2])
                j += 1
        if i < n:
            return arr + nums1[i:]
        elif j < m:
            return arr + nums2[j:]
        else:
            return arr

s = Solution()
print(s.mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))