# 897. Increasing Order Search Tree
# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.inc_tree = TreeNode(-1)
        self.curr = self.inc_tree

    def dfs(self, node: Optional[TreeNode]):
        if node.left:
            self.dfs(node.left)
        self.curr.right = TreeNode(node.val)
        self.curr = self.curr.right
        if node.right:
            self.dfs(node.right)
        
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root)
        return self.inc_tree.right