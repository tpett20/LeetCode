// 725. Split Linked List in Parts
/*
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
Return an array of the k parts.
*/

var splitListToParts = function(head, k) {
    if (k === 1) return [head]
    let walker = head
    let length = 0
    while (walker) {
        length++
        walker = walker.next
    }
    let split = Math.floor(length / k)
    let remainder = length % k
    const output = []
    walker = head
    while (output.length < k) {
        let count = 0
        let newHead = null
        if (split) {
            newHead = walker
            count = 1
        }
        while (count < split) {
            walker = walker.next
            count++
        }
        if (remainder && count > 0) {
            walker = walker.next
            remainder--
        } else if (remainder) {
            newHead = walker
            remainder--
        }
        if (walker) {
            let cachedNode = walker.next
            walker.next = null
            output.push(newHead)
            walker = cachedNode
        } else output.push(newHead)
    }
    return output
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
const k = 3

console.log(`INPUT, k = ${k}`)
testCase.printAsArray()
console.log("OUTPUT Array [")
const result = splitListToParts(testCase, k)
for (let node of result) {
    node.printAsArray()
}
console.log(']')