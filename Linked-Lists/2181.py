# 2181. Merge Nodes in Between Zeros
# You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.
# For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
# Return the head of the modified linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        walker = head.next
        total = 0
        while walker:
            if walker.val == 0:
                walker.val = total
                total = 0
                prev.next = walker
                prev = walker
            else:
                total += walker.val
            walker = walker.next
        return head.next

node8 = ListNode(0)
node7 = ListNode(2, node8)
node6 = ListNode(2, node7)
node5 = ListNode(0, node6)
node4 = ListNode(3, node5)
node3 = ListNode(0, node4)
node2 = ListNode(1, node3)
test_case = ListNode(0, node2)

s = Solution()
output = s.mergeNodes(test_case)

# Print output list as a string
display = ""
walker = output
while walker:
    display += str(walker.val) + " => "
    walker = walker.next
print(display + "None")