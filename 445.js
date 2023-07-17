// 445. Add Two Numbers II
/*
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
*/

var addTwoNumbers = function (l1, l2) {
    let walker1 = l1
    let num1 = ''
    let walker2 = l2
    let num2 = ''
    while (walker1 && walker2) {
        num1 += walker1.val
        num2 += walker2.val
        walker1 = walker1.next
        walker2 = walker2.next
    }
    while (walker1) {
        num1 += walker1.val
        walker1 = walker1.next
    }
    while (walker2) {
        num2 += walker2.val
        walker2 = walker2.next
    }
    let sum = parseInt(num1) + parseInt(num2)
    sum = sum.toString()
    let l3 = new ListNode(parseInt(sum[0]))
    let walker3 = l3
    let i = 1
    while (i < sum.length) {
        walker3.next = new ListNode(parseInt(sum[i]))
        walker3 = walker3.next
        i++
    }
    return l3
};

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

const l1 = new ListNode(1)
l1.append(1)
l1.append(1)
l1.printAsArray()

const l2 = new ListNode(1)
l2.append(2)
l2.append(2)
l2.append(2)
l2.printAsArray()

const solution = addTwoNumbers(l1, l2)
solution.printAsArray()