# 110. Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(node):
            left_depth = 0
            right_depth = 0
            if node.left:
                left_depth = traverse(node.left) + 1
            if node.right:
                right_depth = traverse(node.right) + 1
            if abs(left_depth - right_depth) > 1:
                self.balanced = False
            return max(left_depth, right_depth)
        
        self.balanced = True
        if root:
            traverse(root)
        return self.balanced

test_case = TreeNode(3)
test_case.left = TreeNode(9)
test_case.right = TreeNode(20)
test_case.right.left = TreeNode(15)
test_case.right.right = TreeNode(7)

s = Solution()
print(s.isBalanced(test_case))