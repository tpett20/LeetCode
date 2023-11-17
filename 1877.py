# 1877. Minimize Maximum Pair Sum in Array
# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.
# - For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
# Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:
# - Each element of nums is in exactly one pair, and
# - The maximum pair sum is minimized.
# Return the minimized maximum pair sum after optimally pairing up the elements.

class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        max_sum = 0
        while i < j:
            sum = nums[i] + nums[j]
            max_sum = max(sum, max_sum)
            i += 1
            j -= 1
        return max_sum

s = Solution()
print(s.minPairSum([3,5,2,3]))
print(s.minPairSum([3,5,4,2,4,6]))