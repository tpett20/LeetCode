# 219. Contains Duplicate II
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

def containsNearbyDuplicate(nums, k):
    map = {}
    for i in range(len(nums)):
        if map.get(nums[i]) and (i - (map[nums[i]] - 1) <= k):
            return True
        else:
            map[nums[i]] = i + 1
    return False

print(containsNearbyDuplicate([1,2,3,1], 3), '(Expected: True)')
print(containsNearbyDuplicate([1,0,1,1], 1), '(Expcted: True)')
print(containsNearbyDuplicate([1,2,3,1,2,3], 2), '(Expected: False)')