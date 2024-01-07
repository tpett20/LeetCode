# 236. Lowest Common Ancestor of a Binary Tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    p_path = ""
    q_path = ""
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(node, p, q, path = ""):
            if node.val == p.val:
                self.p_path = path
            elif node.val == q.val:
                self.q_path = path
            if self.p_path and self.q_path:
                return
            if node.left:
                traverse(node.left, p, q, path + "L")
            if node.right:
                traverse(node.right, p, q, path + "R")
        
        traverse(root, p, q)
        i = 0
        node = root
        while (i < len(self.p_path) and i < len(self.q_path) and 
                self.p_path[i] == self.q_path[i]):
            node = node.left if (self.p_path[i] == "L") else node.right
            i += 1
        return node

test_case = TreeNode(3)
test_case.left = TreeNode(5)
test_case.right = TreeNode(1)
test_case.left.left = TreeNode(6)
test_case.left.right = TreeNode(2)
test_case.left.right.left = TreeNode(7)
test_case.left.right.right = TreeNode(4)
test_case.right.left = TreeNode(0)
test_case.right.right = TreeNode(8)
p_node = test_case.left # val = 5
q_node = test_case.left.right.right # val = 4

s = Solution()
LCA = s.lowestCommonAncestor(test_case, p_node, q_node)
print(LCA.val)