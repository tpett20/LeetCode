# 1325. Delete Leaves With a Given Value
# Given a binary tree root and an integer target, delete all the leaf nodes with value target.
# Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, node: Optional[TreeNode], target: int, prev=None, dir=None) -> Optional[TreeNode]:
        if node.left:
            self.removeLeafNodes(node.left, target, node, "L")
        if node.right:
            self.removeLeafNodes(node.right, target, node, "R")
        if not node.left and not node.right and node.val == target:
            if dir == "L":
                prev.left = None
            elif dir == "R":
                prev.right = None
            else:
                return None
        return node

test_case = TreeNode(2)
test_case.left = TreeNode(2)
test_case.left.left = TreeNode(2)
test_case.right = TreeNode(2)
test_case.right.left = TreeNode(2)
test_case.right.right = TreeNode(2)

s = Solution()
print(s.removeLeafNodes(test_case, 2))