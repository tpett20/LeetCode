# 100. Same Tree
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:
        def traverse(node):
            if not node:
                return None
            arr = [node.val]
            if node.left or node.right:
                if node.left:
                    arr += (traverse(node.left))
                else:
                    arr.append(None)
                if node.right:
                    arr += (traverse(node.right))
                else:
                    arr.append(None)
            return arr
        
        return traverse(p) == traverse(q)

test_case1 = TreeNode(1)
test_case1.left = TreeNode(2)
test_case1.left.left = TreeNode(4)
test_case1.right = TreeNode(3)

test_case2 = TreeNode(1)
test_case2.left = TreeNode(2)
test_case2.left.right = TreeNode(4)
test_case2.right = TreeNode(3)

s = Solution()
print(s.isSameTree(test_case1, test_case2))