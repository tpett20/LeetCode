# 2331. Evaluate Boolean Binary Tree
# You are given the root of a full binary tree with the following properties:
    # Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
    # Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
# The evaluation of a node is as follows:
    # If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
    # Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
# Return the boolean result of evaluating the root node.
# A full binary tree is a binary tree where each node has either 0 or 2 children.
# A leaf node is a node that has zero children.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, node: Optional[TreeNode]) -> bool:
        if node.val > 1:
            lt = self.evaluateTree(node.left)
            rt = self.evaluateTree(node.right)
            if node.val == 2:
                return lt or rt
            else:
                return lt and rt
        return not not node.val

test_case = TreeNode(2)
test_case.left = TreeNode(1)
test_case.right = TreeNode(3)
test_case.right.left = TreeNode(0)
test_case.right.right = TreeNode(1)

s = Solution()
print(s.evaluateTree(test_case))