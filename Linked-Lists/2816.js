// 2816. Double a Number Represented as a Linked List
// You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.
// Return the head of the linked list after doubling it.

var doubleIt = function(head) {
    if (head.val === 0) return head
    const numArr = []
    let walker = head
    while (walker) {
        numArr.push(walker.val)
        walker = walker.next
    }
    let r = 0
    for (let i = numArr.length - 1; i >= 0; i--) {
        const dbl = numArr[i] * 2 + r
        r = (dbl >= 10) ? 1 : 0
        numArr[i] = dbl % 10
    }
    walker = head
    for (let i = 0; i < numArr.length; i++) {
        walker.val = numArr[i]
        walker = walker.next
    }
    return r ? new ListNode(1, head) : head
};

class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

const node3 = new ListNode(9)
const node2 = new ListNode(8, node3)
const testCase = new ListNode(1, node2)

const output = doubleIt(testCase)

// Display list as a string
let display = ""
let walker = output
while (walker) {
    display += walker.val.toString() + " => "
    walker = walker.next
}
console.log(display + "null")