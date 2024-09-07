// 3217. Delete Nodes From Linked List Present in Array
// You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

var modifiedList = function(nums, head) {
    const ref = new Set(nums)
    const fakeHead = new ListNode(0, head)
    let pre = fakeHead
    let curr = head
    while (curr) {
        if (ref.has(curr.val)) {
            pre.next = curr.next
        } else {
            pre = curr
        }
        curr = curr.next
    }
    return fakeHead.next
};

class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

const node5 = new ListNode(5)
const node4 = new ListNode(4, node5)
const node3 = new ListNode(3, node4)
const node2 = new ListNode(2, node3)
const testCase = new ListNode(1, node2)

const output = modifiedList([1, 2, 3], testCase)

// Display list as a string
let display = ""
let walker = output
while (walker) {
    display += walker.val.toString() + " => "
    walker = walker.next
}
console.log(display + "null")