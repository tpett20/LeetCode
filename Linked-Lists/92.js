// 92. Reverse Linked List II
// Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

var reverseBetween = function(head, left, right) {
    if (left === right) return head
    let walker = head
    let count = 1
    let lastTrueNode
    while (count < left) {
        lastTrueNode = walker
        walker = walker.next
        count++
    }
    let lastRevNode = walker
    let nextRevNode = walker
    while (count <= right) {
        walker.prev = walker.next
        walker.next = nextRevNode
        nextRevNode = walker
        walker = walker.prev
        count++
    }
    if (lastTrueNode) {
        lastTrueNode.next = nextRevNode 
    } else {
        head = nextRevNode
    }
    lastRevNode.next = walker
    return head
};

// Definition for singly-linked list.
class ListNode {
    constructor(val, next) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
    append(val) {
        const newNode = new ListNode(val)
        let walker = this
        while (walker.next) {
            walker = walker.next
        }
        walker.next = newNode
    }
    printAsArray() {
        let array = []
        let walker = this
        while (walker) {
            array.push(walker.val + ' ->')
            walker = walker.next
        }
        array.push('null')
        console.log(array)
    }
}

const testCase = new ListNode(1)
testCase.append(2)
testCase.append(3)
testCase.append(4)
testCase.append(5)
testCase.append(6)

const result = reverseBetween(testCase, 2, 5)
result.printAsArray()

// Using an Array to Reverse Order
/*
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
*/