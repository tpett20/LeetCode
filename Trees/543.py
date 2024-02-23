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
        leaf_paths = [""]
        
        def traverse(node, path = ""):
            if node.left:
                traverse(node.left, path + "L")
            if node.right:
                traverse(node.right, path + "R")
            if not node.left and not node.right:
                leaf_paths.append(path)

        def compare_paths(path1, path2):
            diff = i = 0
            min_len = min(len(path1), len(path2))
            while i < min_len and path1[i] == path2[i]:
                i += 1
            diff += (len(path1) - i) + (len(path2) - i)
            return diff
        
        traverse(root)
        diam = 0
        for i in range(len(leaf_paths) - 1):
            for j in range(i + 1, len(leaf_paths)):
                diam = max(diam, compare_paths(leaf_paths[i], leaf_paths[j]))
        return diam

test_case = TreeNode(1)
test_case.left = TreeNode(2)
test_case.right = TreeNode(3)
test_case.left.left = TreeNode(4)
test_case.left.right = TreeNode(5)

s = Solution()
print(s.diameterOfBinaryTree(test_case))