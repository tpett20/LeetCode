# 506. Relative Ranks
# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
    # The 1st place athlete's rank is "Gold Medal".
    # The 2nd place athlete's rank is "Silver Medal".
    # The 3rd place athlete's rank is "Bronze Medal".
    # For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.

from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s_scores = sorted(score, reverse=True)
        idxs = {}
        for i in range(len(score)):
            idxs[score[i]] = i
        output = ["0"] * len(s_scores)
        idx = idxs[s_scores[0]]
        output[idx] = "Gold Medal"
        if len(s_scores) > 1:
            idx = idxs[s_scores[1]]
            output[idx] = "Silver Medal"
        if len(s_scores) > 2:
            idx = idxs[s_scores[2]]
            output[idx] = "Bronze Medal"
        for i in range(3, len(s_scores)):
            idx = idxs[s_scores[i]]
            output[idx] = str(i + 1)
        return output

s = Solution()
print(s.findRelativeRanks([5,4,3,2,1]))
print(s.findRelativeRanks([10,3,8,9,4]))