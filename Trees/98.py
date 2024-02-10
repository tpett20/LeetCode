# 98. Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
    # The left subtree of a node contains only nodes with keys less than the node's key.
    # The right subtree of a node contains only nodes with keys greater than the node's key.
    # Both the left and right subtrees must also be binary search trees.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        node_list = []
        
        def traverse(node):
            if node.left:
                traverse(node.left)    
            node_list.append(node.val)
            if node.right:
                traverse(node.right)
        
        traverse(root)
        for i in range(1, len(node_list)):
            if node_list[i - 1] >= node_list[i]:
                return False
        return True

test_case = TreeNode(3)
test_case.left = TreeNode(1)
test_case.right = TreeNode(20)
test_case.right.left = TreeNode(15)
test_case.right.right = TreeNode(25)

s = Solution()
print(s.isValidBST(test_case))