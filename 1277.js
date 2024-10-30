// 1277. Count Square Submatrices with All Ones
// Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

var countSquares = function(matrix) {
    function checkRow(r, c, sz) {
        for (let i = 0; i < sz; i++) {
            if (matrix[r][c + i] !== 1) return false
        }
        return true
    }

    function checkCol(r, c, sz) {
        for (let i = 0; i < sz; i++) {
            if (matrix[r + i][c] !== 1) return false
        }
        return true
    }

    function expandSquare(r, c) {
        let size = 1
        let nxtRow = r, nxtCol = c
        while (
            nxtRow < matrix.length &&
            nxtCol < matrix[0].length &&
            checkRow(nxtRow, c, size) &&
            checkCol(r, nxtCol, size)
        ) {
            size++
            nxtRow++
            nxtCol++
        }
        return size - 1
    }

    let count = 0
    for (let row = 0; row < matrix.length; row++) {
        for (let col = 0; col < matrix[0].length; col++) {
            count += expandSquare(row, col)
        }
    }
    return count
};

const testCase = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]
console.log(countSquares(testCase))