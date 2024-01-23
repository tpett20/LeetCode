# 103. Binary Tree Zigzag Level Order Traversal
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: [TreeNode]) -> list[list[int]]:
        if not root:
            return None
        queue = [root]
        output = []
        while len(queue):
            q_len = len(queue)
            level = []
            for _ in range(q_len):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(level)
        for i in range(1, len(output), 2):
            output[i].reverse()
        return output

test_case = TreeNode(3)
test_case.left = TreeNode(9)
test_case.right = TreeNode(20)
test_case.right.left = TreeNode(15)
test_case.right.right = TreeNode(7)

s = Solution()
print(s.zigzagLevelOrder(test_case))