# 1367. Linked List in Binary Tree
# Given a binary tree root and a linked list with head as the first node. 
# Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.
# In this context downward path means a path that starts at some node and goes downwards.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def check_path(t_node, l_node):
            if not l_node:
                return True
            if not t_node or (t_node.val != l_node.val):
                return False
            return check_path(t_node.left, l_node.next) or check_path(t_node.right, l_node.next)
        
        def dfs(t_node):
            if not t_node:
                return False
            if t_node.val == head.val and check_path(t_node, head) == True:
                return True
            return dfs(t_node.left) or dfs(t_node.right)
        
        return dfs(root)

test_list = ListNode(1)
test_list.next = ListNode(2)
test_list.next.next = ListNode(3)

test_tree = TreeNode(1)
test_tree.left = TreeNode(2)
test_tree.right = TreeNode(99)
test_tree.left.left = TreeNode(99)
test_tree.left.right = TreeNode(3)

s = Solution()
print(s.isSubPath(test_list, test_tree))