# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

def moveZeroes(nums):
    i = 0
    count = 0
    length = len(nums)
    while i < length:
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
        i += 1
    for i in range(count, len(nums)):
        nums[i] = 0
    return nums

print(moveZeroes([0,1,0,3,12]))