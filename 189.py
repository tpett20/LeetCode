# 189. Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    steps = k % len(nums)
    copy = []
    for num in nums:
        copy.append(num)
    for i in range(len(nums)):
        nums[i] = copy[i - steps]
    print(nums)

rotate([1,2,3,4,5,6,7], 3)
rotate([1, 2], 3)
rotate([-1], 2)