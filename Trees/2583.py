# 2583. Kth Largest Sum in a Binary Tree
# You are given the root of a binary tree and a positive integer k.
# The level sum in the tree is the sum of the values of the nodes that are on the same level.
# Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.
# Note that two nodes are on the same level if they have the same distance from the root.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def bfs(node):
            q = [node]
            while len(q):
                q_len = len(q)
                row_sum = 0
                for _ in range(q_len):
                    curr = q.pop(0)
                    row_sum += curr.val
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                row_sums.append(row_sum)
        
        row_sums = []
        bfs(root)
        if len(row_sums) < k:
            return -1
        if k == 1:
            return max(row_sums)
        if k == len(row_sums):
            return min(row_sums)
        row_sums.sort(reverse=True)
        return row_sums[k - 1]