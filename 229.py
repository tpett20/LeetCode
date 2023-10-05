# 229. Majority Element II
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

def majorityElement(nums):
    output = set()
    cutoff = len(nums) // 3
    map = {}
    for num in nums:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1
        if map[num] > cutoff:
            output.add(num)
    return output

print(majorityElement([3,2,3]))
print(majorityElement([1]))
print(majorityElement([1,2]))