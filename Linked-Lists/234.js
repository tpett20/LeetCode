// 234. Palindrome Linked List
// Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

var isPalindrome = function(head) {
    if (!head.next) return true
    let slow = head
    let fast = head
    const firstHalf = []
    while (fast.next && fast.next.next) {
        firstHalf.push(slow.val)
        slow = slow.next
        fast = fast.next.next
    }
    if (fast.next) {
        firstHalf.push(slow.val)
    }
    slow = slow.next
    while (slow) {
        if (slow.val !== firstHalf.pop()) {
            return false
        }
        slow = slow.next
    }
    return true
};

class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

const node5 = new ListNode(1)
const node4 = new ListNode(2, node5)
const node3 = new ListNode(3, node4)
const node2 = new ListNode(2, node3)
const testCase = new ListNode(1, node2)

console.log(isPalindrome(testCase))