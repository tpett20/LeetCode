// 83. Remove Duplicates from Sorted List
// Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

var deleteDuplicates = function (head) {
    if (head === null || head.next === null) return head
    let walker1 = head
    let walker2 = head.next
    while (walker2) {
        while (walker1.val === walker2?.val) {
            walker2 = walker2.next
        }
        walker1.next = walker2
        walker1 = walker1.next
        walker2 = walker2?.next
    }
    return head
};

// Definition for singly-linked list.
class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
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

let testCase = new ListNode(1)
testCase.next = new ListNode(1)
testCase.next.next = new ListNode(1)
testCase.next.next.next = new ListNode(2)
testCase.next.next.next.next = new ListNode(3)
testCase.next.next.next.next.next = new ListNode(3)
testCase.printAsArray()
let solution = deleteDuplicates(testCase)
solution.printAsArray()