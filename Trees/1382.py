# 1382. Balance a Binary Search Tree
# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:    
    def dfs(self, node):
        arr = []
        if node.left:
            arr += self.dfs(node.left)
        arr.append(node.val)
        if node.right:
            arr += self.dfs(node.right)
        return arr
    
    def construct_tree(self, arr):
        if not arr:
            return None
        flr = 0
        ceil = len(arr) - 1
        mid = (flr + ceil) // 2
        node = TreeNode(arr[mid])
        node.left = self.construct_tree(arr[flr:mid])
        node.right = self.construct_tree(arr[mid + 1:ceil+1])
        return node
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        node_vals = self.dfs(root)
        return self.construct_tree(node_vals)

test_case = TreeNode(1)
test_case.right = TreeNode(2)
test_case.right.right = TreeNode(3)
test_case.right.right.right = TreeNode(4)

s = Solution()
output = s.balanceBST(test_case)
print("Head:", output.val)
print("Left:", output.left.val)
print("Right:", output.right.val)
print("Right, Right:", output.right.val)