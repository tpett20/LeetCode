# 2610. Convert an Array Into a 2D Array With Conditions
# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:
# - The 2D array should contain only the elements of the array nums.
# - Each row in the 2D array contains distinct integers.
# - The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.
# Note that the 2D array can have a different number of elements on each row.

class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1
        output = []
        for num in m:
            for i in range(m[num]):
                if i >= len(output):
                    output.append([num])
                else:
                    output[i].append(num)
        return output

s = Solution()
print(s.findMatrix([1,3,4,1,2,3,1]))
print(s.findMatrix([1,2,3,4]))