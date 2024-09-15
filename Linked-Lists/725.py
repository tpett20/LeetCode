# 725. Split Linked List in Parts
# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
# Return an array of the k parts.

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        list_len = 0
        walker = head
        while walker:
            list_len += 1
            walker = walker.next
        base_size = list_len // k
        r = list_len % k
        walker = head
        parts = []
        for i in range(k):
            parts.append(walker)
            size = base_size + 1 if (i < r) else base_size
            for _ in range(size - 1):
                if walker:
                    walker = walker.next
            if walker:
                prev = walker
                walker = walker.next
                prev.next = None
        return parts

test_case = ListNode(1)
test_case.next = ListNode(2)
test_case.next.next = ListNode(3)
test_case.next.next.next = ListNode(4)
test_case.next.next.next.next = ListNode(5)

s = Solution()
output = s.splitListToParts(test_case, 3)
for part in output:
    # Print each LinkedList part as a string
    display = ""
    walker = part
    while walker:
        display += str(walker.val) + " -> "
        walker = walker.next
    print(display + "None")