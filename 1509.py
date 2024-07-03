# 1509. Minimum Difference Between Largest and Smallest Value in Three Moves
# You are given an integer array nums.
# In one move, you can choose one element of nums and change it to any value.
# Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        def check_opts(left, right, count):
            if count == 3:
                return 0
            lt_copy = left.copy()
            lt_total = lt_copy.pop()
            lt_total += check_opts(lt_copy, right.copy(), count + 1)
            rt_copy = right.copy()
            rt_total = rt_copy.pop()
            rt_total += check_opts(left.copy(), rt_copy, count + 1)
            return max(lt_total, rt_total)

        if len(nums) <= 4:
            return 0
        highest = [float('-inf')] * 4
        lowest = [float('inf')] * 4
        for num in nums:
            for i in range(4):
                if num > highest[i]:
                    highest.insert(i, num)
                    highest.pop()
                    break
            for i in range(4):
                if num < lowest[i]:
                    lowest.insert(i, num)
                    lowest.pop()
                    break
        max_diff = highest[0] - lowest[0]
        if max_diff == 0:
            return 0
        hi_diffs = []
        lo_diffs = []
        for i in range(2, -1, -1):
            hi_diffs.append(highest[i] - highest[i + 1])
            lo_diffs.append(lowest[i + 1] - lowest[i])
        max_savings = check_opts(lo_diffs, hi_diffs, 0)
        return max_diff - max_savings

s = Solution()
print(s.minDifference([1,5,0,10,14]))