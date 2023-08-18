# 88. Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    j = 0
    while i < len(nums1) and j < n:
        if nums2[j] <= nums1[i]:
            nums1.insert(i, nums2[j])
            nums1.pop()
            j += 1
            m += 1
        elif i == m:
            nums1[i] = nums2[j]
            j += 1
            m += 1
        i += 1
    print(nums1)

merge([1,2,3,0,0,0], 3, [2,5,6], 3)