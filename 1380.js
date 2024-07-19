// 1380. Lucky Numbers in a Matrix
// Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
// A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

var luckyNumbers  = function(matrix) {
    const output = []
    const rowMins = new Set()
    for (const row of matrix) {
        rowMins.add(Math.min(...row))
    }
    for (let col = 0; col < matrix[0].length; col++) {
        let maxNum = -Infinity
        for (let row = 0; row < matrix.length; row++) {
            const num = matrix[row][col]
            maxNum = Math.max(num, maxNum)
        }
        if (rowMins.has(maxNum)) {
            output.push(maxNum)
        }
    }
    return output
};

console.log(luckyNumbers([[3,7,8], [9,11,13], [15,16,17]]))