# 1669. Merge In Between Linked Lists
# You are given two linked lists: list1 and list2 of sizes n and m respectively.
# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
# The blue edges and nodes in the following figure indicate the result:
# Build the result list and return its head.

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        walker = list1
        idx = 0
        while idx < a - 1:
            walker = walker.next
            idx += 1
        removed = walker.next
        walker.next = list2
        while idx < b - 1:
            removed = removed.next
            idx += 1
        lastL2 = list2
        while lastL2.next:
            lastL2 = lastL2.next
        lastL2.next = removed.next
        removed.next = None
        return list1

nodeA6 = ListNode(5)
nodeA5 = ListNode(9, nodeA6)
nodeA4 = ListNode(6, nodeA5)
nodeA3 = ListNode(13, nodeA4)
nodeA2 = ListNode(1, nodeA3)
test_caseA = ListNode(10, nodeA2)

nodeB3 = ListNode(1000002)
nodeB2 = ListNode(1000001, nodeB3)
test_caseB = ListNode(1000000, nodeB2)

s = Solution()
output = s.mergeInBetween(test_caseA, 3, 4, test_caseB)

# Print list as a string
display = ""
walker = output
while walker:
    display += str(walker.val) + " => "
    walker = walker.next
print(display + "None")