# 1110. Delete Nodes And Return Forest
# Given the root of a binary tree, each node in the tree has a distinct value.
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
# Return the roots of the trees in the remaining forest. You may return the result in any order.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete_set = set(to_delete)
        output = []
        if not root:
            return output
        if root.val not in delete_set:
            output.append(root)
        
        def dfs(node):
            if node.val in delete_set:
                if node.left and node.left.val not in delete_set:
                    output.append(node.left)
                if node.right and node.right.val not in delete_set:
                    output.append(node.right)
            if node.left:
                dfs(node.left)
                if node.left.val in delete_set:
                    node.left = None
            if node.right:
                dfs(node.right)
                if node.right.val in delete_set:
                    node.right = None
        
        dfs(root)
        return output