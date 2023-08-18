// 86. Partition List
// Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
// You should preserve the original relative order of the nodes in each of the two partitions.

var partition = function(head, x) {
    if (!head || !head.next) return head
    let walker = head
    let cachedNode
    let head2
    let walker2
    while (walker) {
        if (walker.val >= x) {
            if (!head2) {
                head2 = walker
                walker2 = head2
                walker = walker.next
                walker2.next = null
            } else {
                walker2.next = walker
                walker = walker.next
                walker2 = walker2.next
                walker2.next = null
            }
            if (!cachedNode) {
                head = walker
                walker = head
            } else {
                cachedNode.next = walker
            }
        } else {
            cachedNode = walker
            walker = walker.next
        }
    }
    if (!head) return head2
    else if (!head2) return head
    walker = head
    while (walker.next) {
        walker = walker.next
    }
    walker.next = head2
    return head
};

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
            array.push(walker.val + ' ->')
            walker = walker.next
        }
        array.push('null')
        console.log(array)
    }
}

const testCase = new ListNode(1)
testCase.append(4)
testCase.append(3)
testCase.append(2)
testCase.append(5)
testCase.append(2)
const x = 3

console.log(`INPUT, x = ${x}`)
testCase.printAsArray()
console.log("OUTPUT")
const result = partition(testCase, x)
result.printAsArray()