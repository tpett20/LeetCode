// Definition for singly - linked list.
class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }

    printAsArr() {
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

var convertListToArray = function(head) {
    const arr = []
    let walker = head
    while (walker) {
        console.log(walker.val)
        arr.push(walker.val)
        walker = walker.next
    }
}

var addOneToEachNode = function(head) {
    let walker = head
    while (walker) {
        walker.val++
        walker = walker.next
    }
}

let head = new ListNode(0)
head.next = new ListNode(1)
head.next.next = new ListNode(2)
head.printAsArr()
addOneToEachNode(head)
head.printAsArr()