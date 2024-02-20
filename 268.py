# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        range_sum = (len(nums) + 1) * len(nums) // 2
        actual_sum = sum(nums)
        return range_sum - actual_sum

s = Solution()
print(s.missingNumber([3,0,1]))
print(s.missingNumber([0,1]))
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))