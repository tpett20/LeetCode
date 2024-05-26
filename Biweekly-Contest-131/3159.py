# 3159. Find Occurrences of an Element in an Array
# 🏆 Biweekly Contest 131 - Solved Problem in 10:49
# You are given an integer array nums, an integer array queries, and an integer x.
# For each queries[i], you need to find the index of the queries[i]th occurrence of x in the nums array. If there are fewer than queries[i] occurrences of x, the answer should be -1 for that query.
# Return an integer array answer containing the answers to all queries.

from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        m = {}
        count = 1
        for i in range(len(nums)):
            if nums[i] == x:
                m[count] = i
                count += 1
        output = []
        for q in queries:
            if q not in m:
                output.append(-1)
            else:
                output.append(m[q])
        return output

s = Solution()
print(s.occurrencesOfElement([1,3,1,7], [1,3,2,4], 1))
print(s.occurrencesOfElement([1,2,3], [10], 5))
print(s.occurrencesOfElement([1], [1], 1))