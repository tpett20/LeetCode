# 2641. Cousins in Binary Tree II
# Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.
# Two nodes of a binary tree are cousins if they have the same depth with different parents.
# Return the root of the modified tree.
# Note that the depth of a node is the number of edges in the path from the root node to it.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(node):
            q = [[node, 0]]
            while len(q):
                q_len = len(q)
                row_sum = 0
                for i in range(q_len):
                    curr = q[i][0]
                    row_sum += curr.val
                    if curr.left and curr.right:
                        q.append([curr.left, curr.right.val])
                        q.append([curr.right, curr.left.val])
                    else:
                        if curr.left:
                            q.append([curr.left, 0])
                        if curr.right:
                            q.append([curr.right, 0])
                for _ in range(q_len):
                    curr, sibling_val = q.pop(0)
                    curr.val = row_sum - (curr.val + sibling_val)

        bfs(root)
        return root