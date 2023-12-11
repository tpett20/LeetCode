# 1287. Element Appearing More Than 25% In Sorted Array
# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        if len(arr) < 4:
            return arr[0]
        target = len(arr) / 4
        i = count = 1
        prev_int = arr[0]
        while True:
            if arr[i] == prev_int:
                count += 1
                if count > target:
                    return arr[i]
            else:
                count = 1
            prev_int = arr[i]
            i += 1
        
s = Solution()
print(s.findSpecialInteger([1,2,2,6,6,6,6,7,10]))