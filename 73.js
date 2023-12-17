// 73. Set Matrix Zeroes
// Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
// You must do it in place.

var setZeroes = function(matrix) {
    const rowsOf0 = new Set()
    const colsOf0 = new Set()
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] === 0) {
                rowsOf0.add(i)
                colsOf0.add(j)
            }
        }
    }
    for (let row of rowsOf0) {
        for (let i = 0; i < matrix[row].length; i++) {
            matrix[row][i] = 0
        }
    }
    for (let col of colsOf0) {
        for (let i = 0; i < matrix.length; i++) {
            matrix[i][col] = 0
        }
    }
};

const testCase = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
console.log('Before:', testCase)
setZeroes(testCase)
console.log('After: ', testCase)