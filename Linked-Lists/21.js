// 21. Merge Two Sorted Lists
/* 
You are given the heads of two sorted linked lists: list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list. 
*/

function mergeTwoLists(list1, list2) {
    if (!list1) return list2
    else if (!list2) return list1
    let walker = list1
    while (list2 && (list2.val <= list1.val)) {
        let next = list1
        list1 = new ListNode(list2.val, next)
        walker = list1
        list2 = list2.next
    }
    while (list2 && walker.next) {
        if (list2.val <= walker.next.val) {
            let next = walker.next
            walker.next = new ListNode(list2.val, next)
            walker = walker.next
            list2 = list2.next
        } else {
            walker = walker.next
        }
    }
    if (list2) {
        walker.next = list2
    }
    return list1
};

class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
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

// TEST CASE

const list1 = new ListNode(0)
list1.next = new ListNode(2)
list1.next.next = new ListNode(4)
list1.next.next.next = new ListNode(7)
list1.next.next.next.next = new ListNode(8)

const list2 = new ListNode(1)
list2.next = new ListNode(3)
list2.next.next = new ListNode(5)
list2.next.next.next = new ListNode(6)
list2.next.next.next.next = new ListNode(9)

const result = mergeTwoLists(list1, list2)
result.printAsArray()