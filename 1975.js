// 1975. Maximum Matrix Sum
/*
You are given an n x n integer matrix. You can do the following operation any number of times:
- Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.
Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.
*/

var maxMatrixSum = function(matrix) {
    const n = matrix.length
    let negativeNums = 0
    let smallestAbs = Infinity
    let sum = 0
    for (let row = 0; row < n; row++) {
        for (let col = 0; col < n; col++) {
            const cell = matrix[row][col]
            const absCell = Math.abs(cell)
            if (cell < 0) negativeNums++
            smallestAbs = Math.min(absCell, smallestAbs)
            sum += absCell
        }
    }
    if (negativeNums % 2 == 0) {
        return sum
    } else {
        return sum - (smallestAbs * 2)
    }
};

const testCase = [
    [1, 2, 3],
    [-1, -2, -3],
    [1, 2, 3]
]

console.log(maxMatrixSum(testCase))

testCase[0][0] = 0
console.log(maxMatrixSum(testCase))