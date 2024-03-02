# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        output = []
        neg_idx = 0
        while neg_idx < len(nums) and nums[neg_idx] < 0:
            neg_idx += 1
        pos_idx = neg_idx
        neg_idx -= 1
        while pos_idx < len(nums) and nums[pos_idx] == 0:
            output.append(0)
            pos_idx += 1
        while neg_idx >= 0 and pos_idx < len(nums):
            if -nums[neg_idx] <= nums[pos_idx]:
                output.append(nums[neg_idx] ** 2)
                neg_idx -= 1
            else:
                output.append(nums[pos_idx] ** 2)
                pos_idx += 1
        while neg_idx >= 0:
            output.append(nums[neg_idx] ** 2)
            neg_idx -= 1
        while pos_idx < len(nums):
            output.append(nums[pos_idx] ** 2)
            pos_idx += 1
        return output

s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
print(s.sortedSquares([-7,-3,2,3,11]))