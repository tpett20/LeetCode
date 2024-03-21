# 876. Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        walker = head
        while walker:
            length += 1
            walker = walker.next
        mid = length // 2 + 1
        idx = 1
        walker = head
        while idx != mid:
            walker = walker.next
            idx += 1
        return walker

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
test_case = ListNode(1, node2)

s = Solution()
midNode = s.middleNode(test_case)

# Print midNode as a string
display = ""
walker = midNode
while walker:
    display += str(walker.val) + " -> "
    walker = walker.next
print(display + "None")