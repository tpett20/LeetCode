// 82. Remove Duplicates from Sorted List II
// Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

var deleteDuplicates = function(head) {
    if (!head || !head.next) return head
    let walker = head
    let cachedNode
    let foundDuplicates = false
    while (walker.next) {
        let dupWalker = walker.next
        if (walker.val === dupWalker.val) {
            foundDuplicates = true
        }
        while (dupWalker && walker.val === dupWalker.val) {
            dupWalker = dupWalker.next
        }
        if (foundDuplicates) {
            if (cachedNode) {
                walker = cachedNode
                walker.next = dupWalker
            } else {
                head = dupWalker
                walker = head
            }
            foundDuplicates = false
            if (walker === null) break
        } else {
            cachedNode = walker
            if (walker && walker.next) {
                walker = walker.next
            } else break
        }
    }
    return head
};

class ListNode {
    constructor (val, next) {
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

const testCase = new ListNode(1)
testCase.append(2)
testCase.append(3)
testCase.append(3)
testCase.append(4)
testCase.append(5)
testCase.append(5)

console.log("INPUT")
testCase.printAsArray()
console.log("OUTPUT")
const result = deleteDuplicates(testCase)
result.printAsArray()