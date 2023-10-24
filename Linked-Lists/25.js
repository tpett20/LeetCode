// 25. Reverse Nodes in k-Group
/*
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
*/

var reverseKGroup = function(head, k) {
    if (k === 1 || !head.next) return head
    let prev = null
    let walker = head
    while (walker) {
        let revHead = walker
        let count = 0
        while (walker && count < k - 1) {
            count++
            walker = walker.next
        }
        if (!walker || count < k - 1) {
            return head
        }
        let currNode = revHead
        let preNode = prev
        let nextNode
        for (let i = 0; i < k; i++) {
            nextNode = currNode.next
            currNode.next = preNode
            preNode = currNode
            currNode = nextNode
        }
        if (prev) prev.next = preNode
        else head = preNode
        prev = revHead
        revHead.next = currNode
        walker = currNode
    }
    return head
};

class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
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
const k = 2

console.log(`INPUT, k = ${k}`)
testCase.printAsArray()
console.log("OUTPUT")
const result = reverseKGroup(testCase, k)
result.printAsArray()