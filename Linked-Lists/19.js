// 19. Remove Nth Node From End of List
// Given the head of a linked list, remove the nth node from the end of the list and return its head.

var removeNthFromEnd = function (head, n) {
    if (!head.next) {
        return n > 1 ? head : null
    }
    let walker = head
    let length = 0
    while (walker) {
        length++
        walker = walker.next
    }
    let target = length - n
    walker = head
    if (target === 0) return walker.next
    let count = 0
    while (count < target - 1) {
        count++
        walker = walker.next
    }
    let nextNode = walker.next.next
    walker.next = nextNode
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
            array.push(walker.val + ' ' + '->')
            walker = walker.next
        }
        array.push('null')
        console.log(array)
    }
}

const head = new ListNode(1)
head.append(2)
head.append(3)
head.append(4)
head.append(5)

let result = removeNthFromEnd(head, 2)
result.printAsArray()