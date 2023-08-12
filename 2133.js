// 2133. Check if Every Row and Column Contains All Numbers
// An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
// Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

var checkValid = function(matrix) {
    let n = matrix[0].length
    for (let row of matrix) {
        const map = {}
        for (let col of row) {
            if (map[col] || col > n || col < 1) {
                return false
            } else {
                map[col] = true
            }
        }
    }
    let col = 0
    while (col < n) {
        const map = {}
        let row = 0
        while (row < n) {
            let val = matrix[row][col]
            if (map[val] || val > n || val < 1) {
                return false
            } else {
                map[val] = true
            }
            row++
        }
        col++
    }
    return true
};

const matrix = [[1,2,3], [3,1,2], [2,3,1]]
console.log(checkValid(matrix))