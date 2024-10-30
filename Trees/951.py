# 951. Flip Equivalent Binary Trees
# For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
# A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
# Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        q1 = [root1]
        q2 = [root2]
        while q1 and q2:
            q1_len = len(q1)
            q2_len = len(q2)
            if q1_len != q2_len:
                return False
            map1 = {}
            for _ in range(q1_len):
                curr = q1.pop(0)
                map1[curr.val] = []
                if curr.left:
                    map1[curr.val].append(curr.left.val)
                    q1.append(curr.left)
                if curr.right:
                    map1[curr.val].append(curr.right.val)
                    q1.append(curr.right)
            for _ in range(q2_len):
                curr = q2.pop(0)
                if curr.val not in map1:
                    return False
                if curr.left:
                    if curr.left.val not in map1[curr.val]:
                        return False
                    q2.append(curr.left)
                if curr.right:
                    if curr.right.val not in map1[curr.val]:
                        return False
                    q2.append(curr.right)
        if q1 or q2:
            return False
        return True