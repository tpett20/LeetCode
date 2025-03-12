# 2529. Maximum Count of Positive Integer and Negative Integer
# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
    # In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def binary_search(pos_target):
            flr = 0
            ceil = len(nums) - 1
            while flr <= ceil:
                mid_idx = (flr + ceil) // 2
                if pos_target:
                    if nums[mid_idx] > 0:
                        if mid_idx == 0 or nums[mid_idx - 1] <= 0:
                            return mid_idx
                        else:
                            ceil = mid_idx - 1
                    elif nums[mid_idx] <= 0:
                        flr = mid_idx + 1
                else:
                    if nums[mid_idx] < 0:
                        if mid_idx == len(nums) - 1 or nums[mid_idx + 1] >= 0:
                            return mid_idx
                        else:
                            flr = mid_idx + 1
                    elif nums[mid_idx] >= 0:
                        ceil = mid_idx - 1
            return mid_idx
        
        pos_idx = binary_search(pos_target=True)
        pos_count = len(nums) - pos_idx if (nums[pos_idx] > 0) else 0
        if pos_count >= len(nums) / 2:
            return pos_count
        neg_idx = binary_search(pos_target=False)
        neg_count = neg_idx + 1 if (nums[neg_idx] < 0) else 0
        return max(neg_count, pos_count)

s = Solution()
print(s.maximumCount([-2,-1,-1,1,2,3]))
print(s.maximumCount([-2,0,0,0,0,0,0,0,0,0,0,0,1,2]))
print(s.maximumCount([-2]))