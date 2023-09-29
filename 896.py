# 896. Monotonic Array
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

def isMonotonic(nums):
    if len(nums) <= 2:
        return True
    diffRule = nums[1] - nums[0]
    for i in range(2, len(nums)):
        diff = nums[i] - nums[i - 1]
        if diffRule == 0 and diff != 0:
            diffRule = diff
        elif diffRule > 0 and diff < 0:
            return False
        elif diffRule < 0 and diff > 0:
            return False
    return True

print(isMonotonic([1,1,2,2,3]))
print(isMonotonic([6,5,4,4]))
print(isMonotonic([1,3,2]))
print(isMonotonic([1,1,1,1]))