# 1609. Even Odd Tree
# A binary tree is named Even-Odd if it meets the following conditions:
    # The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
    # For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
    # For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
# Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: [TreeNode]) -> bool:
        q = [root]
        even_lvl = True
        while len(q):
            q_len = len(q)
            last_val = 0 if even_lvl else float('inf')
            for _ in range(q_len):
                node = q.pop(0)
                even_val = True if (node.val % 2 == 0) else False
                if even_lvl:
                    if even_val or node.val <= last_val:
                        return False
                else:
                    if not even_val or node.val >= last_val:
                        return False
                last_val = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            even_lvl = not even_lvl
        return True

test_case = TreeNode(5)
test_case.left = TreeNode(4)
test_case.right = TreeNode(2)
test_case.left.left = TreeNode(3)
test_case.left.right = TreeNode(3)
test_case.right.left = TreeNode(7)

s = Solution()
print(s.isEvenOddTree(test_case))