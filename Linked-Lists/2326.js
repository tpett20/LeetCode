// 2326. Spiral Matrix IV
/*
You are given two integers m and n, which represent the dimensions of a matrix.
You are also given the head of a linked list of integers.
Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
Return the generated matrix.
*/

var spiralMatrix = function(m, n, head) {
    const matrix = []
    for (let i = 0; i < m; i++) {
        const arr = []
        for (let j = 0; j < n; j++) {
            arr.push(-1)
        }
        matrix.push(arr)
    }

    let row = 0, rowFlr = 0, rowCeil = m
    let col = 0, colFlr = 0, colCeil = n
    let walker = head
    while (true) {
        // Right
        while (col < colCeil) {
            matrix[row][col] = walker.val
            col++
            walker = walker.next
            if (!walker) return matrix
        }
        col--
        row++
        rowFlr++
        // Down
        while(row < rowCeil) {
            matrix[row][col] = walker.val
            row++
            walker = walker.next
            if (!walker) return matrix
        }
        row--
        col--
        colCeil--
        // Left
        while(col >= colFlr) {
            matrix[row][col] = walker.val
            col--
            walker = walker.next
            if (!walker) return matrix
        }
        col++
        row--
        rowCeil--
        // Up
        while (row >= rowFlr) {
            matrix[row][col] = walker.val
            row--
            walker = walker.next
            if (!walker) return matrix
        }
        row++
        col++
        colFlr++
    }
    return matrix
};

class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}
const node3 = new ListNode(3)
const node2 = new ListNode(2, node3)
const testCase = new ListNode(1, node2)

console.log(spiralMatrix(2, 2, testCase))