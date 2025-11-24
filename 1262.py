# 1262. Greatest Sum Divisible by Three
# Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

from typing import List

class Solution:
    def get_two_lowest(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        low1 = float("inf")
        low2 = float("inf")
        for num in nums:
            if num < low1:
                low2 = low1
                low1 = num
            elif num < low2:
                low2 = num
        return [low1, low2]   

    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        total_r = total % 3
        if not total_r:
            return total
        r_ones = []
        r_twos = []
        for num in nums:
            r = num % 3
            if r == 1:
                r_ones.append(num)
            elif r == 2:
                r_twos.append(num)
        low_r_ones = self.get_two_lowest(r_ones)
        low_r_twos = self.get_two_lowest(r_twos)
        opt1 = opt2 = 0
        if total_r == 1:
            if low_r_ones:
                opt1 = total - low_r_ones[0]
            if len(low_r_twos) == 2:
                opt2 = total - sum(low_r_twos)
        elif total_r == 2:
            if low_r_twos:
                opt1 = total - low_r_twos[0]
            if len(low_r_ones) == 2:
                opt2 = total - sum(low_r_ones)
        return max(opt1, opt2)