# 572. Subtree of Another Tree
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_equality(node1, node2):
            if not node1 and not node2:
                return True
            if (not node1 or not node2) or (node1.val != node2.val):
                return False
            left = check_equality(node1.left, node2.left)
            right = check_equality(node1.right, node2.right)
            return left and right
        
        def traverse(node):
            if not node:
                return False
            if node.val == subRoot.val and check_equality(node, subRoot):
                return True
            left = traverse(node.left)
            right = traverse(node.right)
            return left or right
        
        return traverse(root)

test_root = TreeNode(3)
test_root.left = TreeNode(4)
test_root.left.left = TreeNode(1)
test_root.left.right = TreeNode(2)
test_root.right = TreeNode(5)

test_subRoot = TreeNode(4)
test_subRoot.left = TreeNode(1)
test_subRoot.right = TreeNode(2)

s = Solution()
print(s.isSubtree(test_root, test_subRoot))