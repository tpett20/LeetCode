# 1590. Make Sum Divisible by P
# Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.
# Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.
# A subarray is defined as a contiguous block of elements in the array.

from typing import List

class Solution:
    def find_best_mod_idx(self, mod: int, idx: int, mod_idxs: dict, p: int) -> int:
        pair_mod = (p - mod) % p
        if pair_mod not in mod_idxs:
            return -1
        while mod_idxs[pair_mod]:
            best_idx = mod_idxs[pair_mod][-1]
            if best_idx <= idx:
                mod_idxs[pair_mod].pop()
            else:
                return best_idx
        return -1

    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        min_len = n
        rt_mods = {}
        total = 0
        for i in range(n - 1, -1, -1):
            total += nums[i]
            mod = total % p
            if mod in rt_mods:
                rt_mods[mod].append(i)
            else:
                rt_mods[mod] = [i]
            if not mod:
                min_len = min(min_len, i)
        if min_len <= 1:
            return min_len
        total = 0
        for i in range(n):
            total += nums[i]
            mod = total % p
            best_mod_idx = self.find_best_mod_idx(mod, i, rt_mods, p)
            if best_mod_idx != -1:
                dist = best_mod_idx - (i + 1)
                min_len = min(min_len, dist)
            if not mod:
                min_len = min(min_len, n - (i + 1))
        return min_len if min_len < n else -1

s = Solution()
print(s.minSubarray([3,1,4,2], 6))