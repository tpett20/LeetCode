# 129. Sum Root to Leaf Numbers
# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# - For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
# A leaf node is a node with no children.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    sum = 0
    def sumNumbers(self, node: [TreeNode], path = "") -> int:
        path += str(node.val)
        if not node.left and not node.right:
            self.sum += int(path)
        if node.left:
            self.sumNumbers(node.left, path)
        if node.right:
            self.sumNumbers(node.right, path)
        return self.sum

test_case = TreeNode(4)
test_case.left = TreeNode(9)
test_case.right = TreeNode(0)
test_case.left.left = TreeNode(5)
test_case.left.right = TreeNode(1)

s = Solution()
print(s.sumNumbers(test_case))