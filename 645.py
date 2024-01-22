# 645. Set Mismatch
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        output = [0, 0]
        s = set()
        for num in nums:
            if num in s:
                output[0] = num
            else:
                s.add(num)
        for num in range(1, len(nums) + 1):
            if num not in s:
                output[1] = num
                break
        return output

s = Solution()
print(s.findErrorNums([1,2,2,4]))
print(s.findErrorNums([2,2,3,4]))
print(s.findErrorNums([1,2,3,4,4]))