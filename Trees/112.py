# 112. Path Sum
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, node: [TreeNode], target_sum: int, sum = 0) -> bool:
        if not node:
            return False
        sum += node.val
        if not node.left and not node.right:
            return sum == target_sum
        if node.left and node.left:
            return (self.hasPathSum(node.left, target_sum, sum) or 
                self.hasPathSum(node.right, target_sum, sum))
        if node.left:
            return self.hasPathSum(node.left, target_sum, sum)
        else:
            return self.hasPathSum(node.right, target_sum, sum)

test_case = TreeNode(5)
test_case.left = TreeNode(4)
test_case.left.left = TreeNode(11)
test_case.left.left.left = TreeNode(7)
test_case.left.left.right = TreeNode(2)
test_case.right = TreeNode(8)
test_case.right.left = TreeNode(13)
test_case.right.right = TreeNode(4)
test_case.right.right.right = TreeNode(1)
target = 22

s = Solution()
print(s.hasPathSum(test_case, target))