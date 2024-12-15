# 2593. Find Score of an Array After Marking All Elements
# You are given an array nums consisting of positive integers.
# Starting with score = 0, apply the following algorithm:
# Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
# Add the value of the chosen integer to score.
# Mark the chosen element and its two adjacent elements if they exist.
# Repeat until all the array elements are marked.
# Return the score you get after applying the above algorithm.

from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        def get_idx(val):
            map_idx = nums_map[val]["curr"]
            if (map_idx == len(nums_map[val]["idxs"])):
                return -1
            ret_idx = nums_map[val]["idxs"][map_idx]
            nums_map[val]["curr"] += 1
            if (ret_idx in seen or
                ret_idx + 1 in seen or
                ret_idx - 1 in seen):
                return -1
            return ret_idx

        nums_map = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in nums_map:
                nums_map[num]["idxs"].append(i)
            else:
                nums_map[num] = {}
                nums_map[num]["idxs"] = [i]
                nums_map[num]["curr"] = 0
        s_nums = sorted(nums)
        seen = set()
        flr = 0
        score = 0
        while flr < len(s_nums):
            low_val = s_nums[flr]
            low_val_idx = get_idx(low_val)
            if low_val_idx == -1:
                flr += 1
                continue
            else:
                score += nums[low_val_idx]
                seen.add(low_val_idx)
        return score

s = Solution()
print(s.findScore([2,1,3,4,5,2]))
print(s.findScore([1] * 10000))