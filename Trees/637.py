# 637. Average of Levels in Binary Tree
# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: [TreeNode]) -> list[float]:
        averages = []
        if not root: 
            return averages
        node = root
        queue = [root]
        while len(queue):
            q_len = len(queue)
            sum = 0
            for _ in range(q_len):
                node = queue.pop(0)
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            averages.append(sum / q_len)
        return averages

test_case = TreeNode(3)
test_case.left = TreeNode(9)
test_case.right = TreeNode(20)
test_case.right.left = TreeNode(15)
test_case.right.right = TreeNode(7)

s = Solution()
print(s.averageOfLevels(test_case))