# 257. Binary Tree Paths
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode], path: str="") -> List[str]:
        path = f"{path}->{root.val}" if path else str(root.val)
        paths = []
        if not root.left and not root.right:
            return [path]
        if root.left:
            paths.extend(self.binaryTreePaths(root.left, path))
        if root.right:
            paths.extend(self.binaryTreePaths(root.right, path))
        return paths