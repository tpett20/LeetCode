# 1026. Maximum Difference Between Node and Ancestor
# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, node: [TreeNode], low = 100001, high = -1) -> int:
        low_diff = node.val - low
        high_diff = high - node.val
        low = min(node.val, low)
        high = max(node.val, high)
        left_diff = right_diff = 0
        if node.left:
            left_diff = self.maxAncestorDiff(node.left, low, high)
        if node.right:
            right_diff = self.maxAncestorDiff(node.right, low, high)
        return max(low_diff, high_diff, left_diff, right_diff)

test_case = TreeNode(8)
test_case.left = TreeNode(3)
test_case.left.left = TreeNode(1)
test_case.left.right = TreeNode(6)
test_case.left.right.left = TreeNode(4)
test_case.left.right.right = TreeNode(7)
test_case.right = TreeNode(10)
test_case.right.right = TreeNode(14)
test_case.right.right.left = TreeNode(13)

s = Solution()
print(s.maxAncestorDiff(test_case))