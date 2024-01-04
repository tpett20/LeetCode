# 2870. Minimum Number of Operations to Make Array Empty
# You are given a 0-indexed array nums consisting of positive integers.
# There are two types of operations that you can apply on the array any number of times:
# - Choose two elements with equal values and delete them from the array.
# - Choose three elements with equal values and delete them from the array.
# Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1
        ops = 0
        for num in m:
            qty = m[num]
            if qty == 1:
                return -1
            else:
                if qty % 3 == 0:
                    ops += qty // 3
                else:
                    ops += qty // 3 + 1
        return ops
            
s = Solution()
print(s.minOperations([2,3,3,2,2,4,2,3,4]))
print(s.minOperations([2,1,2,2,3,3]))