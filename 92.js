// 92. Reverse Linked List II
/*
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
*/

// Definition for singly-linked list.
class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
    printAsArray() {
        let array = []
        let walker = this
        while (walker) {
            array.push(walker.val + ' ' + '->')
            walker = walker.next
        }
        array.push('null')
        console.log(array)
    }
}

var reverseBetween = function (head, left, right) {
    let walker = head
    let count = 1
    let revArray = []
    while (walker) {
        if (count >= left && count <= right) {
            revArray.push(walker.val)
        }
        count++
        walker = walker.next
    }
    revArray = revArray.reverse()
    count = 1
    let i = 0
    walker = head
    while (walker) {
        if (count >= left && count <= right) {
            walker.val = revArray[i]
            i++
        }
        count++
        walker = walker.next
    }
    return head
};

let head = new ListNode(1)
head.next = new ListNode(2)
head.next.next = new ListNode(3)
head.next.next.next = new ListNode(4)
head.next.next.next.next = new ListNode(5)
head.next.next.next.next.next = new ListNode(6)

reverseBetween(head, 2, 5).printAsArray()