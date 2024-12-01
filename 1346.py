# 1346. Check If N and Its Double Exist
# Given an array arr of integers, check if there exist two indices i and j such that :
    # i != j
    # 0 <= i, j < arr.length
    # arr[i] == 2 * arr[j]

from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums = set(arr)
        has_zeros = False
        if 0 in nums:
            nums.remove(0)
            has_zeros = True
        for num in nums:
            if (num * 2) in nums:
                return True
        if not has_zeros or arr.count(0) < 2:
            return False
        return True

s = Solution()
print(s.checkIfExist([5,2,10,3]))
print(s.checkIfExist([-2,0,10,-19,4,6,-8]))