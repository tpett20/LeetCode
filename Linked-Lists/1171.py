# 1171. Remove Zero Sum Consecutive Nodes from Linked List
# Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
# After doing so, return the head of the final linked list.  You may return any such answer.
# (Note that in the examples below, all sequences are serializations of ListNode objects.)

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = {}
        total = 0
        walker = head
        while walker:
            total += walker.val
            if total in d or total == 0:
                del_node = d[total].next if total in d else head
                sub_total = total
                while del_node != walker:
                    sub_total += del_node.val
                    del d[sub_total]
                    del_node = del_node.next
                if total in d:
                    d[total].next = walker.next
                else:
                    head = walker.next
            else:
                d[total] = walker
            walker = walker.next
        return head

node5 = ListNode(4)
node4 = ListNode(-3, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
test_case = ListNode(1, node2)

s = Solution()
output = s.removeZeroSumSublists(test_case)

# Print list as a string
display = ""
walker = output
while walker:
    display += str(walker.val) + " => "
    walker = walker.next
print(display + "None")