# 2487. Remove Nodes From Linked List 
# You are given the head of a linked list.
# Remove every node which has a node with a greater value anywhere to the right side of it.
# Return the head of the modified linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        max_val = 0
        for i in range(len(vals) - 1, -1, -1):
            val = vals[i]
            vals[i] = max_val
            max_val = max(max_val, val)
        fake_head = ListNode(next=head)
        prev = fake_head
        curr = head
        i = 0
        while curr:
            right_max = vals[i]
            if curr.val < right_max:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
            i += 1
        return fake_head.next

node5 = ListNode(8)
node4 = ListNode(3, node5)
node3 = ListNode(13, node4)
node2 = ListNode(2, node3)
test_case = ListNode(5, node2)

s = Solution()
output = s.removeNodes(test_case)

# Print list as a string
display = ""
walker = output
while walker:
    display += str(walker.val) + " => "
    walker = walker.next
print(display + "None")