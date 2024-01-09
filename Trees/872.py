# 872. Leaf-Similar Trees
# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: [TreeNode], root2: [TreeNode]) -> bool:
        def traverse(node):
            leaves = []
            if not node.left and not node.right:
                leaves.append(node.val)
            else:
                if node.left:
                    leaves += traverse(node.left)
                if node.right:
                    leaves += traverse(node.right)
            return leaves
        
        lvs1 = traverse(root1)
        lvs2 = traverse(root2)
        if len(lvs1) != len(lvs2):
            return False
        for i in range(len(lvs1)):
            if lvs1[i] != lvs2[i]:
                return False
        return True

testcase1 = TreeNode(3)
testcase1.left = TreeNode(5)
testcase1.right = TreeNode(1)
testcase1.left.left = TreeNode(6)
testcase1.left.right = TreeNode(2)
testcase1.left.right.left = TreeNode(7)
testcase1.left.right.right = TreeNode(4)
testcase1.right.left = TreeNode(9)
testcase1.right.right = TreeNode(8)

testcase2 = TreeNode(3)
testcase2.left = TreeNode(5)
testcase2.right = TreeNode(1)
testcase2.left.left = TreeNode(6)
testcase2.left.right = TreeNode(7)
testcase2.right.left = TreeNode(4)
testcase2.right.right = TreeNode(2)
testcase2.right.right.left = TreeNode(9)
testcase2.right.right.right = TreeNode(8)

s = Solution()
print(s.leafSimilar(testcase1, testcase2))