# 3396. Minimum Number of Operations to Make Elements in Array Distinct
# You are given an integer array nums. You need to ensure that the elements in the array are distinct. To achieve this, you can perform the following operation any number of times:
    # Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
# Note that an empty array is considered to have distinct elements. Return the minimum number of operations needed to make the elements in the array distinct.

import math
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        i = len(nums) - 1
        while i >= 0 and nums[i] not in seen:
            seen.add(nums[i])
            i -= 1
        return math.ceil((i + 1) / 3)

s = Solution()
print(s.minimumOperations([4,4]))
print(s.minimumOperations([10,1,2,3,4,5,6,7,8,9,10]))