# 1356. Sort Integers by The Number of 1 Bits
# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.
# Return the array after sorting it.

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        def countOneBits(num):
            one_count = 0
            while num != 0:
                one_count += num % 2
                num = num // 2
            return one_count

        def sortFunc(num):
            ones = countOneBits(num)
            decimal = num / 100000
            return ones + decimal

        arr.sort(key=sortFunc)
        return arr

s = Solution()
print(s.sortByBits([0,1,2,3,4,5,6,7,8]))
print(s.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))