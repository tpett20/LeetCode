// 1582. Special Positions in a Binary Matrix
// Given an m x n binary matrix mat, return the number of special positions in mat.
// A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

var numSpecial = function(mat) {
    let count = 0
    const rowMap = {}
    const colMap = {}
    for (let row = 0; row < mat.length; row++) {
        for (let col = 0; col < mat[row].length; col++) {
            if (mat[row][col] === 1) {
                rowMap[row] ? rowMap[row].length = 2 : rowMap[row] = [col]
                colMap[col] ? colMap[col].length = 2 : colMap[col] = [row]
            }
        }
    }
    for (let row in rowMap) {
        if (rowMap[row].length > 1) continue
        let sCol = rowMap[row][0]
        if (!colMap[sCol] || colMap[sCol].length > 1) continue
        let sRow = colMap[sCol][0]
        if (sRow === parseInt(row)) count++
    }
    return count
};

console.log(numSpecial([[1,0,0], [0,0,1], [1,0,0]]))
console.log(numSpecial([[1,0,0], [0,1,0], [0,0,1]]))