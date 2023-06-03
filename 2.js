// 2. Add Two Numbers
/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
*/

// Definition for singly-linked list. 
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

var addTwoNumbers = function(l1, l2) {
    let l3 = new ListNode()
    let walker1 = l1
    let walker2 = l2
    let walker3 = l3
    while (walker1 || walker2) {
        let sum = walker3.val
        if (walker1 && walker2) {
            sum += (walker1.val + walker2.val)
        }
        else if (walker1) sum += walker1.val
        else sum += walker2.val
        if (sum < 10) {
            walker3.val = sum
            if (walker1?.next || walker2?.next) {
                walker3.next = new ListNode()
            }
        } else {
            walker3.val = sum % 10
            walker3.next = new ListNode(1)
        }
        walker1 = walker1?.next
        walker2 = walker2?.next
        walker3 = walker3.next
    }
    return l3
};


const l1 = new ListNode(9)
l1.append(9)
l1.append(9)

const l2 = new ListNode(1)

let result = addTwoNumbers(l1, l2)
result.printAsArray()