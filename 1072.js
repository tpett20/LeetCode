// 1072. Flip Columns For Maximum Number of Equal Rows
/*
You are given an m x n binary matrix matrix.
You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).
Return the maximum number of rows that have all values equal after some number of flips.
*/

var maxEqualRowsAfterFlips = function(matrix) {
    function flipBits(string) {
        let output = ""
        for (const bit of string) {
            if (bit === "1") {
                output += "0"
            } else {
                output += "1"
            }
        }
        return output
    }

    let maxEqual = 0
    const m = matrix.length
    const n = matrix[0].length
    const rows = {}
    for (let row = 0; row < m; row++) {
        let str = ""
        for (let col = 0; col < n; col++) {
            const cell = matrix[row][col]
            str += cell.toString()
        }
        rows[str] = rows[str] ? ++rows[str] : 1
    }
    const equalRow0 = "0".repeat(n)
    const equalRow1 = "1".repeat(n)
    if (rows[equalRow0]) {
        maxEqual += rows[equalRow0]
        rows[equalRow0] = 0
    }
    if (rows[equalRow1]) {
        maxEqual += rows[equalRow1]
        rows[equalRow1] = 0
    }
    for (const row in rows) {
        if (rows[row]) {
            const opposite = flipBits(row)
            let freq = rows[row]
            if (rows[opposite]) {
                freq += rows[opposite]
                rows[opposite] = 0
            }
            maxEqual = Math.max(maxEqual, freq)
        }
    }
    return maxEqual
};

const testCase = [
    [0,0,0],
    [0,0,1],
    [1,1,0]
]

console.log(maxEqualRowsAfterFlips(testCase))