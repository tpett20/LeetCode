# 117. Populating Next Right Pointers in Each Node II
# Given a binary tree
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = [root]
        while len(q):
            q_len = len(q)
            nxt = None
            for _ in range(q_len):
                node = q.pop(0)
                node.next = nxt
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                nxt = node
        return root

test_case = Node(1)
test_case.left = Node(2)
test_case.right = Node(3)
test_case.left.left = Node(4)
test_case.left.right = Node(5)
test_case.right.right = Node(7)

s = Solution()
s.connect(test_case)

# Print each node's value and next pointer
def display_result(root):
    q = [root]
    output = ""
    while len(q):
        q_len = len(q)
        for _ in range(q_len):
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if node.next:
                string = f"{node.val} => {node.next.val}, "
            else:
                string = f"{node.val} => {None}, "
            output += string
    return output[:-2]

print(display_result(test_case))