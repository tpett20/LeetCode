# 114. Flatten Binary Tree to Linked List
# Given the root of a binary tree, flatten the tree into a "linked list":
# - The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# - The "linked list" should be in the same order as a pre-order traversal of the binary tree.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: [TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        node = root
        while node.right or node.left:
            if node.right:
                stack.append(node.right)
                node.right = None
            if node.left:
                node.right = node.left
                node.left = None
                node = node.right
            while len(stack) and not node.left and not node.right:
                node.right = stack.pop()
                node = node.right

test_case = TreeNode(1)
test_case.left = TreeNode(2)
test_case.left.left = TreeNode(3)
test_case.left.right = TreeNode(4)
test_case.right = TreeNode(5)
test_case.right.right = TreeNode(6)

s = Solution()
s.flatten(test_case)
test_node = test_case
while test_node:
    print(f"node.val: {test_node.val}, left: {test_node.left}, right: next line")
    test_node = test_node.right