// 328. Odd Even Linked List
/*
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
*/

// Definition for singly-linked list. 
class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
    append(val) {
        const newNode = new ListNode(val)
        if (this.val === null) {
            this.val = newNode
            return
        }
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
            array.push(walker.val + ' ' + '->')
            walker = walker.next
        }
        array.push('null')
        console.log(array)
    }
}

var oddEvenList = function (head) {
    if (!head || head.next === null || head.next.next === null) {
        return head
    } 
    let oddWalker = head
    let evenList = null
    let evenWalker = null
    while (oddWalker.next?.next) {
        if (!evenList) {
            evenList = oddWalker.next
            evenWalker = evenList
        } else {
            evenWalker.next = oddWalker.next
            evenWalker = evenWalker.next
        }
        oddWalker.next = oddWalker.next?.next
        oddWalker = oddWalker.next
    }
    if (evenWalker.next?.next) {
        evenWalker.next = evenWalker.next.next
    } else {
        evenWalker.next = null
    }
    oddWalker.next = evenList
    return head
};


const head = new ListNode(1)
head.append(2)
head.append(3)
head.append(4)

console.log('Input')
head.printAsArray()
let result = oddEvenList(head)
console.log('Output')
result.printAsArray()