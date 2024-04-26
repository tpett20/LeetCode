# 1372. Longest ZigZag Path in a Binary Tree
# You are given the root of a binary tree.
# A ZigZag path for a binary tree is defined as follow:
    # Choose any node in the binary tree and a direction (right or left).
    # If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
    # Change the direction from right to left or from left to right.
    # Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
# Return the longest ZigZag path contained in that tree.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, node: Optional[TreeNode], length=0, dir=None) -> int:
        left = right = 0
        if node.left:
            if dir == "r":
                left = self.longestZigZag(node.left, length + 1, "l")
            else:
                left = self.longestZigZag(node.left, 1, "l")
        if node.right:
            if dir == "l":
                right = self.longestZigZag(node.right, length + 1, "r")
            else:
                right = self.longestZigZag(node.right, 1, "r")
        return max(left, right, length)


test_case = TreeNode(1)
test_case.right = TreeNode(2)
test_case.right.left = TreeNode(3)
test_case.right.right = TreeNode(4)
test_case.right.right.left = TreeNode(5)
test_case.right.right.right = TreeNode(6)
test_case.right.right.left.right = TreeNode(7)
test_case.right.right.left.right.right = TreeNode(8)

s = Solution()
print(s.longestZigZag(test_case))