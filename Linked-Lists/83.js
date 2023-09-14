// 83. Remove Duplicates from Sorted List
// Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

var deleteDuplicates = function(head) {
    if (!head || !head.next) return head  
    let walker1 = head
    let walker2 = head.next
    while (walker1) {
        while (walker2 && walker1.val === walker2.val) {
            walker2 = walker2.next
        }
        walker1.next = walker2
        walker1 = walker1.next
    }
    return head
};

// Definition for singly-linked list.
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
        const arr = []
        let walker = this
        while (walker) {
            arr.push(`${walker.val} ->`)
            walker = walker.next
        }
        arr.push('null')
        console.log(arr)
    }
}

const testCase = new ListNode(1)
testCase.append(1)
testCase.append(1)
testCase.append(2)
testCase.append(3)
testCase.append(3)
testCase.printAsArray()
const solution = deleteDuplicates(testCase)
solution.printAsArray()