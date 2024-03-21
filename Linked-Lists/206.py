# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        while head.next:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        head.next = prev
        return head

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
test_case = ListNode(1, node2)

s = Solution()
output = s.reverseList(test_case)

# Print list as a string
display = ""
walker = output
while walker:
    display += str(walker.val) + " => "
    walker = walker.next
print(display + "None")