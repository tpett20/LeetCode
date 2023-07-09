# 2765. Longest Alternating Subarray
# Biweekly Contest 108
# You are given a 0-indexed integer array nums. A subarray s of length m is called alternating if:
# m is greater than 1.
# s1 = s0 + 1.
# The 0-indexed subarray s looks like [s0, s1, s0, s1,...,s(m-1) % 2]. In other words, s1 - s0 = 1, s2 - s1 = -1, s3 - s2 = 1, s4 - s3 = -1, and so on up to s[m - 1] - s[m - 2] = (-1)m.
# Return the maximum length of all alternating subarrays present in nums or -1 if no such subarray exists.
# A subarray is a contiguous non-empty sequence of elements within an array.

def alternatingSubarray(nums):
    maxLen = 0
    subLen = 1
    i = 0
    while i < len(nums) - 1:
        # print(subLen, subLen % 2, nums[i])
        if subLen % 2 == 0:
            # print('hit1')
            if nums[i + 1] == nums[i] - 1:
                # print('Down Hit')
                subLen += 1
                if subLen > maxLen:
                    maxLen = subLen
            else: 
                subLen = 1
                i -= 1
        elif nums[i + 1] == nums[i] + 1:
            # print('Up Hit')
            subLen += 1
            if subLen > maxLen:
                maxLen = subLen
        else:
            subLen = 1
        i += 1
    return maxLen if maxLen > 1 else -1

print(alternatingSubarray([2,3,4,3,4]))
print(alternatingSubarray([64,65,64,65,64,65,66,65,66,65]))
print(alternatingSubarray([1,1]))