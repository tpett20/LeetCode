# 2095. Delete the Middle Node of a Linked List
# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.        

def deleteMiddle(head):
    walker = head
    n = 0
    while walker:
        n += 1
        walker = walker.next
    if n == 1: 
        return
    middle = n // 2
    walker = head
    count = 0
    while walker: 
        if count + 1 == middle: 
            walker.next = walker.next.next
            return head
        count += 1
        walker = walker.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print_as_list(self): 
        walker = self
        list = []
        while walker:
            list.append(f"{walker.val} ->")
            walker = walker.next
        list.append("None")
        print(list)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print('Input:')
head.print_as_list()
head = deleteMiddle(head)
print('Output:')
head.print_as_list()