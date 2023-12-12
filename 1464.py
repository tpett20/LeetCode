# 1464. Maximum Product of Two Elements in an Array
# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        high = nums[0]
        scnd_high = float('-inf')
        for i in range(1, len(nums)):
            num = nums[i]
            if num > high:
                scnd_high = high
                high = num
            elif num > scnd_high:
                scnd_high = num
        return (high - 1) * (scnd_high - 1)

s = Solution()
print(s.maxProduct([3,4,5,2]))
print(s.maxProduct([1,5,4,5]))
print(s.maxProduct([3,7]))