# 349. Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        output = []
        for num in set1:
            if num in set2:
                output.append(num)
        return output
    
s = Solution()
print(s.intersection([1,2,2,1], [2,2]))
print(s.intersection([4,9,5], [9,4,9,8,4]))