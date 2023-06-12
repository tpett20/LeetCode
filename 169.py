# 169. Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majorityElement(nums):
    if len(nums) <= 2: return nums[0]
    map = {}
    majority = len(nums) / 2
    for num in nums:
        if map.get(num): 
            map[num] += 1
            if map.get(num) >= majority:
                return num
        else: 
            map[num] = 1

print(majorityElement([2,2,1,1,1,2,2]))