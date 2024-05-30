# 1442. Count Triplets That Can Form Two Arrays of Equal XOR
# Given an array of integers arr.
# We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
# Let's define a and b as follows:
    # a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
    # b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# Note that ^ denotes the bitwise-xor operation.
# Return the number of triplets (i, j and k) Where a == b.

from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        a_vals = []
        for i in range(len(arr) - 1):
            for l in range(len(a_vals)):
                a_vals[l] ^= arr[i]
            a_vals.append(arr[i])
            b = 0
            for k in range(i + 1, len(arr)):
                b ^= arr[k]
                count += a_vals.count(b)
        return count

s = Solution()
print(s.countTriplets([2,3,1,6,7]))
print(s.countTriplets([1,1,1,1,1]))