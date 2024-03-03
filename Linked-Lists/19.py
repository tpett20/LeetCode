# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        walker = head
        length = 0
        while walker:
            walker = walker.next
            length += 1
        if length == n:
            return head.next
        trgt_idx = length - n
        idx = 1
        walker = head
        while idx != trgt_idx:
            walker = walker.next
            idx += 1
        removed_node = walker.next
        new_next = removed_node.next
        walker.next = new_next
        return head

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
test_case = ListNode(1, node2)

s = Solution()
output = s.removeNthFromEnd(test_case, 2)

# Print new, modified list as a string
display = ""
walker = output
while walker:
    display += str(walker.val) + " -> "
    walker = walker.next
print(display + "None")