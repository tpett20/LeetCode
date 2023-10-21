// 61. Rotate List
// Given the head of a linked list, rotate the list to the right by k places.

var rotateRight = function(head, k) {
    if (!head || !head.next || k === 0) return head
    let walker = head
    let len = 0
    while (walker) {
        len++
        walker = walker.next
    }
    k = k % len
    if (k === 0) return head

    let oldHead = head
    walker = head
    let count = 1
    let target = len - k
    while (count < target) {
        count++
        walker = walker.next
    }
    head = walker.next
    walker.next = null

    walker = head
    while (walker.next) {
        walker = walker.next
    }
    walker.next = oldHead
    return head
};

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
const result = rotateRight(testCase, k)
result.printAsArray()