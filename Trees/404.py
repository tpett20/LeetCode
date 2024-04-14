# 404. Sum of Left Leaves
# Given the root of a binary tree, return the sum of all left leaves.
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, node: Optional[TreeNode]) -> int:
        left_sum = 0
        if node.left:
            if not node.left.left and not node.left.right:
                left_sum += node.left.val
            else:
                left_sum += self.sumOfLeftLeaves(node.left)
        if node.right:
            left_sum += self.sumOfLeftLeaves(node.right)
        return left_sum

test_case = TreeNode(3)
test_case.left = TreeNode(9)
test_case.right = TreeNode(20)
test_case.right.left = TreeNode(15)
test_case.right.left.left = TreeNode(15)
test_case.right.right = TreeNode(7)

s = Solution()
print(s.sumOfLeftLeaves(test_case))