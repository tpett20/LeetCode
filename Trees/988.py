# 988. Smallest String Starting From Leaf
# You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.
# Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
# As a reminder, any shorter prefix of a string is lexicographically smaller.
    # For example, "ab" is lexicographically smaller than "aba".
# A leaf of a node is a node that has no children.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest = "~"
        def dfs(node, string):
            nonlocal smallest
            string = chr(node.val + 97) + string
            if not node.left and not node.right:
                if string < smallest:
                    smallest = string
                return
            if node.left:
                dfs(node.left, string)
            if node.right:
                dfs(node.right, string)
        
        dfs(root, "")
        return smallest

test_case = TreeNode(25)
test_case.left = TreeNode(1)
test_case.left.left = TreeNode(1)
test_case.left.right = TreeNode(3)
test_case.right = TreeNode(3)
test_case.right.left = TreeNode(0)
test_case.right.right = TreeNode(2)

s = Solution()
print(s.smallestFromLeaf(test_case))