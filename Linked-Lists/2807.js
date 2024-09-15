// 2807. Insert Greatest Common Divisors in Linked List
/*
Given the head of a linked list head, in which each node contains an integer value.
Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
Return the linked list after insertion.
The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
*/

var insertGreatestCommonDivisors = function(head) {
    function getGCD(num1, num2) {
        let i = (num1 < num2) ? num1 : num2
        while (num1 % i !== 0 || num2 % i !== 0) {
            i--
        }
        return i
    }

    let walker = head
    while (walker.next) {
        const midVal = getGCD(walker.val, walker.next.val)
        const nxt = walker.next
        walker.next = new ListNode(midVal, nxt)
        walker = nxt
    }
    return head
};

class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

const node4 = new ListNode(3)
const node3 = new ListNode(10, node4)
const node2 = new ListNode(6, node3)
const testCase = new ListNode(18, node2)

const output = insertGreatestCommonDivisors(testCase)

// Display list as a string
let display = ""
let walker = output
while (walker) {
    display += walker.val.toString() + " => "
    walker = walker.next
}
console.log(display + "null")