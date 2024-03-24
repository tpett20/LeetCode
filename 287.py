# 287. Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        new_slow = nums[0]
        while slow != new_slow:
            slow = nums[slow]
            new_slow = nums[new_slow]
        return slow

s = Solution()
print(s.findDuplicate([1,3,4,2,2]))
print(s.findDuplicate([3,1,3,4,2]))
print(s.findDuplicate([3,3,3,3,3]))
print(s.findDuplicate([2,5,9,6,9,3,8,9,7,1]))