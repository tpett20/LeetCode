# 1769. Minimum Number of Operations to Move All Balls to Each Box
# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.
# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.
# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.
# Each answer[i] is calculated considering the initial state of the boxes.

from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        prefix_sum = 0
        box_count = 0
        for i in range(len(boxes)):
            answer.append(prefix_sum)
            if boxes[i] == "1":
                box_count += 1
            prefix_sum += box_count
        prefix_sum = 0
        box_count = 0
        for i in range(len(boxes) - 1, -1, -1):
            answer[i] += prefix_sum
            if boxes[i] == "1":
                box_count += 1
            prefix_sum += box_count
        return answer

s = Solution()
print(s.minOperations("110"))
print(s.minOperations("11111"))
print(s.minOperations("10000"))
print(s.minOperations("00001"))