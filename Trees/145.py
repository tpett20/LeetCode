from typing import Optional, List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, node: Optional[TreeNode]) -> List[int]:
        visited = []
        if not node:
            return visited
        visited += self.postorderTraversal(node.left)
        visited += self.postorderTraversal(node.right)
        visited.append(node.val)
        return visited

test_case = TreeNode(4)
test_case.left = TreeNode(9)
test_case.right = TreeNode(0)
test_case.left.left = TreeNode(5)
test_case.left.right = TreeNode(1)

s = Solution()
print(s.postorderTraversal(test_case))