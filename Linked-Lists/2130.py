# 2130. Maximum Twin Sum of a Linked List
# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
# - For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

class Solution:
    def pairSum(self, head) -> int:
        prev = head
        walker = prev.next
        length = 1
        while walker:
            length += 1
            walker.prev = prev
            prev = walker
            walker = walker.next
        walker = head
        back_walker = prev
        max_sum = walker.val + back_walker.val
        count = 2
        while count < length:
            walker = walker.next
            back_walker = back_walker.prev
            sum = walker.val + back_walker.val
            max_sum = max(sum, max_sum)
            count += 2
        return max_sum 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"

    def append(self, val):
        newNode = ListNode(val)
        walker = self
        while walker.next:
            walker = walker.next
        walker.next = newNode

testCase = ListNode(5)
testCase.append(4)
testCase.append(2)
testCase.append(1)
print('INPUT')
print(testCase)

s = Solution()
result = s.pairSum(testCase)
print('OUTPUT')
print(result)