// 876. Middle of the Linked List
/*
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
*/

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
            array.push(walker.val + ' ' + '->')
            walker = walker.next
        }
        array.push('null')
        console.log(array)
    }
}

var middleNode = function(head) {
    let count = 0
    let walker = head
    while (walker) {
        walker = walker.next
        count++
    }
    let middle = count / 2
    walker = head
    count = 1
    while (count <= middle) {
        walker = walker.next
        count++
    }
    return walker
};


const head = new ListNode(1)
head.append(2)
head.append(3)
head.append(4)
head.append(5)
head.append(6)

let result = middleNode(head)
result.printAsArray()