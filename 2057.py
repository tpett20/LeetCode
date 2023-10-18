# 2057. Smallest Index With Equal Value
# Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.
# x mod y denotes the remainder when x is divided by y.

class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        for i, num in enumerate(nums):
            if i % 10 == num:
                return i
        return -1

s = Solution()
print(s.smallestEqual([0,1,2]))
print(s.smallestEqual([4,3,2,1]))
print(s.smallestEqual([1,2,3,4,5,6,7,8,9,10,10]))