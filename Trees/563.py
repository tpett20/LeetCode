# 563. Binary Tree Tilt
# Given the root of a binary tree, return the sum of every tree node's tilt.
# The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.tilt = 0
    
    def traverse(self, node):
        if not node:
            return 0
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        self.tilt += abs(left - right)
        return node.val + left + right

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.tilt

test_case = TreeNode(1)
test_case.left = TreeNode(2)
test_case.right = TreeNode(3)

s = Solution()
print(s.findTilt(test_case))