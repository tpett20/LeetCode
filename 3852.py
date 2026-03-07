# 3852. Smallest Pair With Different Frequencies
# You are given an integer array nums.
# Consider all pairs of distinct values x and y from nums such that:
    # x < y
    # x and y have different frequencies in nums.
# Among all such pairs:
    # Choose the pair with the smallest possible value of x.
    # If multiple pairs have the same x, choose the one with the smallest possible value of y.
# Return an integer array [x, y]. If no valid pair exists, return [-1, -1].

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        res = [101, 101]
        freq_map = {}
        smallest_nums_by_freq = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        for num in freq_map:
            freq = freq_map[num]
            smallest_nums_by_freq[freq] = min(num, smallest_nums_by_freq.get(freq, 101))
        if len(smallest_nums_by_freq) < 2:
            return [-1, -1]
        for num in smallest_nums_by_freq.values():
            if num < res[0]:
                res[1] = res[0]
                res[0] = num
            elif num < res[1]:
                res[1] = num
        return res