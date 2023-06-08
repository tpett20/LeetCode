# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums, target):
    map = {}
    for i in range(len(nums)):
        if map.get(nums[i]):
            map[nums[i]].append(i)
        else: 
            map[nums[i]] = [i]
    for num in map:
        difference = target - int(num)
        if difference == num: 
            if len(map.get(num)) > 1:
                return map.get(num)
        elif map.get(difference):
            return [map.get(num)[0], map.get(difference)[0]]

print(twoSum([2,7,11,15], 9))

# alternate, simpler method with better memory inspired by peyman_np's solution
# https://leetcode.com/problems/two-sum/solutions/737092/sum-megapost-python3-solution-with-a-detailed-explanation/
# def twoSum(nums, target):
#     map = {}
#     for i in range(len(nums)):
#         difference = target - nums[i]
#         if map.get(difference):
#             return [i, map.get(difference) - 1]
#         else: 
#             map[nums[i]] = i + 1

# alternate method with better memory but worse runtime
# def twoSum(nums, target):
#     map = {}
#     for num in nums:
#         if map.get(num):
#             map[num] += 1
#         else: 
#             map[num] = 1
#     for i in range(len(nums)):
#         difference = target - nums[i]
#         if difference == nums[i]:
#             if map.get(difference) > 1:
#                 idx = nums.index(difference, i + 1)
#                 return [i, idx]
#         elif map.get(difference):
#             idx = nums.index(difference)
#             return [i, idx]