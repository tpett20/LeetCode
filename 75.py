# 75. Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        while l < len(nums) and nums[l] == 0:
            l += 1
        r = len(nums) - 1
        while r >= 0 and nums[r] == 2:
            r -= 1
        i = l
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1

test_case = [1,0,2,2,0,1]
print("Before:", test_case)
s = Solution()
s.sortColors(test_case)
print("After: ", test_case)