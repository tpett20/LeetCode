# 209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

def minSubArrayLen(target, nums):
    minLen = len(nums) + 1
    count = 0
    sum = 0
    startIdx = 0
    i = 0
    while i < len(nums):
        print(nums[i])
        if nums[i] >= target:
            return 1
        sum += nums[i]
        count += 1
        if sum >= target and count < minLen:
            print('RESET')
            minLen = count
            frontNums = nums[startIdx]
            while sum - frontNums >= target:
                print('hit')
                minLen -= 1
                startIdx += 1
                frontNums += nums[startIdx]
            count = 0
            sum = 0
            i -= 1
            startIdx = i
        i += 1
        print('minLen', minLen, 'count', count, 'sum', sum)
    return minLen if minLen < len(nums) + 1 else 0

print('Output:', minSubArrayLen(80, [10,5,13,4,8,4,5,11,14,9,16,10,20,8]))