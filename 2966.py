# 2966. Divide Array Into Arrays With Max Difference
# You are given an integer array nums of size n and a positive integer k.
# Divide the array into one or more arrays of size 3 satisfying the following conditions:
    # Each element of nums should be in exactly one array.
    # The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        output = []
        sub_arr = []
        sorted_nums = sorted(nums)
        for num in sorted_nums:
            if len(sub_arr) == 0 or abs(num - sub_arr[0]) <= k:
                sub_arr.append(num)
            else:
                return []
            if len(sub_arr) == 3:
                output.append(sub_arr)
                sub_arr = []
        return output

s = Solution()
print(s.divideArray([1,3,4,8,7,9,3,5,1], 2))
print(s.divideArray([1,3,3,2,7,3], 3))
print(s.divideArray([6,10,5,12,7,11,6,6,12,12,11,7], 2))
print(s.divideArray([15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2], 2))