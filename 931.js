// 931. Minimum Falling Path Sum 🚫 INCOMPLETE - Time Limit Exceeded
/*
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
*/

var minFallingPathSum = function(matrix) {
    let minSum = Infinity
    for (let i = 0; i < matrix[0].length; i++) {
        minSum = Math.min(minSum, checkPath(matrix.slice(1), i, matrix[0][i]))
    }
    return minSum
    
    function checkPath(rows, col, sum) {
        if (!rows.length) return sum
        let left = Infinity, ctr = Infinity, right = Infinity
        if (rows[0][col - 1] !== undefined) {
            left = checkPath(rows.slice(1), col - 1, sum + rows[0][col - 1])
        }
        if (rows[0][col] !== undefined) {
            ctr = checkPath(rows.slice(1), col, sum + rows[0][col])
        }
        if (rows[0][col + 1] !== undefined) {
            right = checkPath(rows.slice(1), col + 1, sum + rows[0][col + 1])
        }
        return Math.min(left, right, ctr)
    }
};

console.log(minFallingPathSum([[2,1,3], [6,5,4], [7,8,9]]))
console.log(minFallingPathSum([[-19,57], [-40,-5]]))