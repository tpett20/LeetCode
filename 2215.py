# 2215. Find the Difference of Two Arrays
# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

def findDifference(nums1, nums2):
    map = {}
    answer = [[], []]
    for num in nums1:
        if not map.get(num):
            map[num] = 'nums1'
    for num in nums2:
        if map.get(num):
            map[num] = 'both'
        else:
            answer[1].append(num)
    for key in map:
        if map[key] == 'nums1':
            answer[0].append(key)
    return answer
            

print(findDifference([-80,-15,-81,-28,-61,63,14,-45,-35,-10], [-1,-40,-44,41,10,-43,69,10,2]))