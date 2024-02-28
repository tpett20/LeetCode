# 513. Find Bottom Left Tree Value
# Given the root of a binary tree, return the leftmost value in the last row of the tree.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: [TreeNode]) -> int:
        left_val = None
        q = [root]
        while len(q):
            left_val = q[0].val
            q_len = len(q)
            for _ in range(q_len):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return left_val

test_case = TreeNode(1)
test_case.left = TreeNode(2)
test_case.right = TreeNode(3)
test_case.left.left = TreeNode(4)
test_case.right.left = TreeNode(5)
test_case.right.right = TreeNode(6)
test_case.right.left.left = TreeNode(7)

s = Solution()
print(s.findBottomLeftValue(test_case))