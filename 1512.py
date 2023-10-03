# 1512. Number of Good Pairs
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

def numIdenticalPairs(nums):
    pairs = 0
    map = {}
    for num in nums:
        if not num in map:
            map[num] = 1
        else:
            pairs += map[num]
            map[num] += 1
    return pairs

print(numIdenticalPairs([1,2,3,1,1,3]))
print(numIdenticalPairs([1,1,1,1]))
print(numIdenticalPairs([1,2,3]))