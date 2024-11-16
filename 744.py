# 744. Find Smallest Letter Greater Than Target
# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        flr = 0
        ceil = len(letters) - 1
        while flr <= ceil:
            mid = (flr + ceil) // 2
            if letters[mid] > target and (mid == 0 or letters[mid - 1] <= target):
                return letters[mid] 
            elif letters[mid] <= target:
                flr = mid + 1
            else:
                ceil = mid - 1
        return letters[0]

s = Solution()
print(s.nextGreatestLetter(["c","c","d","e","e","e","e","f","j"], "d"))