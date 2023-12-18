# 1913. Maximum Product Difference Between Two Pairs
# The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).
# - For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
# Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.
# Return the maximum such product difference.

class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        high = second_high = float('-inf')
        low = second_low = float('inf')
        for num in nums:
            if num >= high:
                second_high = high
                high = num
            elif num > second_high:
                second_high = num
            if num <= low:
                second_low = low
                low = num
            elif num < second_low:
                second_low = num
        return high * second_high - low * second_low

s = Solution()
print(s.maxProductDifference([5,6,2,7,4]))
print(s.maxProductDifference([4,2,5,9,7,4,8]))
print(s.maxProductDifference([1,1,1,1]))