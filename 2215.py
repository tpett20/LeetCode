# 2215. Find the Difference of Two Arrays
# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

def findDifference(nums1, nums2):
    map1 = {}
    map2 = {}
    answer = [[], []]
    for num in nums1:
        if not map1.get(num):
            map1[num] = 'nums1'
    for num in nums2:
        if map1.get(num):
            map1[num] = 'both'
        else:
            if not map2.get(num):
                map2[num] = 'nums2'
    for key in map1:
        if map1[key] == 'nums1':
            answer[0].append(key)
    for key in map2:
        answer[1].append(key)
    return answer
            
print(findDifference([1,9,9], [1,10,10]))