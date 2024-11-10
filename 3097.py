# 3097. Shortest Subarray With OR at Least K II
# You are given an array nums of non-negative integers and an integer k.
# An array is called special if the bitwise OR of all of its elements is at least k.
# Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def check_if_special(curr, target):
            for i in range(len(curr)):
                if curr[i] >= 1 and target[i] == "0":
                    return True
                elif target[i] == "1" and curr[i] == 0:
                    return False
            return True
        
        def update_freq(curr, string, add):
            for i in range(len(string)):
                c_idx = len(curr) - 1 - i
                s_idx = len(string) - 1 - i
                if string[s_idx] == "1":
                    if add:
                        curr[c_idx] += 1
                    else:
                        curr[c_idx] -= 1
        
        k_bits = list(bin(k)[2:])
        bit_freq = [0] * len(k_bits)
        min_len = float("inf")
        l = 0
        for r in range(len(nums)):
            new_num = nums[r]
            if new_num >= k:
                return 1
            new_bits = bin(new_num)[2:]
            update_freq(bit_freq, new_bits, add=True)
            while check_if_special(bit_freq, k_bits):
                min_len = min(min_len, (r - l) + 1)
                del_bits = bin(nums[l])[2:]
                l += 1
                update_freq(bit_freq, del_bits, add=False)
        return min_len if min_len < float("inf") else -1

s = Solution()
print(s.minimumSubarrayLength([2, 1, 8], 10))
print(s.minimumSubarrayLength([2, 100], 10))
print(s.minimumSubarrayLength([1969, 1973, 1986, 2000, 2015], 2024))