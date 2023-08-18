# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

def isPalindrome(head):
    if not head.next: return True
    arr = []
    walker = head
    while walker:
        arr.append(walker.val)
        walker = walker.next
    walker = head
    for i in range(len(arr)-1, -1, -1):
        if walker.val != arr[i]:
            return False
        walker = walker.next
    return True

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list = ListNode(2)
list.next = ListNode(1)
list.next.next = ListNode(2)

print(isPalindrome(list))