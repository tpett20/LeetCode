# 33. Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def find_original_end(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] <= nums[-1]:
            return n - 1
        flr = 0
        ceil = len(nums) - 1
        while True:
            mid = (flr + ceil) // 2
            if nums[mid] > nums[(mid + 1) % n]:
                return mid
            if nums[mid - 1] > nums[mid]:
                return mid - 1
            if nums[mid] < nums[flr]:
                ceil = mid - 1
            elif nums[mid] > nums[ceil]:
                flr = mid + 1
    
    def binary_search(self, nums: List[int], target: int) -> int:
        flr = 0
        ceil = len(nums) - 1
        while flr <= ceil:
            mid = (flr + ceil) // 2
            if nums[mid] > target:
                ceil = mid - 1
            elif nums[mid] < target:
                flr = mid + 1
            else:
                return mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_original_end(nums)
        res1 = self.binary_search(nums[:pivot + 1], target)
        if res1 > -1:
            return res1
        res2 = self.binary_search(nums[pivot + 1:], target)
        if res2 > -1:
            return res2 + pivot + 1
        return -1

s = Solution()
print(s.search([4, 5, 6, 0, 1, 2], 0))
print(s.search([1, 2, 3, 4], 0))
print(s.search([4, 5, 1, 2, 3], 1))