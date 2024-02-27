# 543. Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: [TreeNode]) -> int:
        max_diff = 0
        
        def traverse(node):
            left = traverse(node.left) if node.left else 0
            right = traverse(node.right) if node.right else 0
            diff = left + right
            nonlocal max_diff
            max_diff = max(diff, max_diff)
            return max(left, right) + 1
        
        traverse(root)
        return max_diff

test_case = TreeNode(1)
test_case.left = TreeNode(2)
test_case.right = TreeNode(3)
test_case.left.left = TreeNode(4)
test_case.left.right = TreeNode(5)

s = Solution()
print(s.diameterOfBinaryTree(test_case))