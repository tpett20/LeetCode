// 206. Reverse Linked List
// Given the head of a singly linked list, reverse the list, and return the reversed list.

var reverseList = function(head) {
    if (head === null || head.next === null) return head
    let walker = head
    let last
    while (walker) {
        walker.prev = walker.next
        if (last) {
            walker.next = last
            last = last.prev
        } else {
            walker.next = null
            last = walker
        }
        if (walker.prev !== null) {
            walker = walker.prev
        } else {
            return walker
        }
    }
};

class ListNode {
    constructor(val, next) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
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

const testCase = new ListNode(1)
testCase.append(2)
testCase.append(3)
testCase.append(4)
testCase.append(5)
testCase.printAsArray()
reverseList(testCase).printAsArray()