# 1089. Duplicate Zeros
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        original = arr.copy()
        n = len(arr)
        i = 0
        j = 0
        while i < n:
            num = original[j]
            arr[i] = num
            if num == 0 and i + 1 < n:
                arr[i + 1] = 0
                i += 1
            i += 1
            j += 1