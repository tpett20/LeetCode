# 2418. Sort the People
# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
# For each index i, names[i] and heights[i] denote the name and height of the ith person.
# Return names sorted in descending order by the people's heights.

from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ref = {}
        for i in range(len(names)):
            ref[heights[i]] = names[i]
        
        hts = sorted(heights, reverse=True)
        output = []
        for height in hts:
            output.append(ref[height])
        return output

s = Solution()
print(s.sortPeople(["Mary", "John", "Emma", "Mike Piazza"], heights = [180, 165, 170, 250]))