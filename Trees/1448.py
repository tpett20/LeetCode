# 1448. Count Good Nodes in Binary Tree
# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, node: TreeNode, ceil = float('-inf')) -> int:
        count = 0
        if node.val >= ceil:
            ceil = node.val
            count = 1
        if node.left:
            count += self.goodNodes(node.left, ceil)
        if node.right:
            count += self.goodNodes(node.right, ceil)
        return count

test_case = TreeNode(3)
test_case.left = TreeNode(1)
test_case.right = TreeNode(4)
test_case.left.left = TreeNode(3)
test_case.right.left = TreeNode(1)
test_case.right.right = TreeNode(5)

s = Solution()
print(s.goodNodes(test_case))