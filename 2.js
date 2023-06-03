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
    let arr1 = []
    let arr2 = []
    let walker1 = l1
    let walker2 = l2
    while (walker1) {
        arr1.push(walker1.val)
        walker1 = walker1.next
    }
    while (walker2) {
        arr2.push(walker2.val)
        walker2 = walker2.next
    }
    console.log(arr1, arr2)
    arr1.reverse()
    arr2.reverse()
    let str1 = ""
    let str2 = ""
    arr1.forEach(char => str1 += char)
    arr2.forEach(char => str2 += char)
    console.log(str1, str2)
    str1 = parseInt(str1)
    str2 = parseInt(str2)
    console.log(str1, str2)
    let sum = str1 + str2
    console.log(sum)
    sum = sum.toString()
    console.log(sum)
    let revSum = ''
    for (let i = sum.length - 1; i >= 0; i--) {
        revSum += sum[i]
    }
    let l3 = new ListNode(revSum[0])
    let walker3 = l3
    for (let i = 1; i < revSum.length; i++) {
        walker3.next = new ListNode(revSum[i])
        walker3 = walker3.next
    }
    return l3
};


const l1 = new ListNode(0)
l1.next = new ListNode(0)
l1.next.next = new ListNode(0)
l1.next.next.next = new ListNode(2)

const l2 = new ListNode(0)
l2.next = new ListNode(0)
l2.next.next = new ListNode(1)

let result = addTwoNumbers(l1, l2)
result.printAsArray()

// Bad Testcase: 
// l1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
// l2 = [5,6,4]
// Output = [0,3,NaN,NaN,1]
// Expected = [6,6,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]