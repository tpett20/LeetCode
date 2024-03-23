# 143. Reorder List
# You are given the head of a singly linked-list. The list can be represented as:
    # L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
    # L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        back = prev
        front = head
        while back:
            f_nxt = front.next
            b_nxt = back.next
            front.next = back
            back.next = f_nxt
            front = f_nxt
            back = b_nxt

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
test_case = ListNode(1, node2)

# Print original list as a string
print("BEFORE")
display = ""
walker = test_case
while walker:
    display += str(walker.val) + " -> "
    walker = walker.next
print(display + "None")

s = Solution()
s.reorderList(test_case)

# Print modified list as a string
print("AFTER")
display = ""
walker = test_case
while walker:
    display += str(walker.val) + " -> "
    walker = walker.next
print(display + "None")