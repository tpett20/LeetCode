# 1679. Max Number of K-Sum Pairs
# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        count = 0
        freq = {}
        for num in nums:
            if num >= k:
                continue
            diff = k - num
            if diff in freq and freq[diff]:
                count += 1
                freq[diff] -= 1
            elif num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        return count

s = Solution()
print(s.maxOperations([1,2,3,4], 5))
print(s.maxOperations([3,1,3,4,3], 6))