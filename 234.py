# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    if not head.next: return True
    string = ''
    walker = head
    while walker:
        string += str(walker.val)
        walker = walker.next
    if string == string[::-1]:
        return True
    return False


list = ListNode(2)
list.next = ListNode(2)
list.next.next = ListNode(1)

print(isPalindrome(list))