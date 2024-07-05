// 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
/*
A critical point in a linked list is defined as either a local maxima or a local minima.
A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].
*/

var nodesBetweenCriticalPoints = function(head) {
    let minDist = Infinity, maxDist = -1
    let i = 0, firstCrIdx = -1, prevCrIdx = -1
    let prev = head
    let walker = head.next
    while (walker.next) {
        if (
            (walker.val > prev.val && walker.val > walker.next.val) ||
            (walker.val < prev.val && walker.val < walker.next.val)
        ) {
            if (firstCrIdx !== -1) {
                minDist = Math.min(minDist, i - prevCrIdx)
                maxDist = i - firstCrIdx
            } else {
                firstCrIdx = i
            }
            prevCrIdx = i
        }
        prev = walker
        walker = walker.next
        i++
    }
    if (minDist === Infinity) minDist = -1
    return [minDist, maxDist]
};

class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

const node7 = new ListNode(2)
const node6 = new ListNode(1, node7)
const node5 = new ListNode(5, node6)
const node4 = new ListNode(2, node5)
const node3 = new ListNode(1, node4)
const node2 = new ListNode(3, node3)
const testCase = new ListNode(5, node2)

// Display list as a string
let display = ""
let walker = testCase
while (walker) {
    display += walker.val.toString() + " => "
    walker = walker.next
}
console.log("INPUT\n", display + "null")

console.log("OUTPUT\n", nodesBetweenCriticalPoints(testCase))