# 1207. Unique Number of Occurrences
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq_map = {}
        for num in arr:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        freq_set = set()
        for num in freq_map:
            freq = freq_map[num]
            if freq in freq_set:
                return False
            else:
                freq_set.add(freq)
        return True

s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))
print(s.uniqueOccurrences([1,2]))
print(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))