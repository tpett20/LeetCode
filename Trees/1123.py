# 1123. Lowest Common Ancestor of Deepest Leaves
# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.
# Recall that:
    # The node of a binary tree is a leaf if and only if it has no children
    # The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
    # The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_depth = 0
        self.lca = None
    
    def dfs(self, node: Optional[TreeNode], depth: int) -> int:
        if not node:
            return depth
        depth += 1
        if depth > self.max_depth:
            self.lca = node
            self.max_depth = depth
        left_max_depth = self.dfs(node.left, depth)
        right_max_depth = self.dfs(node.right, depth)
        if (node.left and node.right and 
            left_max_depth == right_max_depth == self.max_depth):
            self.lca = node
        return max(left_max_depth, right_max_depth)
    
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root, 0)
        return self.lca