# 1290. Convert Binary Number in a Linked List to Integer
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
# The most significant bit is at the head of the linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary = ""
        curr = head
        while curr:
            binary += str(curr.val)
            curr = curr.next
        return int(binary, 2)

node3 = ListNode(1)
node2 = ListNode(0, node3)
test_case = ListNode(1, node2)

s = Solution()
print(s.getDecimalValue(test_case))