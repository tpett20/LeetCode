# 3202. Find the Maximum Length of Valid Subsequence II
# You are given an integer array nums and a positive integer k.
# A subsequence sub of nums with length x is called valid if it satisfies:
    # (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
# Return the length of the longest valid subsequence of nums.

from typing import List

class Solution:
    def get_max_len(self, arrA: List[int], arrB: List[int]) -> int:
        arr1 = arrA.copy()
        arr2 = arrB.copy()
        count = 0
        prev1 = arr1[0] > arr2[0]
        while arr1 and arr2:
            if arr1[0] < arr2[0]:
                arr1.pop(0)
                if not prev1:
                    count += 1
                prev1 = True
            else:
                arr2.pop(0)
                if prev1:
                    count += 1
                prev1 = False
        if (arr1 and not prev1) or (arr2 and prev1):
            count += 1
        return count

    def maximumLength(self, nums: List[int], k: int) -> int:
        r_map = {}
        for idx, num in enumerate(nums):
            r = num % k
            if r in r_map:
                r_map[r].append(idx)
            else:
                r_map[r] = [idx]
        max_count = 0
        all_rs = []
        for r in r_map:
            count = len(r_map[r])
            max_count = max(count, max_count)
            all_rs.append(r)
        rs_len = len(all_rs)
        for i in range(rs_len - 1):
            for j in range(i + 1, rs_len):
                r1 = all_rs[i]
                r1idxs = r_map[r1]
                r2 = all_rs[j]
                r2idxs = r_map[r2]
                max_potential = min(len(r1idxs), len(r2idxs)) * 2 + 1
                if max_potential > max_count:
                    count = self.get_max_len(r1idxs, r2idxs)
                    max_count = max(max_count, count)
        return max_count