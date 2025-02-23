# 1028. Recover a Tree From Preorder Traversal
# We run a preorder depth-first search (DFS) on the root of a binary tree.
# At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.
# If a node has only one child, that child is guaranteed to be the left child.
# Given the output traversal of this traversal, recover the tree and return its root.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, arr):
        i = 0
        depth, val = arr[i]
        i += 1
        node = TreeNode(val)
        left = None
        right = None
        while i < len(arr):
            if arr[i][0] <= depth or (left and right):
                break
            if not left and arr[i][0] == depth + 1:
                left = i
            elif arr[i][0] == depth + 1:
                right = i
            i += 1
        if left and right:
            node.left = self.dfs(arr[left:right])
        elif left:
            node.left = self.dfs(arr[left:])
        if right:
            node.right = self.dfs(arr[right:])
        return node
        
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0
        trav_arr = []
        while i < len(traversal):
            depth = 0
            while traversal[i] == "-":
                depth += 1
                i += 1
            val = ""
            while i < len(traversal) and traversal[i] != "-":
                val += traversal[i]
                i += 1
            val = int(val)
            trav_arr.append((depth, val))
        return self.dfs(trav_arr)