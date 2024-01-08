# 938. Range Sum of BST
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, node: [TreeNode], low: int, high: int, sum = 0) -> int:
        if node.val >= low and node.val <= high:
            sum += node.val
        if node.left:
            sum += self.rangeSumBST(node.left, low, high)
        if node.right:
            sum += self.rangeSumBST(node.right, low, high)
        return sum

test_case = TreeNode(10)
test_case.left = TreeNode(5)
test_case.right = TreeNode(15)
test_case.left.left = TreeNode(3)
test_case.left.right = TreeNode(7)
test_case.right.right = TreeNode(18)
l = 7
h = 15

s = Solution()
print(s.rangeSumBST(test_case, l, h))